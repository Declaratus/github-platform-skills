import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'lib'))
import liquid
import yaml
import resolve_liquid as r


class ResolverTests(unittest.TestCase):
    def setUp(self):
        temp_root = Path(__file__).resolve().parents[2] / '.build-cache/test-temp'
        temp_root.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=temp_root)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.reusables = self.root / 'reusables'
        self.reusables.mkdir()
        self.variables = {'product': {'name': 'Copilot', 'qwen3.8': 'Qwen', 'zero': 0}}
        self.tables = {'models': [{'name': 'Alpha', 'price': 2}, {'name': 'Beta', 'price': 3}]}

    def resolve(self, text):
        return r.resolve(text, self.variables, self.reusables, self.tables,
                         context={'defaultRestApiVersion': '2001-02-03'})

    def reusable(self, name, text):
        (self.reusables / (name + '.md')).write_text(text, encoding='utf-8')

    def test_dotted_key_and_zero(self):
        self.assertEqual(self.resolve('{% data variables.product.qwen3.8 %}/{% data variables.product.zero %}'), 'Qwen/0')

    def test_nested_multiline_list(self):
        self.reusable('outer', '{% data reusables.inner %}')
        self.reusable('inner', 'First\nSecond {% data variables.product.name %}')
        self.assertEqual(self.resolve('- {% data reusables.outer %}'), '- First\n  Second Copilot')

    def test_indented_code_inclusion(self):
        self.reusable('java', '```java\nprivate int n;\n```')
        self.assertEqual(self.resolve('{% indented_data_reference reusables.java spaces=3 %}'),
                         '   ```java\n   private int n;\n   ```')

    def test_missing_variable_and_reusable(self):
        for text in ['{% data variables.missing %}', '{% data reusables.missing %}']:
            with self.subTest(text=text), self.assertRaisesRegex(r.ResolutionError, 'Unresolved data'):
                self.resolve(text)

    def test_cycle_is_named(self):
        self.reusable('a', '{% data reusables.b %}')
        self.reusable('b', '{% data reusables.a %}')
        with self.assertRaisesRegex(r.ResolutionError, 'reusables.a -> reusables.b -> reusables.a'):
            self.resolve('{% data reusables.a %}')

    def test_depth_and_idempotence(self):
        for i in range(24):
            self.reusable(str(i), '{% data reusables.' + str(i+1) + ' %}' if i < 23 else 'DONE')
        result = self.resolve('{% data reusables.0 %}')
        self.assertEqual(result, 'DONE')
        self.assertEqual(self.resolve(result), result)
        for i in range(24, 68):
            self.reusable(str(i), '{% data reusables.' + str(i+1) + ' %}')
        self.reusable('23', '{% data reusables.24 %}')
        with self.assertRaisesRegex(r.ResolutionError, 'nesting exceeds'):
            self.resolve('{% data reusables.0 %}')

    def test_size_is_bounded(self):
        self.reusable('large', 'x' * (r.MAX_SIZE + 1))
        with self.assertRaisesRegex(r.ResolutionError, '8 MB'):
            self.resolve('{% data reusables.large %}')

    def test_ordinary_table_and_row_condition(self):
        self.assertEqual(self.resolve('{% for row in tables.models %}{{ row.name }}{% if row.price == 2 %}!{% else %}?{% endif %}{% endfor %}'), 'Alpha!Beta?')

    def test_version_outside_table(self):
        branch = '{% ifversion ghec %}Cloud{% else %}Server{% endif %}'
        self.assertEqual(self.resolve(branch + '{% for m in tables.models %}{{m.name}}{% endfor %}'), branch + 'AlphaBeta')

    def test_nested_version_inside_table(self):
        branch = '{% ifversion ghec %}{% ifversion feature %}{{m.name}}{% else %}B{% endif %}{% elsif ghes %}C{% else %}D{% endif %}'
        output = self.resolve('{% for m in tables.models %}' + branch + '{% endfor %}')
        self.assertEqual(output, branch.replace('{{m.name}}', 'Alpha') + branch.replace('{{m.name}}', 'Beta'))

    def test_table_in_both_version_alternatives(self):
        loop = '{% for m in tables.models %}{{m.name}}{% endfor %}'
        self.assertEqual(self.resolve('{% ifversion ghec %}' + loop + '{% else %}' + loop + '{% endif %}'),
                         '{% ifversion ghec %}AlphaBeta{% else %}AlphaBeta{% endif %}')

    def test_literal_raw_and_fence_survive_adjacent_table(self):
        literal = '```liquid\n{% raw %}{% data variables.product.name %}{% endraw %}\n{{ user.name }}\n{% if user %}example{% endif %}\n```\n'
        loop = '{% for row in tables.models %}{{row.name}}{% endfor %}'
        self.assertEqual(self.resolve(literal + loop), literal + 'AlphaBeta')

    def test_literal_table_example_in_fence(self):
        literal = '```liquid\n{% for m in tables.missing %}{{m.name}}{% endfor %}\n```\n'
        self.assertEqual(self.resolve(literal), literal)

    def test_unrelated_output_prose_and_conditions(self):
        prose = 'Discuss tables.models and {{ user.name }}. {% if user %}A{% else %}B{% endif %}'
        self.assertEqual(self.resolve(prose), prose)
        self.assertEqual(self.resolve(prose + '{{tables.models[0].name}}'), prose + 'Alpha')

    def test_missing_table_output_and_iteration(self):
        for text in ['{{ tables.missing }}', '{% for m in tables.missing %}lost{% endfor %}',
                     '{% for m in tables.models %}{{m.misspelled}}{% endfor %}']:
            with self.subTest(text=text), self.assertRaises(liquid.exceptions.UndefinedError):
                self.resolve(text)

    def test_data_carried_by_table_value(self):
        self.tables['models'][0]['name'] = '{% data variables.product.name %}'
        self.assertEqual(self.resolve('{{tables.models[0].name}}'), 'Copilot')

    def test_loop_local_does_not_evaluate_unrelated_prose(self):
        loop = '{% for row in tables.models %}{{row.name}}{% endfor %}'
        literal = 'Example outside loop: `{{row.name}}`.'
        self.assertEqual(self.resolve(literal + loop + literal), literal + 'AlphaBeta' + literal)

    def test_constant_condition_in_version_inside_loop(self):
        self.assertEqual(self.resolve('{% for m in tables.models %}{% ifversion ghec %}{% if true %}{{m.name}}{% else %}wrong{% endif %}{% endif %}{% endfor %}'),
                         '{% ifversion ghec %}Alpha{% endif %}{% ifversion ghec %}Beta{% endif %}')

    def test_preserve_unrelated_empty_table_row(self):
        table = '| A | B |\n| --- | --- |\n| | |\n'
        self.assertEqual(self.resolve(table + '{{tables.models[0].name}}'), table + 'Alpha')

    def test_no_empty_loop_wrapper_rows(self):
        out = self.resolve('| {% for m in tables.models %} |\n| {{m.name}} |\n| {% endfor %} |\n')
        self.assertNotIn('| |', out)
        self.assertIn('| Alpha |', out)
        self.assertIn('| Beta |', out)
        self.assertNotIn('\n\n|', out)

    def test_loop_and_if_wrapper_rows(self):
        text = '| {% for m in tables.models %}{% if m.price == 2 %} |\n| {{m.name}} |\n| {% endif %}{% endfor %} |\n'
        self.assertEqual(self.resolve(text), '| Alpha |\n')

    def test_writer_comment_does_not_parse_literal_tags(self):
        self.assertEqual(self.resolve('{% comment %}Example {% for x in tables.missing %}{% endcomment %}text'), 'text')

    def test_frontmatter_semantics_quotes_unicode_newline(self):
        self.variables['product']['text'] = "organization's \"legal\" folder: café\nsecond line"
        source = "---\nproduct: '{% data variables.product.text %}'\ncount: 3\nitems: [one, two]\n---\nBody\n"
        output = self.resolve(source)
        parsed = yaml.safe_load(r.FRONT.match(output)[1])
        self.assertEqual(parsed, {'product': self.variables['product']['text'], 'count': 3, 'items': ['one', 'two']})
        self.assertEqual(self.resolve(output), output)

    def test_frontmatter_multiline_reusable_has_no_body_padding(self):
        self.reusable('lines', 'Line one.\n\nLine two.')
        self.reusable('nested', 'Nested: {% data reusables.lines %}')
        for inclusion, expected in [
                ('lines', 'Prefix text.<br>Line one.\n\nLine two.'),
                ('nested', 'Prefix text.<br>Nested: Line one.\n\nLine two.')]:
            with self.subTest(inclusion=inclusion):
                source = '---\nproduct: "Prefix text.<br>{% data reusables.' + inclusion + ' %}"\n---\nBody\n'
                output = self.resolve(source)
                self.assertEqual(yaml.safe_load(r.FRONT.match(output)[1]), {'product': expected})
                self.assertEqual(self.resolve(output), output)

    def test_frontmatter_preserves_existing_scalar_whitespace(self):
        self.reusable('lines', 'Line one.\n\n  Line two.')
        source = '---\nproduct: |+\n  Prefix: {% data reusables.lines %}\n    Existing indentation.\n\n---\nBody\n'
        # Literal YAML indentation is decoded before data substitution. Only
        # whitespace from the author and reusable may enter this scalar.
        expected = 'Prefix: Line one.\n\n  Line two.\n  Existing indentation.\n'
        output = self.resolve(source)
        self.assertEqual(yaml.safe_load(r.FRONT.match(output)[1]), {'product': expected})
        self.assertEqual(self.resolve(output), output)

    def test_frontmatter_and_body_use_distinct_continuation_rules(self):
        self.reusable('lines', 'Line one.\n\nLine two.')
        source = '---\nproduct: "Prefix: {% data reusables.lines %}"\n---\n- {% data reusables.lines %}\n'
        output = self.resolve(source)
        self.assertEqual(yaml.safe_load(r.FRONT.match(output)[1]),
                         {'product': 'Prefix: Line one.\n\nLine two.'})
        self.assertEqual(output[r.FRONT.match(output).end():], '- Line one.\n  \n  Line two.\n')

    def test_multiline_plain_scalar_boundary(self):
        source = '---\nintro: This describes\n  {% data variables.product.name %}.\nversions:\n  feature: copilot\n---\n'
        parsed = yaml.safe_load(r.FRONT.match(self.resolve(source))[1])
        self.assertEqual(parsed, {'intro': 'This describes Copilot.', 'versions': {'feature': 'copilot'}})

    def test_raw_scalar_and_fenced_raw_idempotence(self):
        source = '---\nintro: "{% raw %}{{ literal }}{% endraw %}"\n---\n```yaml\n{% raw %}${{ secrets.TOKEN }}{% endraw %}\n```\n'
        self.assertEqual(self.resolve(source), source)

    def test_api_default_requires_context(self):
        with self.assertRaisesRegex(r.ResolutionError, 'site context'):
            r.resolve('{{ defaultRestApiVersion }}', {}, self.reusables, {})
        self.assertEqual(self.resolve('```sh\n-H "X: {{ defaultRestApiVersion }}"\n```'), '```sh\n-H "X: 2001-02-03"\n```')

    def test_malformed_data_inclusion_fails(self):
        for text in ['{% data variables.product.name unexpected %}',
                     '{% indented_data_reference reusables.java spaces=oops %}']:
            with self.subTest(text=text), self.assertRaisesRegex(r.ResolutionError, 'malformed'):
                self.resolve(text)

    def test_malformed_table_program_fails(self):
        with self.assertRaises(r.ResolutionError):
            self.resolve('{% for m in tables.models %}missing endfor')

    def test_tree_validation_before_any_write(self):
        (self.root / 'variables').mkdir()
        (self.root / 'tables').mkdir()
        (self.root / 'variables/product.yml').write_text('name: Copilot')
        pages = self.root / 'pages'; pages.mkdir()
        good = pages / 'a.md'; bad = pages / 'z.md'
        good.write_text('---\ntitle: Good\n---\n{% data variables.product.name %}')
        bad.write_text('---\ntitle: Bad\n---\n{% data variables.missing %}')
        with self.assertRaisesRegex(r.ResolutionError, 'z.md'):
            r.resolve_tree(self.root, pages, {})
        self.assertEqual(good.read_text(), '---\ntitle: Good\n---\n{% data variables.product.name %}')


if __name__ == '__main__':
    unittest.main()

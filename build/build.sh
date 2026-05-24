#!/usr/bin/env bash
# Rebuild skill references from upstream sources.
#
# Usage:
#   ./build/build.sh <plugin-name>      # rebuild one
#   ./build/build.sh --all              # rebuild every plugin with a recipe
#   ./build/build.sh --list             # list available recipes
#
# Each plugin that needs upstream content has a recipe at
# build/recipes/<plugin-name>.sh. Plugins without a recipe are
# hand-curated and have no automated rebuild.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export REPO_ROOT
RECIPE_DIR="$REPO_ROOT/build/recipes"

usage() {
  cat <<EOF
Usage:
  $(basename "$0") <plugin-name>   rebuild one plugin's references/
  $(basename "$0") --all           rebuild every plugin that has a recipe
  $(basename "$0") --list          list available recipes
EOF
}

list_recipes() {
  find "$RECIPE_DIR" -maxdepth 1 -name '*.sh' -type f \
    | sed -e "s|^$RECIPE_DIR/||" -e 's|\.sh$||' \
    | sort
}

run_recipe() {
  local name="$1"
  local recipe="$RECIPE_DIR/$name.sh"
  if [[ ! -f "$recipe" ]]; then
    echo "ERROR: no recipe at $recipe" >&2
    echo "       (this plugin may be hand-curated with no upstream)" >&2
    return 1
  fi
  echo "→ $name"
  bash "$recipe"
}

case "${1:-}" in
  ""|-h|--help)
    usage
    exit 0
    ;;
  --list)
    list_recipes
    ;;
  --all)
    while read -r name; do
      [[ -z "$name" ]] && continue
      run_recipe "$name"
    done < <(list_recipes)
    ;;
  *)
    run_recipe "$1"
    ;;
esac

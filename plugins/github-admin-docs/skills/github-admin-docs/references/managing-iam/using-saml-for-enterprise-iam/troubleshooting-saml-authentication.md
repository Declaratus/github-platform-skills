---
title: Troubleshooting SAML authentication
shortTitle: Troubleshoot SAML SSO
intro: If you use SAML single sign-on (SSO) and people are unable to authenticate to access GitHub, you can troubleshoot the problem.
versions:
  ghes: '*'
  ghec: '*'
redirect_from:
  - /admin/identity-and-access-management/using-saml-for-enterprise-iam/troubleshooting-saml-authentication
contentType: how-tos
category:
  - Configure authentication
---

{% ifversion ghes %}

## About problems with SAML authentication

GitHub Enterprise Server logs error messages for failed SAML authentication in the systemd journal logs for the `github-unicorn` container. You can review responses in this log, and you can also configure more verbose logging.

For more information about SAML response requirements, see [AUTOTITLE](/admin/managing-iam/iam-configuration-reference/saml-configuration-reference#saml-response-requirements).

## Configuring SAML debugging

You can configure GitHub Enterprise Server to write verbose debug logs for every SAML authentication attempt. You may be able to troubleshoot failed authentication attempts with this extra output.

> [!WARNING]
>
> * Only enable SAML debugging temporarily, and disable debugging immediately after you finish troubleshooting. If you leave debugging enabled, the size of the logs increases much faster than usual, which can negatively impact the performance of GitHub Enterprise Server.
> * Test new authentication settings for {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} in a staging environment before you apply the settings in your production environment. For more information, see [AUTOTITLE](/admin/installing-your-enterprise-server/setting-up-a-github-enterprise-server-instance/setting-up-a-staging-instance).

{%- ifversion ghes %}
1. In the top-right corner of GitHub Enterprise Server, click your profile picture, then click **Enterprise settings**.
{%- else %}
1. Navigate to your enterprise. For example, from the [Enterprises](https://github.com/settings/enterprises?ref_product=ghec&ref_type=engagement&ref_style=text) page on GitHub.com.
{%- endif %}
1. At the top of the page, click **(icon: law) Policies**.
1. Under {% ifversion ghes %} **(icon: law) Policies**{% else %}"(icon: gear) Settings"{% endif %}, click **Options**.

1. Under "SAML debugging", select the drop-down and click **Enabled**.
1. Attempt to sign in to {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} through your SAML IdP.
1. Review the debug output in the `systemd` journal for `github-unicorn` on {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}. For more information, see [AUTOTITLE](/admin/monitoring-and-managing-your-instance/monitoring-your-instance/about-system-logs#system-logs-in-the-systemd-journal-for-github-enterprise-server).
1. When you're done troubleshooting, select the drop-down and click **Disabled**.

## Decoding responses

Some output in the `systemd` journal for `github-unicorn` may be Base64-encoded. You can access the administrative shell and use the `base64` utility on {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} to decode these responses. For more information, see [AUTOTITLE](/admin/administering-your-instance/administering-your-instance-from-the-command-line/accessing-the-administrative-shell-ssh).

To decode the output, run the following command, replacing `ENCODED_OUTPUT` with the encoded output from the log.

```shell
base64 --decode ENCODED_OUTPUT
```

## Error: "Another user already owns the account"

When a user signs into {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %} for the first time with SAML authentication, GitHub creates a user account on the instance and maps the SAML `NameID` and `nameid-format` to the account.

When the user signs in again, GitHub Enterprise Server compares the account's `NameID` and `nameid-format` mapping to the IdP's response. If the `NameID` or `nameid-format` in the IdP's response no longer matches the values that GitHub expects for the user, the sign-in will fail. The user will see the following message.

> Another user already owns the account. Please have your administrator check the authentication log.

The message typically indicates that the person's username or email address has changed on the IdP. Ensure that the `NameID` and `nameid-format` mapping for the user account on GitHub Enterprise Server matches the user's `NameID` and `nameid-format` on your IdP. For more information, see [AUTOTITLE](/admin/managing-iam/using-saml-for-enterprise-iam/updating-a-users-saml-nameid).

## Error: Recipient in SAML response was blank or not valid

If the `Recipient` does not match the ACS URL for {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}, one of the following two error messages will appear in the authentication log when a user attempts to authenticate.

```text
Recipient in the SAML response must not be blank.
```

```text
Recipient in the SAML response was not valid.
```

Ensure that you set the value for `Recipient` on your IdP to the full ACS URL for {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}. For example, `https://ghe.corp.example.com/saml/consume`.

## Error: "SAML Response is not signed or has been modified"

If your IdP does not sign the SAML response, or the signature does not match the contents, the following error message will appear in the authentication log.

```text
SAML Response is not signed or has been modified.
```

Ensure that you configure signed assertions for the GitHub application on your IdP.

## Error: "Audience is invalid" or "No assertion found"

If the IdP's response has a missing or incorrect value for `Audience`, the following error message will appear in the authentication log.

```text
Audience is invalid. Audience attribute does not match https://YOUR-INSTANCE-URL
```

Ensure that you set the value for `Audience` on your IdP to the `EntityId` for {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}, which is the full URL to your instance. For example, `https://ghe.corp.example.com`.
{% endif %}

## Error: "Current time is earlier than NotBefore condition"

This error can occur when there's too large of a time difference between your IdP and GitHub, which commonly occurs with self-hosted IdPs.

{% ifversion ghes %}To prevent this problem, we recommend pointing your appliance to the same Network Time Protocol (NTP) source as your IdP, if possible. {% endif %}If you encounter this error, make sure the time on your {% ifversion ghes %}appliance{% else %}IdP{% endif %} is properly synced with your NTP server. {% ifversion ghes %}You can use the `chronyc` command on the administrative shell to synchronize time immediately. For more information, see [AUTOTITLE](/admin/configuring-settings/configuring-network-settings/configuring-time-synchronization#correcting-a-large-time-drift).{% endif %}

If you use ADFS as your IdP, also set `NotBeforeSkew` in ADFS to 1 minute for GitHub. If `NotBeforeSkew` is set to 0, even very small time differences, including milliseconds, can cause authentication problems.

{% ifversion ghes %}

## Error: "failure - Updated SAML validation returned an invalid result"

This error can occur in version 3.17.0 or later of {% ifversion ghes %}your GitHub Enterprise Server instance{% else %}GitHub.com{% endif %}. It indicates that GitHub is unable to properly process the SAML response it received from the identity provider. Please open a GitHub support ticket so that the GitHub Support and Engineering teams can investigate and address the issue.

{% endif %}

{% ifversion ghec %}
## Users are repeatedly redirected to authenticate

If users are repeatedly redirected to the SAML authentication prompt in a loop, you may need to increase the SAML session duration in your IdP settings.

The `SessionNotOnOrAfter` value sent in a SAML response determines when a user will be redirected back to the IdP to authenticate. If a SAML session duration is configured for 2 hours or less, GitHub will refresh a SAML session 5 minutes before it expires. If your session duration is configured as 5 minutes or less, users can get stuck in a SAML authentication loop.

To fix this problem, we recommend configuring a minimum SAML session duration of 4 hours. For more information, see [AUTOTITLE](/admin/managing-iam/iam-configuration-reference/saml-configuration-reference#session-duration-and-timeout).
{% endif %}

## Error: Digest mismatch

A "Digest mismatch" error indicates that your SAML IdP is using a different SAML signing certificate than the one you have uploaded to GitHub{% ifversion ghes %} or that the **Signature Method** or **Digest Method** configured on GitHub differs from what your IdP is using{% endif %}.

{% ifversion ghes %}Re-download this SAML certificate from your IdP and validate it using an online tool, such as the [Format a x509 cert](https://www.samltool.com/format_x509cert.php) tool from OneLogin. Then upload the SAML certificate again in the "Authentication" section in your GitHub Enterprise Server management console. See [AUTOTITLE](/admin/administering-your-instance/administering-your-instance-from-the-web-ui/accessing-the-management-console#accessing-the-as-an-unauthenticated-user).{% endif %}

{% ifversion ghec %}Re-download this SAML certificate from your IdP and validate it using a tool such as the [Format a x509 cert](https://www.samltool.com/format_x509cert.php) tool from OneLogin. Then update the certificate saved in the GitHub SAML settings.{% endif %}

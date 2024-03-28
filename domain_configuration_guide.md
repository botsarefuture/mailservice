Below is a detailed domain configuration guide for setting up your domain to send emails through the email sending service hosted at "mailservice.luova.club":

# Domain Configuration Guide

This guide will walk you through the steps to configure your domain for sending emails using the email sending service hosted at "mailservice.luova.club". The configuration involves adding SPF and DKIM records to your domain's DNS settings and verifying domain ownership.

## 1. Add SPF Record (Sender Policy Framework)

- SPF records specify which mail servers are authorized to send emails on behalf of your domain. Adding an SPF record helps prevent spoofing and improves email deliverability.

- Log in to your DNS management dashboard provided by your domain registrar or hosting provider.

- Navigate to the DNS settings for your domain.

- Create a new TXT record with the following details:
  - Name/Host/Alias: `@` (or your domain name)
  - Value: `"v=spf1 include:mail.luova.club ~all"`
  - TTL: Leave it as default or set according to your preference.

- Save the changes to update your DNS settings.

## 2. Add DKIM Record (DomainKeys Identified Mail)

- DKIM records add a digital signature to your outgoing emails, which helps verify the authenticity of the sender and prevent email spoofing.

- Obtain the DKIM public key from the email sending service provider (in this case, "mailservice.luova.club").

- Log in to your DNS management dashboard provided by your domain registrar or hosting provider.

- Navigate to the DNS settings for your domain.

- Create a new TXT record with the following details:
  - Name/Host/Alias: `mail._domainkey` (or whatever DKIM selector you are using)
  - Value: Paste the entire DKIM public key obtained from the email sending service provider.
  - TTL: Leave it as default or set according to your preference.

- Save the changes to update your DNS settings.

## 3. Verify Domain Ownership

- Some email sending services require domain verification to ensure domain ownership and prevent misuse.

- Follow the instructions provided by the email sending service provider to verify your domain ownership. This step may involve adding a specific DNS TXT record to your domain's DNS settings with a unique value provided by the service.

- After adding the verification record, allow some time for DNS propagation. This process can take up to 48 hours, although changes often take effect much sooner.

## 4. Test Email Sending

- Once the SPF and DKIM records are added and domain ownership is verified, test the email sending functionality.

- Send test emails from your domain and verify that they are successfully delivered to recipients' inboxes without being marked as spam.

By following these steps, you can configure your domain to send emails through the email sending service hosted at "mailservice.luova.club". Ensure to carefully follow the instructions provided by your email service provider and regularly monitor email deliverability to maintain a reliable email sending setup.

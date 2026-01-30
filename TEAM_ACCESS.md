# Team Access Management

This document outlines the procedures for granting and managing repository access for team members working on the llm-benchmarking-py project.

## Table of Contents

- [Access Levels](#access-levels)
- [Requesting Access](#requesting-access)
- [Granting Access](#granting-access)
- [Access Review](#access-review)
- [Revoking Access](#revoking-access)
- [Security Requirements](#security-requirements)
- [Contact Information](#contact-information)

## Access Levels

### Read Access

**Permissions:**
- Clone and pull the repository
- View code and files
- View issues and pull requests
- Fork the repository
- Create issues

**Typical Users:**
- External contributors
- Documentation reviewers
- Project observers
- Stakeholders

### Write Access

**Permissions:**
- All Read permissions
- Push to non-protected branches
- Create and delete branches
- Create, edit, and close issues
- Create and merge pull requests
- Apply labels and milestones

**Typical Users:**
- Active developers
- Team members contributing code
- Quality assurance engineers
- Technical writers with commit access

### Maintain Access

**Permissions:**
- All Write permissions
- Manage issues and pull requests (without merge access to protected branches)
- Push to protected branches (with approval)
- Manage project boards
- Manage wiki

**Typical Users:**
- Project leads
- Senior developers
- Release managers

### Admin Access

**Permissions:**
- All Maintain permissions
- Manage repository settings
- Manage team access and permissions
- Add/remove collaborators
- Delete repository (restricted)
- Manage security and alerts
- Manage branch protection rules

**Typical Users:**
- Repository owners
- Technical leads
- Engineering managers

## Requesting Access

### For New Team Members

#### Step 1: Prepare Your Request

Before requesting access, ensure you have:

1. ✅ A GitHub/GitLab account with two-factor authentication enabled
2. ✅ Company email address
3. ✅ Manager approval (if required by your organization)
4. ✅ Clear understanding of your role in the project

#### Step 2: Submit Access Request

Choose one of the following methods:

**Method 1: GitHub Issue (Recommended)**

1. Go to the repository's Issues page
2. Click "New Issue"
3. Select "Repository Access Request" template
4. Fill out all required fields
5. Submit the issue

**Method 2: Email Request**

Send an email to the repository maintainer(s) with:

- **Subject:** "Repository Access Request - [Your Name]"
- **Body should include:**
  - Full name
  - Company email
  - GitHub/GitLab username
  - Team/Department
  - Requested access level (Read/Write/Maintain/Admin)
  - Reason for access
  - Areas you'll be working on
  - Manager approval (if applicable)

**Contact:**
- Primary: Matthew Truscott (matthew.truscott@turintech.ai)

**Method 3: Slack/Teams Message**

Contact the maintainers directly via company communication channels with the same information as the email method.

#### Step 3: Wait for Approval

- Access requests are typically reviewed within 2-3 business days
- Urgent requests can be expedited (mark as urgent in your request)
- You'll receive notification via email once access is granted

#### Step 4: Accept Invitation

1. Check your email for the repository invitation
2. Click the invitation link
3. Accept the invitation
4. Verify you can access the repository
5. Set up your local development environment (see [CONTRIBUTING.md](CONTRIBUTING.md))

### For External Contributors

External contributors (non-team members) can:

- Fork the repository
- Create pull requests from their fork
- Participate in discussions
- Report issues

No special access request is needed for external contributions.

## Granting Access

### For Repository Administrators

#### Access Request Review Checklist

Before granting access, verify:

- [ ] Requestor is a verified team member or approved contractor
- [ ] Two-factor authentication is enabled on their account
- [ ] Request includes all required information
- [ ] Requested access level is appropriate for their role
- [ ] Manager approval obtained (if required)
- [ ] Requestor has acknowledged reading CONTRIBUTING.md

#### Granting Access via GitHub

1. Go to repository Settings → Collaborators and teams
2. Click "Add people" or "Add teams"
3. Enter the user's GitHub username or email
4. Select the appropriate role:
   - **Read** → Read
   - **Triage** → Triage
   - **Write** → Write
   - **Maintain** → Maintain
   - **Admin** → Admin
5. Click "Add [username] to this repository"
6. Update the access request issue with status
7. Add user to relevant documentation (if needed)

#### Granting Access via GitLab

1. Go to Project → Members
2. Click "Invite members"
3. Enter username or email
4. Select role (Guest/Reporter/Developer/Maintainer/Owner)
5. Set expiration date (if temporary)
6. Click "Invite"

#### Post-Grant Actions

After granting access:

1. ✅ Comment on the access request issue confirming access granted
2. ✅ Close the access request issue
3. ✅ Send welcome message with:
   - Link to CONTRIBUTING.md
   - Link to relevant documentation
   - Team communication channels
   - Key contacts
4. ✅ Add user to CODEOWNERS file (if they'll own specific code areas)
5. ✅ Update internal team roster (if applicable)
6. ✅ Schedule onboarding session (if needed)

#### Welcome Message Template

```
Hi @username,

Welcome to the llm-benchmarking-py project! Your access has been granted with [ACCESS_LEVEL] permissions.

**Next Steps:**
1. Review the [CONTRIBUTING.md](CONTRIBUTING.md) guidelines
2. Set up your development environment (instructions in README.md)
3. Join our team communication channels: [CHANNEL_INFO]
4. Check out the current issues and pick something to work on

**Key Resources:**
- Documentation: [LINK]
- Team Wiki: [LINK]
- Code Style Guide: See CONTRIBUTING.md

If you have any questions, feel free to reach out to:
- @matthew-truscott
- Or ask in [COMMUNICATION_CHANNEL]

Looking forward to your contributions!
```

## Access Review

### Regular Access Audits

Repository administrators should conduct regular access reviews:

**Quarterly Reviews:**
- Review all users with Write, Maintain, or Admin access
- Verify users still require their current access level
- Remove inactive users (no activity in 90+ days)
- Update access levels as team roles change

**Annual Reviews:**
- Complete audit of all repository access
- Verify compliance with security policies
- Review and update access procedures
- Update CODEOWNERS file

### Access Review Process

1. Export current list of collaborators
2. Cross-reference with active team roster
3. Identify users who:
   - Are no longer with the organization
   - Have changed roles
   - Have been inactive for extended periods
4. Contact users to confirm continued need for access
5. Update access levels as needed
6. Document changes in access log

## Revoking Access

### When to Revoke Access

Access should be revoked when:

- Team member leaves the organization
- Contract or project ends
- Role changes no longer require access
- User has been inactive for 90+ days
- Security policy violation
- Upon user request

### Revocation Process

#### For Immediate Revocation (Security Concerns)

1. **Immediately** remove user from repository
2. Revoke any personal access tokens
3. Review recent activity for any suspicious changes
4. Notify security team if needed
5. Document the incident

#### For Standard Revocation (Departure/Role Change)

1. Receive notification of departure/role change
2. Schedule access revocation for last working day
3. Ensure knowledge transfer is complete
4. Remove repository access
5. Remove from:
   - Collaborators list
   - CODEOWNERS file (if listed)
   - Team communication channels
   - Documentation (if needed)
6. Document in access log
7. Archive any important work/documentation

#### GitHub Access Revocation Steps

1. Go to Settings → Collaborators and teams
2. Find the user
3. Click the settings icon next to their name
4. Click "Remove from repository"
5. Confirm removal

## Security Requirements

### Mandatory Requirements

All users with repository access must:

1. **Enable Two-Factor Authentication (2FA)**
   - Required for all access levels
   - Use authenticator app or security key
   - SMS backup acceptable as secondary method

2. **Use Strong Passwords**
   - Minimum 12 characters
   - Mix of uppercase, lowercase, numbers, symbols
   - Unique password (not reused from other sites)

3. **Keep Credentials Secure**
   - Never share passwords or access tokens
   - Store credentials in secure password manager
   - Never commit credentials to repository

4. **Use SSH Keys or Personal Access Tokens**
   - For Git operations
   - Rotate tokens regularly (every 90 days)
   - Use scoped tokens with minimal permissions

5. **Keep Software Updated**
   - Use latest Git client
   - Keep OS and security software updated
   - Apply security patches promptly

### Best Practices

- Use company-issued devices for repository access
- Don't access repository over public WiFi without VPN
- Log out of shared computers
- Report suspicious activity immediately
- Review audit logs of your own activity
- Use branch protection and require reviews
- Never force push to main/master branch
- Keep local copies encrypted

### Security Incident Response

If you suspect a security issue:

1. **Immediately** report to:
   - Repository administrators
   - Your manager
   - Security team
2. **Do not** attempt to investigate on your own
3. **Do not** discuss publicly until cleared by security team
4. Document what you observed
5. Follow security team instructions

## Contact Information

### Repository Maintainers

**Primary Maintainer:**
- Name: Matthew Truscott
- Email: matthew.truscott@turintech.ai
- GitHub: @matthew-truscott

### Access Request Contacts

For access requests or questions:
1. Open an issue using the "Repository Access Request" template
2. Email: matthew.truscott@turintech.ai
3. Internal communication channels (Slack/Teams)

### Emergency Access

For urgent access needs (production issues, security concerns):
- Contact primary maintainer directly
- Mark request as "URGENT" in subject line
- Include specific reason for urgency
- Expect response within 4 business hours

## Additional Resources

- [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guidelines
- [CODEOWNERS](CODEOWNERS) - Code ownership structure
- [README.md](README.md) - Project overview and setup
- [GitHub Access Permissions Documentation](https://docs.github.com/en/organizations/managing-access-to-your-organizations-repositories/repository-permission-levels-for-an-organization)

---

**Document Version:** 1.0  
**Last Updated:** 2024  
**Next Review:** Quarterly  
**Owner:** Matthew Truscott

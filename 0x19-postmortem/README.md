#	`0x19. Postmortem`

### My first postmortem
=======================

## Issue Summary
 
 * Duration of Outage: The outage occurred from 10:00 AM to 11:30 AM (UTC) on Oct, 10, 2023.
 * Impact: The Nginx server outage resulted in the unavailability of the website, which serves as the primary platform for Debugging interactions. Users experienced downtime during the incident, affecting approximately 100% of our Student base.

## Timeline

 * 06:00 PM (UTC): Issue detected through an Student noticed something indicating Nginx server unresponsiveness.
 * 06:05 PM (UTC): Student Notice and started investigating.
 * 06:15 PM (UTC): Initial investigation focused on server resource utilization and network connectivity.
 * 06:45 PM (UTC): The issue was escalated to the infrastructure team for further analysis.
 * 07:00 PM (UTC): Root cause identified as a misconfiguration in the Nginx configuration file.
 * 07:15 PM (UTC): The Nginx configuration was corrected, and the server was restarted.
 * 07:30 PM (UTC): The issue was resolved, and normal service was restored.

## Root Cause and Resolution:

 * Root Cause: The root cause of the issue was a misconfiguration in the Nginx server's configuration file. Specifically, Listing port Number error was present in one of the location directives, causing the Nginx server to fail to start.

 * Resolution: To resolve the issue, the misconfigured Nginx configuration file was corrected. The erroneous Listing Port Number was identified and fixed, and then the Nginx server was restarted to apply the changes. Once the Nginx server was successfully restarted, the Server became accessible, and the outage was resolved.

## Corrective and Preventative Measures:

To prevent similar incidents in the future and improve system reliability, the following actions will be taken:

1. Regular Configuration Audits: Implement a regular schedule for auditing Nginx configuration files to identify and rectify potential misconfigurations before they cause outages.
2. Automated Testing: Develop automated tests for Nginx configuration files to catch any errors and other issues before they are deployed into production. 
3. Configuration Version Control: Utilize version control systems for Nginx configuration files to track changes and facilitate easier rollback in case of issues.
4. Enhanced Monitoring: Improve server monitoring to detect issues more proactively, including the capability to identify configuration-related problems.
5. Documentation and Training: Ensure that team members are well-versed in Nginx best practices and maintain up-to-date documentation on server configurations.
6. Incident Response Plan: Formalize an incident response plan to expedite the resolution process when such issues occur, including clear escalation procedures and communication protocols.

* These measures are essential for maintaining system stability and preventing similar Nginx server outages in the future. The incident served as a valuable lesson, highlighting the importance of regular configuration checks and proactive monitoring to ensure the uninterrupted operation of critical services.

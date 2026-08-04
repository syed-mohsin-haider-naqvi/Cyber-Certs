# Cloud Scripts

Python scripts using Boto3 (AWS's python library) to interact with AWS directly — automating stuff instead of clicking through the console every time. Built alongside the AWS Cloud Practitioner material and the hands-on work in `cloud-projects/`.

---

## Planned / In Progress

- **s3-bucket-auditor/** — checks S3 buckets in an account and flags any that are publicly accessible when they shouldnt be
- **ec2-instance-lister/** — lists all running EC2 instances and flags anything unexpected (like an instance running that shouldnt be, or one missing expected tags)
- **iam-policy-checker/** — basic script to review IAM policies and flag ones that look overly permissive instead of following least-privilege

Each one will get its own folder with a README, the actual script, and notes on what it does and why — same format as the security scripts.

---

*This section is early too — these are the first scripts I'm planning to build once I'm further into the Cloud Practitioner material, not built yet as of right now.*

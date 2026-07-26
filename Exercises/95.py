import re

def redact_emails(log_content):
    email_pattern = (
        r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    )
    redacted_content = re.sub(email_pattern, "REDACTED", log_content
    )
    return redacted_content

# Esempio di utilizzo:
log_content = "User john.doe@example.com accessed the system on 2023-10-01.\nUser jane.smith@work.org logged in from IP 192.168.1.1."
print(redact_emails(log_content))



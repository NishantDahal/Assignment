def is_spam(email):
    spam_keywords = ["buy now", "limited time", "earn money", "free gift", "click here", "unsubscribe"]
    suspicious_sender_domains = ["example.com", "spammydomain.com"]
    
    email = email.lower()
    
    for keyword in spam_keywords:
        if keyword in email:
            return True
    
    for domain in suspicious_sender_domains:
        if f"@{domain}" in email:
            return True
    
    return False


example_email_text = "Congratulations! Congratulations!! Congratulations!!! You've won a free gift. Click here to claim it now."
if is_spam(example_email_text):
    print("This email is likely spam.")
else:
    print("This email is not spam.")

import imaplib
import email


username = "skupdoer@gmail.com"
password = "Test@1234"

gmailHost = 'imap.gmail.com'

mail = imaplib.IMAP4_SSL(gmailHost)
mail.login(username, password)
mail.select("INBOX")

_, selected_mails = mail.search(None, 'UNSEEN')

print("Total messages from customercare@goodearth.in:",
      len(selected_mails[0].split()))

for num in selected_mails[0].split():
    _, data = mail.fetch(num, '(RFC822)')
    _, bytes_data = data[0]
    email_message = email.message_from_bytes(bytes_data)
    print("\n===========================================")

    # access data

    messageSubject = email_message["subject"]

    if messageSubject == "Good Earth - Password Reset":
        print("Subject: ", email_message["subject"])
        print("To:", email_message["to"])
        print("From: ", email_message["from"])
        print("Date: ", email_message["date"])
        bodyMessage = email.message_from_string(str(email_message))
        print(bodyMessage)

        resetPasswordLink = str(bodyMessage).split('#fff;" href="')[1].split('">set a password')[0]

        print("Split String is:", resetPasswordLink)

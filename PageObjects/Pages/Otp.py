import time
import imaplib
import email
from PageObjects.Pages.LogInPopUp import *
from PageObjects.Utils.CommonMethods import *
from PageObjects.Utils.TestData import TestOtpData

OTP_TEXT = cssSelector('Otp text field')
OTP_MAIL = xpathLocator('otp mail field')
RESET_PASSWORD_MAIL = xpathLocator('reset password mail field')
SET_PASSWORD_BUTTON = xpathLocator('reset button')
ENTER_OTP = cssSelector('otp field')
VERIFY_OTP_BUTTON = xpathLocator('verify button')


def getOTP():
    mail = imaplib.IMAP4_SSL(TestOtpData.gmailHost)
    mail.login(TestOtpData.userName, TestOtpData.password)  # Creating the IMAP4 server connection
    mail.select("INBOX")   # Selecting the inbox folder inside the emails.

    _, selected_mails = mail.search(None, 'UNSEEN')  # Only reading the unseen mesaages.

    print("Total messages from customercare@goodearth.in:", len(selected_mails[0].split()))

    for num in selected_mails[0].split():
        _, data = mail.fetch(num, '(RFC822)')
        _, bytes_data = data[0]
        email_message = email.message_from_bytes(bytes_data)
        print("\n===========================================")

        # access data
        messageSubject = email_message["subject"]
        if messageSubject == "Almost There! Please verify your email address":
            print("Subject: ", email_message["subject"])
            print("To:", email_message["to"])
            print("From: ", email_message["from"])
            print("Date: ", email_message["date"])
            bodyMessage = email.message_from_string(str(email_message))
            # print(bodyMessage)
            otp = str(bodyMessage).split("letter-spacing:6px;")[1].split('</div>')[0].split("> ")[1]
            print("Split String is:", otp)
    # This will return the OTP after spliting the whole email.         
    return otp


def deleteAllMailsFromInbox():
    # account credentials
    username = "skupdoer@gmail.com"
    password = "Test@1234"

    folderToDeleteEmailsFrom = '"[Gmail]/All Mail"'
    trashFolder = '[Gmail]/Trash'

    # create IMAP4 with SSL
    imap = imaplib.IMAP4_SSL("imap.gmail.com", 993)
    # authenticate
    imap.login(username, password)

    # list all the mailboxes present
    print(imap.list())
    # SECTION 1: select the mailbox to delete emails from
    imap.select(folderToDeleteEmailsFrom)

    gmail_search = '"category:promotions NOT is: important"'
    typ, [msg_ids] = imap.search(None, 'X-GM-RAW', gmail_search)
    msg_count = len(msg_ids)
    print("Found message count: ", msg_count)
    if msg_count == 0:
        print("No new messages matching the criteria to be deleted.")
    else:
        if isinstance(msg_ids, bytes):
            # if it's a bytes type, decode to str
            msg_ids = msg_ids.decode()

        # SECTION 2: imap store command allows us to batch perform an operation
        # on a bunch of comma-separated msg ids
        msg_ids = ','.join(msg_ids.split(' '))
        print("Moving to Trash using X-GM_LABELS.")
        imap.store(msg_ids, '+X-GM-LABELS', '\\Trash')

        # SECTION 3: Once all the required emails have been sent to Trash,
        # permanently delete emails marked as deleted from the selected folder
        print("Emptying Trash and expunge...")
        imap.select(trashFolder)
        imap.store("1:*", '+FLAGS', '\\Deleted')  # Flag all Trash as Deleted
        imap.expunge()

    # SECTION 4: close the mailbox once the task is done
    print("Done. Closing connection & logging out.")
    imap.close()
    # logout
    imap.logout()


def clickOnOtpMail():
    time.sleep(10)
    refreshTab()
    refreshTab()
    refreshTab()
    time.sleep(2)
    # moveIntoView(OTP_MAIL)
    if isElementPresent(OTP_MAIL):
        clickOnTheButton(OTP_MAIL)
    else:
        raise Exception(str(OTP_MAIL) + "element is not located.")


def getOtp():
    if isElementPresent(ENTER_OTP):
        clickOnTheButton(ENTER_OTP)
        clearTheInputField(ENTER_OTP)
        enterTheInputValue(ENTER_OTP, getOTP())
        clickOnTheButton(VERIFY_OTP_BUTTON)
        print("Get OTP function working.")
    else:
        print("Locators" + str(ENTER_OTP) + "is not found.")


def clickOnResetPasswordMail(n):
    switchWindow(n)
    time.sleep(10)
    refreshTab()
    refreshTab()
    if isElementPresent(RESET_PASSWORD_MAIL):
        text = verifyForText(RESET_PASSWORD_MAIL)
        if text == "Good Earth - Password Reset":
            clickOnTheButton(RESET_PASSWORD_MAIL)
            clickOnSetPasswordButton()
    else:
        raise Exception(str(RESET_PASSWORD_MAIL) + "element is not located.")


def clickOnSetPasswordButton():
    if isElementPresent(SET_PASSWORD_BUTTON):
        clickOnTheButton(SET_PASSWORD_BUTTON)
    else:
        raise Exception(str(SET_PASSWORD_BUTTON) + "element is not located")

# TODO: send email alerts. setup gmail for alerts, query secrets

import smtplib
import time
from email.mime.text import MIMEText
from textwrap import wrap
from src import utils
from src import config

log = utils.get_module_logger(__name__)


def create_message(sender, to, subject, message_text):
    """Create a message for an email.

    Args:
    sender: Email address of the sender.
    to: Email address of the receiver.
    subject: The subject of the email message.
    message_text: The text of the email message.

    Returns:
    An object containing a base64url encoded email object.
    """
    message = MIMEText(message_text, 'plain')
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    return message


def send_message(sender, message, receivers):
    conf = config.Config()
    """
    Send an email message.
    """
    try:
        s = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)
        s.login(user=conf.SYSTEM_EMAIL_USER, password=conf.SYSTEM_EMAIL_PASSWD)
        s.sendmail(sender, receivers, message.as_string())
        s.quit()
        return message
    except Exception as error:
        log.warning('An error occurred: %s' % error)


def config_and_send_mail(recipient, subject, message_text, to_email_addr):
    sender = 'it@example.com'

    subject = f"{subject}"
    email_string = f"""Dear {recipient}:\n{message_text}\nSincerely,\nThe App"""

    string = wrap(email_string, width=70)
    # string = [x.encode('us-ascii') for x in string]
    # print(string)
    # msg = create_message(sender, to_email_addr, subject, string)
    print(string)
    # off for the demo.  Ideally, this would hit a queue and be consumed by an email service.
    # send_message(sender, msg, to_email_addr)
    time.sleep(5)
    log.info(f'email alert was sent to {to_email_addr}.')

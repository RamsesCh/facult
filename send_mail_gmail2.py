import httplib2
import os

from oauth2client import client, tools
from oauth2client.file import Storage
from oauth2client.client import AccessTokenRefreshError, OAuth2WebServerFlow
from apiclient import errors, discovery

import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import mimetypes
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase

scope = 'https://www.googleapis.com/auth/gmail.send'
client_id = '908800123283-3i5ira70uita6kd0m0tkufff8tk6cp0d.apps.googleusercontent.com'
client_secret = 'xIxL4lHSI_pW7s4czvWiKeT1'
flow = OAuth2WebServerFlow(client_id, client_secret, scope)

def get_credentials():
    storage = Storage('credentials.dat')
    credentials = credentials = storage.get()
    return credentials

def SendMessage(sender, to, subject, msgHtml, msgPlain):
    credentials = get_credentials()
    http = httplib2.Http()
    http = credentials.authorize(http)
    service = discovery.build('gmail', 'v1', http=http)

    message1 = CreateMessageHtml(sender, to, subject, msgHtml, msgPlain)
    result = SendMessageInternal(service, "me", message1)
    return result

def SendMessageInternal(service, user_id, message):
    try:
        message = (service.users().messages().send(userId=user_id, body=message).execute())
        print('Message Id: %s' % message['id'])
        return message
    except errors.HttpError as error:
        print('An error occurred: %s' % error)
        return "Error"
    return "OK"

def CreateMessageHtml(sender, to, subject, msgHtml, msgPlain):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = to
    msg.attach(MIMEText(msgPlain, 'plain'))
    msg.attach(MIMEText(msgHtml, 'html'))
    return {'raw': base64.urlsafe_b64encode(msg.as_string())}


def main():
    to = "jose.chavarria@gnp.com.mx"
    sender = "facultamientos@gnp.com.mx"
    subject = "subject"
    msgHtml = "Hi<br/>Html Email"
    msgPlain = "Hi\nPlain Email"
    SendMessage(sender, to, subject, msgHtml, msgPlain)


    
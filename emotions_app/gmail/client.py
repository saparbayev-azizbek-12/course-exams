import base64
from gmail.auth import get_gmail_service

service = get_gmail_service()

def get_label_id(label_name):
    labels = service.users().labels().list(userId='me').execute().get('labels', [])
    for label in labels:
        if label['name'].lower() == label_name.lower():
            return label['id']
    return None

def get_messages(max_results=10, label_id='INBOX'):
    res = service.users().messages().list(
        userId='me',
        labelIds=[label_id],
        maxResults=max_results
    ).execute()

    return res.get('messages', [])

def get_email_text(msg_id):
    msg = service.users().messages().get(
        userId='me',
        id=msg_id,
        format='full'
    ).execute()

    headers = msg['payload']['headers']
    subject = next((h['value'] for h in headers if h['name'] == 'Subject'), '')

    body = ""
    parts = msg['payload'].get('parts', [])

    for part in parts:
        if part['mimeType'] == 'text/plain':
            data = part['body'].get('data')
            if data:
                body = base64.urlsafe_b64decode(data).decode('utf-8')

    return subject + "\n" + body

def get_or_create_label(name):
    labels = service.users().labels().list(userId='me').execute()['labels']

    for lbl in labels:
        if lbl['name'] == name:
            return lbl['id']

    new_label = service.users().labels().create(
        userId='me',
        body={'name': name}
    ).execute()

    return new_label['id']

def move_to_label(msg_id, label_name):
    label_id = get_or_create_label(label_name)

    service.users().messages().modify(
        userId='me',
        id=msg_id,
        body={
            'addLabelIds': [label_id],
            'removeLabelIds': ['INBOX']
        }
    ).execute()

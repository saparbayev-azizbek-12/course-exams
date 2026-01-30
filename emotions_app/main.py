from model.predict import predict
from gmail.client import get_label_id, get_messages, get_email_text, move_to_label

input_label = 'Emotions/inbox'
label_id = get_label_id(input_label)
messages = get_messages(max_results=20, label_id=label_id)

for msg in messages:
    text = get_email_text(msg['id'])

    if len(text) < 20:
        continue

    label = "Emotions/" + predict(text)
    print(label)
    move_to_label(msg['id'], label)

    print(f"Moved email → {label}")

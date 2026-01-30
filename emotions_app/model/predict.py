import torch
from transformers import AutoTokenizer
from model.model_loader import model, device, itos


tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model.eval()

def predict(text):
    tokenize = tokenizer(
        text,
        truncation=True,
        padding="max_length",
        max_length=128,
        return_tensors="pt"
    )

    tokenize = {k: v.to(device) for k, v in tokenize.items()}
    
    with torch.no_grad():
        outputs = model(**tokenize)
        pred = torch.argmax(outputs.logits, dim=1)
    return itos[str(pred.item())]


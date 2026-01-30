import os
import json
import torch
from transformers import AutoModelForSequenceClassification

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILES_DIR = os.path.join(BASE_DIR, "files")

itos = None
with open(os.path.join(FILES_DIR, "label_map.json"), "r") as f:
    itos = json.load(f)

labels = list(itos.values())
device = "cuda" if torch.cuda.is_available() else "cpu"
model = AutoModelForSequenceClassification.from_pretrained(
    "bert-large-uncased",
    num_labels=len(labels),
)

model_path = os.path.join(FILES_DIR, "emotional_model.pt")
model.load_state_dict(torch.load(model_path, map_location=device))
model.to(device)
model.eval()

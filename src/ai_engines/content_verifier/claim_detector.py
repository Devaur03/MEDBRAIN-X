from transformers import AutoTokenizer, AutoModel

def load_biobert_model():
    path = "data/models/biobert-base"
    tokenizer = AutoTokenizer.from_pretrained(path)
    model = AutoModel.from_pretrained(path)
    return tokenizer, model

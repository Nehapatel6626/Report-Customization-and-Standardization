from datasets import Dataset
import pandas as pd
import os

# Load your annotated data (example structure)
def load_data(text_dir, labels_dir):
    samples = []
    for txt_file in os.listdir(text_dir):
        with open(os.path.join(text_dir, txt_file)) as f:
            text = f.read()
        with open(os.path.join(labels_dir, txt_file)) as f:  
            labels = f.read().splitlines()
        
        # Split into paragraphs with labels
        paragraphs = [p for p in text.split('\n\n') if p.strip()]
        for i, (para, label) in enumerate(zip(paragraphs, labels)):
            samples.append({
                "text": para,
                "label": label,
                "doc_id": txt_file,
                "para_id": i
            })
    
    return Dataset.from_pandas(pd.DataFrame(samples))

dataset = load_data("text_output", "labels")
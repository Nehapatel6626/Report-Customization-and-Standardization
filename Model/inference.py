from transformers import pipeline

class DocumentSegmenter:
    def __init__(self):
        self.classifier = pipeline(
            "text-classification", 
            model=model,
            tokenizer=tokenizer
        )
        self.crf = crf
    
    def segment_document(self, text):
        paragraphs = [p for p in text.split('\n\n') if p.strip()]
        
        # BERT predictions
        preds = self.classifier(paragraphs)
        
        # CRF sequence correction
        features = [para_to_features(p, pred["label"]) 
                   for p, pred in zip(paragraphs, preds)]
        final_labels = self.crf.predict([features])[0]
        
        # Structure output
        return [
            {"text": p, "label": l} 
            for p, l in zip(paragraphs, final_labels)
        ]
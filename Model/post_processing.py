from sklearn_crfsuite import CRF

# Convert predictions to CRF features
def para_to_features(para, pred_label):
    return {
        "bias": 1.0,
        "label": pred_label,
        "text_len": len(para),
        "starts_with_number": para[0].isdigit(),
        "contains_section_word": any(w in para.lower() for w in ["section", "chapter"])
    }

# Train CRF for sequence correction
crf = CRF(
    algorithm="lbfgs",
    c1=0.1,
    c2=0.1,
    max_iterations=100
)
crf.fit(train_features, train_labels)


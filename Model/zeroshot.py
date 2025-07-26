import os
from transformers import pipeline

# === CONFIG ===
input_folder = "paragraphs_txt"            # Your folder with .txt files
output_file = "file_level_classification_results.txt"
candidate_labels = [
    "Abstract", "Introduction", "Literature Review", 
    "Methodology", "Results", "Conclusion", "Future Work", "Title", "Tables and Figures", "References", "Appendix"
]

# === SETUP ===
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli", device=-1)

# === MAIN ===
with open(output_file, "w", encoding="utf-8") as out:
    for file_name in os.listdir(input_folder):
        if file_name.lower().endswith(".txt"):
            file_path = os.path.join(input_folder, file_name)
            with open(file_path, "r", encoding="utf-8") as f:
                paragraph = f.read().strip()
            
            if not paragraph:
                out.write(f"{file_name}\tEMPTY FILE\n")
                continue

            result = classifier(paragraph, candidate_labels, multi_label=False)
            top_label = result["labels"][0]
            score = result["scores"][0]
            out.write(f"{file_name}\t{top_label}\t{score:.2f}\n")
            print(f"✔️ {file_name}: {top_label} ({score:.2f})")

print(f"\n✅ Done. Results saved to: {output_file}")

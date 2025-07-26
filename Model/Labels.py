import os

def split_into_paragraphs(text):
    return [p.strip() for p in text.split('\n\n') if p.strip()]

def create_labels(text_dir, label_dir, placeholder='O'):
    os.makedirs(label_dir, exist_ok=True)

    for txt_file in os.listdir(text_dir):
        if not txt_file.endswith('.txt'):
            continue

        txt_path = os.path.join(text_dir, txt_file)
        label_path = os.path.join(label_dir, txt_file)

        with open(txt_path, 'r', encoding='utf-8') as f:
            text = f.read()

        paragraphs = split_into_paragraphs(text)
        # Create one label per paragraph
        labels = [placeholder] * len(paragraphs)

        with open(label_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(labels))

        print(f"✅ Created label file for: {txt_file} ({len(labels)} paragraphs)")

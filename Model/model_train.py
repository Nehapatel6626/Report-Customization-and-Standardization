from transformers import (
    AutoTokenizer, 
    AutoModelForSequenceClassification,
    TrainingArguments,
    Trainer
)

# Load pretrained model
model_name = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(
    model_name, 
    num_labels=len(label_names)
)

# Tokenize data
def tokenize(batch):
    return tokenizer(
        batch["text"], 
        padding=True, 
        truncation=True, 
        max_length=256
    )

dataset = dataset.map(tokenize, batched=True)

# Training setup
training_args = TrainingArguments(
    output_dir="results",
    per_device_train_batch_size=8,
    num_train_epochs=4,
    learning_rate=2e-5,
    evaluation_strategy="epoch"
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset["train"],
    eval_dataset=dataset["test"]
)

trainer.train()
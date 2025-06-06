from transformers import T5ForConditionalGeneration, T5Tokenizer
import random

# Load the model and tokenizer
model_name = "valhalla/t5-base-e2e-qg"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

def generate_mcqs_from_text(text):
    """
    Generates multiple choice questions (MCQs) with placeholder options.
    """
    prompt = "generate question: " + text.strip().replace("\n", " ")
    inputs = tokenizer.encode(prompt, return_tensors="pt", max_length=512, truncation=True)
    outputs = model.generate(inputs, max_length=512, num_return_sequences=1, early_stopping=True)

    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    questions = [q.strip() for q in result.split("?") if len(q.strip()) > 5]

    mcqs = []
    for idx, question in enumerate(questions):
        question_text = question + "?"
        correct = "Correct Option"
        options = [correct, "Option B", "Option C", "Option D"]
        random.shuffle(options)
        mcqs.append({
            "question": question_text,
            "options": options,
            "answer": correct
        })

    return {"quiz": mcqs}

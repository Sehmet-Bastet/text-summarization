import re
import nltk
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from transformers import T5Tokenizer, T5ForConditionalGeneration
import gradio as gr

nltk.download('punkt_tab')

# Функция очистки текста
def clean_text(text):
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


# Функция разделения текста на предложения
def split_into_sentences(text):
    return sent_tokenize(text)


# Extractive summarization
def extractive_summarize(text, top_n=3):
    cleaned_text = clean_text(text)
    sentences = split_into_sentences(cleaned_text)
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(sentences)
    similarity_matrix = cosine_similarity(tfidf_matrix)
    scores = np.sum(similarity_matrix, axis=1)
    top_indices = np.argsort(scores)[-top_n:]
    top_sentences = [sentences[i] for i in top_indices]
    return " ".join(top_sentences)


# Abstractive summarization
tokenizer = T5Tokenizer.from_pretrained('t5-small')
model = T5ForConditionalGeneration.from_pretrained('t5-small')

def generate_summary_t5(text, max_length=150):
    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=512, truncation=True)
    summary_ids = model.generate(inputs, max_length=max_length, min_length=30, length_penalty=2.0)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary


# Основная функция для генерации рефератов
def summarize(text):
    extractive_summary = extractive_summarize(text, top_n=3)
    abstractive_summary = generate_summary_t5(text)
    return extractive_summary, abstractive_summary


# Создание веб-интерфейса
iface = gr.Interface(
    fn=summarize,
    inputs="text",
    outputs=["text", "text"],
    title="Text Summarization"
)
iface.launch()
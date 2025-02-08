from rouge_score import rouge_scorer
import os

# Функция для вычисления метрик
def evaluate_metrics(reference_summary, generated_summary):
    """
    Вычисляет ROUGE-метрики для сравнения эталонного и сгенерированного рефератов.

    :param reference_summary: Эталонный реферат (строка).
    :param generated_summary: Сгенерированный реферат (строка).
    :return: Словарь с метриками ROUGE-1, ROUGE-2, ROUGE-L.
    """
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    scores = scorer.score(reference_summary, generated_summary)
    return scores


# Функция для сохранения метрик в файл
def save_metrics_to_file(scores, filename="metrics.txt"):
    """
    Сохраняет метрики в текстовый файл.

    :param scores: Словарь с метриками.
    :param filename: Имя файла для сохранения.
    """
    with open(filename, "w", encoding="utf-8") as f:
        for metric, values in scores.items():
            f.write(f"{metric}:\n")
            f.write(f"  Precision: {values.precision:.2f}\n")
            f.write(f"  Recall: {values.recall:.2f}\n")
            f.write(f"  F-measure: {values.fmeasure:.2f}\n")
            f.write("\n")


# Пример использования
if __name__ == "__main__":
    # Пример входных данных
    reference_summary = """Machine learning (ML) is a field of study in artificial intelligence concerned with the development and study of statistical algorithms that can learn from data and generalize to unseen data, and thus perform tasks without explicit instructions.[1] 
Within a subdiscipline in machine learning, advances in the field of deep learning have allowed neural networks, a class of statistical algorithms, to surpass many previous machine learning approaches in performance.[2] 
ML finds application in many fields, including natural language processing, computer vision, speech recognition, email filtering, agriculture, and medicine.[3][4] The application of ML to business problems is known as predictive analytics. 
Statistics and mathematical optimization (mathematical programming) methods comprise the foundations of machine learning. Data mining is a related field of study, focusing on exploratory data analysis (EDA) via unsupervised learning.[6][7]
From a theoretical viewpoint, probably approximately correct learning provides a framework for describing machine learning."""
    extractive_summary = "Data mining is a related field of study, focusing on exploratory data analysis (EDA) via unsupervised learning. [1] Within a subdiscipline in machine learning, advances in the field of deep learning have allowed neural networks, a class of statistical algorithms, to surpass many previous machine learning approaches in performance. Machine learning (ML) is a field of study in artificial intelligence concerned with the development and study of statistical algorithms that can learn from data and generalize to unseen data, and thus perform tasks without explicit instructions."
    abstractive_summary = "ML is a field of study in artificial intelligence concerned with the development and study of statistical algorithms that can learn from data and generalize to unseen data. ML finds application in many fields, including natural language processing, computer vision, speech recognition, email filtering, agriculture, and medicine."

    # Вычисление метрик
    extractive_scores = evaluate_metrics(reference_summary, extractive_summary)
    abstractive_scores = evaluate_metrics(reference_summary, abstractive_summary)

    print("Extractive Scores:", extractive_scores)
    print("Abstractive Scores:", abstractive_scores)

    # Создание пути к файлу в папке проекта
    project_directory = os.path.dirname(os.path.abspath(__file__))  # Путь к папке проекта
    extractive_metrics_path = os.path.join(project_directory, "extractive_metrics.txt")
    abstractive_metrics_path = os.path.join(project_directory, "abstractive_metrics.txt")

    # Сохранение метрик
    save_metrics_to_file(extractive_scores, extractive_metrics_path)
    save_metrics_to_file(abstractive_scores, abstractive_metrics_path)

    print(f"Metrics saved to {extractive_metrics_path} and {abstractive_metrics_path}")
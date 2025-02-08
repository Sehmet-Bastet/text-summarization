from rouge_score import rouge_scorer


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
    with open(filename, "w") as f:
        for metric, values in scores.items():
            f.write(f"{metric}:\n")
            f.write(f"  Precision: {values.precision:.2f}\n")
            f.write(f"  Recall: {values.recall:.2f}\n")
            f.write(f"  F-measure: {values.fmeasure:.2f}\n")
            f.write("\n")
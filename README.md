```markdown
# Text Summarization Project

This project implements both extractive and abstractive text summarization techniques using Python. It includes:

- **Extractive Summarization:** Based on TF-IDF and cosine similarity.
- **Abstractive Summarization:** Using the T5 model.

## Features

- Extractive summary: Selects top-N sentences from the input text.
- Abstractive summary: Generates a concise summary using the T5 model.
- Web interface: Built with Gradio for easy interaction.
- Evaluation metrics: ROUGE scores (ROUGE-1, ROUGE-2, ROUGE-L) to assess the quality of summaries.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/text-summarization.git
   cd text-summarization
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Web Interface

To launch the Gradio web interface for generating summaries:

```bash
python app.py
```

Open the provided URL (e.g., `http://127.0.0.1:7860`) in your browser and enter a text to generate extractive and abstractive summaries.

### Evaluating Metrics

To evaluate the quality of summarization using ROUGE metrics, run the following command:

```bash
python run_metrics.py
```

This will calculate ROUGE scores for the example data and save the results to two files:
- `extractive_metrics.txt`: Metrics for extractive summarization.
- `abstractive_metrics.txt`: Metrics for abstractive summarization.

#### Custom Data

If you want to evaluate metrics for your own data:
1. Replace the example texts in `run_metrics.py` with your reference, extractive, and abstractive summaries.
2. Alternatively, modify `run_metrics.py` to accept input from files or command-line arguments.

## Examples

### Input
```plaintext
Although the earliest machine learning model was introduced in the 1950s when Arthur Samuel invented a program that calculated the winning chance in checkers for each side, the history of machine learning roots back to decades of human desire and effort to study human cognitive processes.
```

### Extractive Output
```plaintext
[12] In 1949, Canadian psychologist Donald Hebb published the book The Organization of Behavior, in which he introduced a theoretical neural structure formed by certain interactions among nerve cells...
```

### Abstractive Output
```plaintext
The history of machine learning roots back to decades of human desire and effort to study human cognitive processes...
```

## Notes

- The `venv/` folder is excluded from the repository via `.gitignore`. To set up a virtual environment, run:
  ```bash
  python -m venv venv
  venv\Scripts\activate  # On Windows
  source venv/bin/activate  # On macOS/Linux
  ```
- Temporary metric files (`extractive_metrics.txt` and `abstractive_metrics.txt`) are also excluded via `.gitignore`.

## License

This project is open-source and available under the [MIT License](LICENSE).
```
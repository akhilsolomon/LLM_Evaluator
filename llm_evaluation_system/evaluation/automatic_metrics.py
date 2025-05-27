# evaluation/automatic_metrics.py

from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from rouge import Rouge

def compute_bleu(reference, hypothesis):
    reference = [reference.split()]
    hypothesis = hypothesis.split()
    smoothie = SmoothingFunction().method4
    return sentence_bleu(reference, hypothesis, smoothing_function=smoothie)

def compute_rouge(reference, hypothesis):
    rouge = Rouge()
    try:
        scores = rouge.get_scores(hypothesis, reference)
        return scores[0]['rouge-l']['f']  # returning ROUGE-L F1 score
    except ValueError:
        return 0.0

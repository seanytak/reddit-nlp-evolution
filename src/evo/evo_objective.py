import numpy as np

def objective(member_text: str, original_text: str, nlp, x=2, y=2/3, alpha=1, beta=1):
    """
    """
    # nlp = spacy.load('en_core_web_sm')
    # member_text = set(member_text.split(' ')
    # original_text = original_text.split(' ')
    
    # num_diff = sum([1 if a != b else 0 for a, b in zip(member_text.split(' '), original_text.split(' '))])

    num_diff = len(set(member_text.split(' ')) - set(original_text.split(' ')))
    num_words = max(len(set(member_text.split(' '))), len(set(original_text.split(' '))))

    objective_one =  nlp(member_text).similarity(nlp(original_text))
    objective_two = (num_diff + 1) / num_words
    
    return alpha * objective_one**x + beta * objective_two**y


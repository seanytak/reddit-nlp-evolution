import spacy

def objective(member: str, original_text: str, nlp, x=2, y=2/3, alpha=1, beta=1):
    """
    """
    # nlp = spacy.load('en_core_web_sm')
    # member = set(member.split(' ')
    # original_text = original_text.split(' ')
    num_diff = len(set(member.split(' ')) - set(original_text.split(' ')))
    # num_diff = sum([1 if a != b else 0 for a, b in zip(member.split(' '), original_text.split(' '))])
    num_words = max(len(set(member.split(' '))), len(set(original_text.split(' '))))
    
    return alpha * nlp(member).similarity(nlp(original_text))**x + beta * ((num_diff + 1) / num_words)**y


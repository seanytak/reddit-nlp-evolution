import spacy

def objective(nlp, member: str, original_text: str, x=2, y=2/3, alpha=1, beta=1):
    """
    """
    # nlp = spacy.load('en_core_web_sm')
    num_diff = sum([1 if a != b else 0 for a, b in zip(member.split(' '), original_text.split(' '))])
    num_words = len(member.split(' '))
    
    return alpha * nlp(member).similarity(nlp(original_text))**x + beta * ((num_diff + 1) / num_words)**y


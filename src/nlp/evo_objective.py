import spacy

def objective(nlp, member: str, original_text: str):
    """
    """
    # nlp = spacy.load('en_core_web_sm')
    num_diff = sum([1 if a != b else 0 for a, b in zip(member.split(' '), original_text.split(' '))])
    num_words = len(member.split(' '))
    
    return nlp(member).similarity(nlp(original_text))**2 * ((num_diff + 1) / num_words)**(2/3)


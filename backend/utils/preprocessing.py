import re

def preprocess(text):

    text = str(text).lower()

    text = re.sub(
        r'[^a-zA-Z0-9 ]',
        ' ',
        text
    )

    text = " ".join(text.split())

    return text
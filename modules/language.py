from nltk.tokenize import word_tokenize
from nltk import pos_tag

class Language:
    def __init__(self, dictionary):
        self.pos_dictionary = dictionary

    def tokenize(self, text):
        tokens = word_tokenize(text)
        return tokens

    def pos_tagging(self, tokens):
        tagged_tokens = pos_tag(tokens)
        return tagged_tokens

    def interpret_input(self, text):
        tokens = self.tokenize(text)
        tagged_tokens = self.pos_tagging(tokens)

        action = None
        target = None

        for token, tag in tagged_tokens:
            if tag.startswith('VB') or tag.startswith('JJ'):
                action = token.upper()
            elif tag.startswith('NN'):
                target = token.upper()

        print("Action:", action)
        print("Target:", target)

        return action, target

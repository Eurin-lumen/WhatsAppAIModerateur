# ml_model.py
# Ceci est une implémentation simple, un modèle ML complet nécessitera plus de travail.
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

class SpamClassifier:
    def __init__(self):
        self.vectorizer = CountVectorizer()
        self.classifier = MultinomialNB()
    
    def train(self, messages, labels):
        vectors = self.vectorizer.fit_transform(messages)
        self.classifier.fit(vectors, labels)
    
    def predict(self, message):
        vector = self.vectorizer.transform([message])
        return self.classifier.predict(vector)

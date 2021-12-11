import random

def evaluate(image):
    return {
        'anger': random.random(),
        'disgust': random.random(),
        'fear': random.random(),
        'happiness': random.random(),
        'neutral': random.random(),
        'sadness': random.random(),
        'surprise': random.random()
        }

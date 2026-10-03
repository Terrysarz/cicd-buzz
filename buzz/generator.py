import random


def sample(lst):
    return random.choice(lst)


def generate_buzz():
    buzz_words = [
        "continuous", "agile", "DevOps",
        "cloud-native", "serverless",
    ]
    actions = ["integration", "deployment", "delivery", "monitoring"]
    objects = ["pipeline", "workflow", "platform", "infrastructure"]
    return " ".join([sample(buzz_words), sample(actions), sample(objects)])

# Create a function named create_challenge() that takes name, language, and steps arguments. Steps should be optional, so give it a default value of 1. Create a Challenge from the arguments. create_challenge should not return anything.

from models import Challenge

def create_challenge(name:str, language:str, steps=1):
    Challenge.create(name=name, language=language, steps=steps)
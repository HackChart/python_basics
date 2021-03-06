# Create a function named search_challenges that takes two arguments, name and language. Return all Challenges where the name field contains name argument and the language field is equal to the language argument. Use == for equality. You don't need boolean and or binary & for this, just put both conditions in your where().

from models import Challenge


def create_challenge(name, language, steps=1):
    Challenge.create(name=name,
                     language=language,
                     steps=steps)

            
def search_challenges(name:str, language:str):
    return  Challenge.select().where(Challenge.name.contains(name) and Challenge.language == language)
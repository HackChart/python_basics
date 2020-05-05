# Create a function named delete_challenge that takes a Challenge as an argument. Delete the specified Challenge. Your function shouldn't return anything.


def delete_challenge(challenge):
    challenge.delete_instance()
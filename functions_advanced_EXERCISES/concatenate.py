def concatenate(*args):
    text = ""
    for arg in args:
        text += arg
    return text



print(concatenate("Soft", "Uni", "Is", "Great", "!"))
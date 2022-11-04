import typer
import re

app = typer.Typer()

def escape_special_regex_characters(word: str) -> str:
    special_characters = [
        r'\.', 
        r'\+', 
        r'\*', 
        r'\?', 
        r'\^', 
        r'\$', 
        r'\(', 
        r'\)', 
        r'\[', 
        r'\]', 
        r'\{', 
        r'\}', 
        r'\|', 
        r'\\'
        ]
    for character in special_characters:
        word = re.sub(character, character, word) # magic
    return word

fs = [
    lambda word: word.lstrip(), 
    escape_special_regex_characters,
    lambda word: re.sub(r'\n', '', word), 
    lambda word: r"(^\s*" + word + r"\s*$)", 
]


@app.command()
def file(
    path: str,
):
    """
    Generate a regex by a file containg a list of words.
    Each line represents a possible word.
    """
    words = []
    with open(path, 'r') as infile:
        for line in infile:
            word = line
            if not re.search(r'^\s*$', word):
                for f in fs:
                    word = f(word)
                words.append(word)
    regex = "|".join(words)
    print(regex)
    return(regex)
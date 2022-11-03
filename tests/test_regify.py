from regex_words.regify import file
import re

def test_regify_file():
    test_file = "./tests/test_file.txt"
    regex = file(path=test_file)
    with open(test_file, "r") as infile:
        for line in infile:
            if not re.search(r'^\s*$', line):
                if not re.search(pattern=regex, string=line):
                    raise AssertionError(f"Word {line} not matched by regex.")    
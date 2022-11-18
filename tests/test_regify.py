from regex_words.regify import file, file_names
import re
import random
import string

def test_regify_file():
    test_file = "./tests/test_file.txt"
    regex = file(path=test_file)
    with open(test_file, "r") as infile:
        for line in infile:
            if not re.search(r'^\s*$', line):
                assert re.search(pattern=regex, string=line), f"Word {line} not matched by regex."

def test_regify_file_names():
    regex = file_names(extensions=["xqz", "abs"])

    negatives = [(''.join(random.choices("." + string.ascii_uppercase + string.digits, k=10)), False) for _ in range(100)]
    negatives += [("test.test", False), ("test.xq", False), ("test.a", False), ("test.bs", False), ("test.abss", False)]
    negatives += [("%!my-file.xqz", False), ("^^$!my-file.abs", False)]

    positives = [("test.xqz", True), ("test.abs", True)] 

    for test, result in negatives + positives:
        if result:
            assert re.search(pattern=regex, string=test), f"{test} matched falsly."
        if not result:
            assert not re.search(pattern=regex, string=test), f"{test} matched falsly."

def test_regify_file_names_str():
    regex_str = file_names(extensions="xqz,abs")
    regex_list = file_names(extensions=["xqz", "abs"])
    assert regex_str == regex_list, "Something went wrong while parsing input string."

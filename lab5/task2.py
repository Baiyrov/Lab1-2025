import re

pattern = r"ab{2,3}" # "*" means that b 0 or more
test_strings = ["abb", "abbb", "abbbb", "a", "abc"]

for i in test_strings:
    if re.fullmatch(pattern, i):
        print(f"Matched: {i}")
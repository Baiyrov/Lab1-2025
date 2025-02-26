'''
import re

def snake_to_camel(snake_str):
    words = snake_str.split("_")
    return "".join(word.capitalize() for word in words)

print(snake_to_camel("hello_world_example"))  # HelloWorldExample
'''
import re

snake_to_camel = ("hello_world_example")
result = re.sub(r"([a-z])(_)([a-z])" , r"\1\3", snake_to_camel)

print(result)  # HelloWorldExample
import re

if __name__ == "__main__":
    print(re.sub(r"\b(the\s+){2,}", r"\1", "If the the problem is textual, use the the re module."))
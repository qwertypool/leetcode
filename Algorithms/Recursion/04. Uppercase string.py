First uppercase letter in a string (Recursive)

# Recursive Solution
def upCase(string):
    if len(string) < 0:
        return -1
    return string[0] if string[0].isupper() else upCase(string[1:])

print(upCase("Deepa"))

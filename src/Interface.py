width = 50

def row(content):
    print(f"| {content}" + " "*(width-4-len(content)) +" |")

def border():
    print("-"*width)

def double_border():
    print("="*width)

def ask(question, options):
    return input(f"{question} ({'/'.join(options)}) > ")

def show(content):
    print(content)

def error(content):
    print(f"ERROR: {content}")
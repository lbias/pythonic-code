# Truthiness of an element, True or False


def print_truthiness(msg, exp):
    print(("TRUE" if exp else "FALSE") + " <-- " + msg)


print_truthiness("Testing True", True)
# the keyword 'False' is False
print_truthiness("Testing False", False)

# for sequences
seq = []
# an empty list is False
print_truthiness("Empty list", seq)
seq.append("The cat")
print_truthiness("1 item list", seq)

# for objects and numbers, zero is False, the others are True
print_truthiness("Zero", 0)
print_truthiness("Eleven", 11)
print_truthiness("-Eleven", -11)

# for None, that is the thing that represents pointing to noting, is False
# 'None' is not zero, but it's considered to be False
print_truthiness("For none", None)


# custom types
class AClass:
    def __init__(self):
        self.data = []

    def add(self, item):
        self.data.append(item)

    def __bool__(self):
        return True if self.data else False


a = AClass()
# empty is False
print_truthiness("Empty AClass", a)
a.add("Thing")
print_truthiness("nonempty AClass", a)

# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


# Using for loop
for item in my_gen():
    print(item)


def add():
    for index in range(-1, 20, 2):
        yield index

for i in add():
    print(i)



def rev_str(my_str):
    length = len(my_str)
    print(length)
    for i in range(length - 1,-1,-1):
        yield my_str[i]

# For loop to reverse the string
# Output:
# o
# l
# l
# e
# h
for char in rev_str("hello"):
     print(char)


def add(a, d):
    """
    index a * d   """
    return a * d
print(add.__doc__)


# Tuple
tups = ("Duanpen", "Ning", 12, 10, 1992)
tuples = (1, 2, 3, 4, 5)
mixs = tups + tuples
print(mixs)
print(tups[1], tups[-1])
print(tups[1:3])
print(tups[-3:-2])
for index in range(len(tups)):
    print("print tuple", index + 1, tups[index])
    if "Duanpen" in tups:
        print("Trakulram")


def rev_str(my_str):
    length = len(my_str)
    print(length)
    for i in range(length - 1,-1,-1):
        yield my_str[i]

# For loop to reverse the string
# Output:
# o
# l
# l
# e
# h
for char in rev_str("hello"):
     print(char)



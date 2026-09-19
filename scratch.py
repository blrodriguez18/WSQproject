# DO SOME SCRATCH CODING

min = lambda x: (-x[value], x)

[x.title() for x in list if x.isalpha()]

# wrong:
multipliers = [lambda x: i * x for i in range(3)]
print([m(2) for m in multipliers])  # Output: [4, 4, 4] (instead of [0, 2, 4])

# right:
multipliers = [lambda x, i=i: i * x for i in range(3)]
print([m(2) for m in multipliers])  # Output: [0, 2, 4]

# wrong:
def append_to(element, target_list=[]):
    target_list.append(element)
    return target_list

print(append_to(1))  # Output: [1]
print(append_to(2))  # Output: [1, 2]  <-- The '1' stayed behind!

# right:
def append_to(element, target_list=None):
    if target_list is None:
        target_list = []
    target_list.append(element)
    return target_list


for i, j in range(n):
    i = left
    
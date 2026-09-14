# DO SOME SCRATCH CODING

min = lambda x: (-x[value], x)

[x.title() for x in list if x.isalpha()]

# wrong:
multipliers = [lambda x: i * x for i in range(3)]
print([m(2) for m in multipliers])  # Output: [4, 4, 4] (instead of [0, 2, 4])

# right:
multipliers = [lambda x, i=i: i * x for i in range(3)]
print([m(2) for m in multipliers])  # Output: [0, 2, 4]
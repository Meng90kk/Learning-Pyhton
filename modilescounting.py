import itertools

# ordered locations
for i in itertools.permutations('ABC', 3):
    print(i)

print()
# choose 2 from 10 locations
for i, c in enumerate(itertools.combinations('ABCDEFGHIJ', 2)):
    print(f"Option {i+1} = {c}")

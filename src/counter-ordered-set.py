import collections

ordered_set = collections.Counter()
ordered_set.update("a")
ordered_set.update("b")
ordered_set.update("c")
ordered_set.update("a")

for e in ordered_set:
    print(e)

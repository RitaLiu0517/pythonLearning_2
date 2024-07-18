# iterables & iterator 迭代器

# iterate over
# iteration
# stateful

x = [1, 2, 3]
it = iter(x)  # it = x.__iter__()
next(it)  # it.__next__()
print(sum(it))
print(list(it))
from collections import Iterable
def flatten(item, ingore_types=(str, bytes)):
    for x in item:
        if isinstance(x, Iterable) and not isinstance(x, ingore_types):
            for y in flatten(x):
                yield y
        else:
            yield x

s = ["a,b", "3,4"]
r = [x for x in flatten([x.split(",") for x in s])]
print r

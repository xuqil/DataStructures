
def reverse(elements):
    elems = elements
    i, j = 0, len(elems) - 1
    while i < j:
        elems[i], elems[j] = elems[j], elems[i]
        i, j = i + 1, j - 1
    return elems


a = [1, 2, 3, 4, 5, 6, 7]
print(reverse(a))
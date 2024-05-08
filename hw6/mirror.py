def mirror(input):
    if isinstance(input, list):
        return list(map(mirror, input))[::-1]
    else:
        return input

# Test cases
test_cases = [
    [1, 2, [3, [4, 5], 6]],
    [1, [2, [3, [4, [5]]]]],
    [[1, 2], [3, 4], [5, [6, 7]]]
]

results = list(map(mirror, test_cases))
print(results)
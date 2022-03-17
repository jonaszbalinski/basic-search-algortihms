def matches_at_position(text, pattern, position):
    if position < 0 or position > (len(text) - len(pattern)):
        raise IndexError(f"Invalid value of the 3 argument (\"position\"), position: {position}")

    for i in range(0, len(pattern)):
        if text[i + position] != pattern[i]:
            return False
    return True


def naive_algorithm(text, pattern):
    for i in range(0, len(text) - len(pattern) + 1):
        if matches_at_position(text, pattern, i):
            print(f"Naive - found at position: {i}")


def sunday_algorithm(text, pattern):
    last_position = {}
    for i in range(0, len(pattern)):
        last_position[pattern[i]] = i

    i = 0
    while i <= (len(text) - len(pattern)):
        if matches_at_position(text, pattern, i):
            print(f"Sunday - found at position: {i}")
        i += len(pattern)
        if i < len(text):
            i -= last_position.get(text[i], -1)


def boyer_moore_algorithm(text, pattern):
    last_position = {}
    for i in range(0, len(pattern)):
        last_position[pattern[i]] = i

    m = len(pattern)
    n = len(text)

    i = 0
    while i <= (n - m):
        j = m - 1
        while (j > -1) and (pattern[j] == text[i + j]):
            j -= 1
        if j == -1:
            print(f"Boyer–Moore - found at position: {i}")
            i += 1
        else:
            i += max(1, j - last_position.get(text[i + j], -1))


if __name__ == '__main__':
    example_text = "Yabhisavdiuatsd&vyhasv#$dguavlsdtgqcwdc??wuidbhiuasgxc~iut,furaycvduiwboduqbhuyvbgiTC tf/*&7wdaOY"
    example_pattern = "bh"

    naive_algorithm(example_text, example_pattern)
    print("*" * 50)
    sunday_algorithm(example_text, example_pattern)
    print("*" * 50)
    boyer_moore_algorithm(example_text, example_pattern)

def matches_at_position(text, pattern, position):
    pattern_len = len(pattern)
    text_len = len(text)

    if position < 0 or position > (text_len - pattern_len):
        raise IndexError(f"Invalid value of the 3 argument (\"position\"), position: {position}")

    for i in range(0, pattern_len):
        if text[i + position] != pattern[i]:
            return False
    return True


def naive_algorithm(text, pattern):
    results = []
    for i in range(0, len(text) - len(pattern) + 1):
        if matches_at_position(text, pattern, i):
            results.append(i)

    return results


def sunday_algorithm(text, pattern):
    results = []
    pattern_len = len(pattern)
    text_len = len(text)

    last_position = {}
    for i in range(0, pattern_len):
        last_position[pattern[i]] = i

    i = 0
    while i <= (text_len - pattern_len):
        if matches_at_position(text, pattern, i):
            results.append(i)
        i += pattern_len
        if i < text_len:
            i -= last_position.get(text[i], -1)

    return results


def boyer_moore_algorithm(text, pattern):
    results = []
    pattern_len = len(pattern)
    text_len = len(text)

    last_position = {}
    for i in range(0, pattern_len):
        last_position[pattern[i]] = i

    i = 0
    while i <= (text_len - pattern_len):
        j = pattern_len - 1
        while (j > -1) and (pattern[j] == text[i + j]):
            j -= 1
        if j == -1:
            results.append(i)
            i += 1
        else:
            i += max(1, j - last_position.get(text[i + j], -1))

    return results


if __name__ == '__main__':
    example_text = "Yabhisavd iuatsd&vyhasv#$dguavlsdtgqcwdc??wuidbh iuasgxc~iut,furaycvduiwboduqbhuyvbgiTC_tf/*&7wdaOY"
    example_pattern = "bh"

    print(f"Naive algorithm: {naive_algorithm(example_text, example_pattern)}")
    print(f"Sunday algorithm: {sunday_algorithm(example_text, example_pattern)}")
    print(f"Boyer-Moore algorithm: {boyer_moore_algorithm(example_text, example_pattern)}")

def matches_at_position(text, pattern, position):
    if position < 0 or position > (len(text) - len(pattern)):
        raise IndexError("Invalid value of the 3 argument (\"position\"), position: ", str(position))

    for i in range(0, len(pattern)):
        if text[i + position] != pattern[i]:
            return False
    return True


def naive_algorithm(text, pattern):
    for i in range(0, len(text) - len(pattern) + 1):
        if matches_at_position(text, pattern, i):
            print("Naive - found at position: " + str(i))


def sunday_algorithm(text, pattern):
    last_position = {}
    for i in range(0, len(pattern)):
        last_position[pattern[i]] = i

    i = 0
    while i <= (len(text) - len(pattern)):
        if matches_at_position(text, pattern, i):
            print("Sunday - found at position: " + str(i))
        i += len(pattern)
        if i < len(text):
            i -= last_position.get(text[i], -1)


if __name__ == '__main__':
    example_text = "abhisavdiuatsdvyhasvdguavlsdtgqcwdcwuidbhiuasgxciutfuraycvduiwboduqbhuyvbgiTC tfwdaOY"
    example_pattern = "Y"

    naive_algorithm(example_text, example_pattern)
    sunday_algorithm(example_text, example_pattern)

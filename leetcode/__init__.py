def generate_patterns(word):
    for i in range(len(word)):
        yield word[:i] + "*" + word[i + 1:]


def find_ladders(begin, end, words):
    if not begin or not end or not (end in words):
        return 0

    # Get all the patterns
    patterns = {}
    for word in words:
        for pattern in generate_patterns(word):
            if not (pattern in patterns):
                patterns[pattern] = []
            patterns[pattern].append(word)

    # Keep track of visited word`
    visited = {begin}
    queue = [(begin, 1)]
    while queue:
        current_word, level = queue.pop()
        for pattern in generate_patterns(current_word):
            if pattern not in patterns:
                continue

            for word_relative in patterns[pattern]:
                if end == word_relative:
                    return level + 1
                elif word_relative not in visited:
                    visited.add(word_relative)
                    queue.append((word_relative, level + 1))


if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    print(find_ladders(beginWord, endWord, wordList))
    # print(my_ladder_length(beginWord, endWord, wordList))

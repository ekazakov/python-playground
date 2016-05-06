

def calc_distance(wordA, wordB, lenA, lenB):
    # print('lenA:', lenA, 'lenB:', lenB)

    if lenA == 0:
        return lenB

    if lenB == 0:
        return lenA

    if wordA[lenA - 1] == wordB[lenB - 1]:
        return calc_distance(wordA, wordB, lenA - 1, lenB - 1)

    return 1 + min(
        calc_distance(wordA, wordB, lenA - 1, lenB),
        calc_distance(wordA, wordB, lenA, lenB - 1),
        calc_distance(wordA, wordB, lenA - 1, lenB - 1)
    )


def calc_distance_2(wordA, wordB, lenA, lenB):
    cache = [[0 for x in range(lenB + 1)] for x in range(lenA + 1)]

    for i in range(lenA + 1):
        for j in range(lenB + 1):
            if i == 0:
                cache[i][j] = j
            elif j == 0:
                cache[i][j] = i
            elif wordA[i - 1] == wordB[j - 1]:
                cache[i][j] = cache[i - 1][j - 1]
            else:
                cache[i][j] = 1 + min(cache[i][j-1], cache[i-1][j], cache[i-1][j-1])

    return cache[lenA][lenB]


word_a = 'lrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmcoq'
word_b = 'hnwnkuewhsqmgbbuqcljjivswmdkqtbxixmvtrrbljptnsnfwzqfjmafadrrwsofsbcnuvqhffbsaqxwpqcaceh'
# print(calc_distance(word_a, word_b, 84, 87))

# word_a = 'sunday'
# word_b = 'saturday'
print(calc_distance_2(word_a, word_b, len(word_a), len(word_b)))

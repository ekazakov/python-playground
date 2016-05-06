alphabet = 'abcdefghijklmnopqrstuvwxyz'

def permutations(n, k):
    index = 0

    def _permutations(string, step=0):
        nonlocal index

        if step == k:
            print('%3d. %s' % (index, ''.join(string[:k])))
            index += 1

        for i in range(step, len(string)):
            string_copy = [char for char in string]

            string_copy[step], string_copy[i] = string_copy[i], string_copy[step]
            _permutations(string_copy, step + 1)

    return _permutations(alphabet[:n])
# permutations('abc')


permutations(4,4)

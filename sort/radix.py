def counting_sort(arr, key, count_size=10):
    size = len(arr)

    output = [0] * size
    count = [0] * count_size

    for i in range(size):
        count[key(arr[i])] += 1

    for i in range(1, count_size):
        count[i] += count[i - 1]

    i = size - 1

    while i >= 0:
        output[count[key(arr[i])] - 1] = arr[i]
        count[key(arr[i])] -= 1
        i -= 1

    for i in range(size):
        arr[i] = output[i]


def radix_sort(arr):
    max_item = max(arr)

    exp = 1
    while int(max_item / exp) > 0:
        print(arr)
        counting_sort(arr, key=lambda item: int(item / exp) % 10)

        exp *= 10

data = [170, 45, 75, 11, 12, 13, 90, 802, 24, 2, 66]

radix_sort(data)

print(data)
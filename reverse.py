
def reverse(string):
    if len(string) <= 1:
        return string[0]
    else:
        return string[-1] + reverse(string[0:-1])

print(reverse('abcdej'))
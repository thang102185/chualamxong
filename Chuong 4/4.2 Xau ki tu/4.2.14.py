import re

def sapxep(S):
    numbers = re.findall(r'\d+', S)

    numbers = sorted(map(int, numbers))

    result = []

    number_index = 0

    i = 0
    while i < len(S):
        if S[i].isdigit():
            result.append(str(numbers[number_index]))
            number_index += 1
            while i < len(S) and S[i].isdigit():
                i += 1
        else:
            result.append(S[i])
            i += 1

    return ''.join(result)


S = input().strip()

print(sapxep(S))

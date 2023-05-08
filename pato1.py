def removeDuplicates(s):
    chars = []
    prev = None

    for c in s:
        if prev != c:
            chars.append(c)
            prev = c

    return ''.join(chars)

n = int(input())
for _ in range(n):
    m = int(input())
    s = input()
    sr = removeDuplicates(s.replace(" ", "").upper())
    if sr == "MEOW":
        print("El multiverso es nuestro")
    else:
        print("El multiverso no es nuestro")

#https://leetcode.com/problems/reverse-vowels-of-a-string/
def reverse_only_vowels(string):
    t = ['a', 'e', 'i', 'o', 'u', "A", 'E', 'I', 'O', "U"]
    n = list(string)
    i = 0
    j = len(string) - 1
    while i < j:
        if n[i] in t and n[j] in t:
            temp = n[i]
            n[i] = n[j]
            n[j] = temp
            j -= 1
            i += 1
        if n[i] not in t:
            i += 1
        if n[j] not in t:
            j -= 1
    return "".join(n)


string = "hello"
print(reverse_only_vowels(string))

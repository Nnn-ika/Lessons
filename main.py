# Сложность O(N**2)
# def symbolCounter(s: str):
#     for i in range(len(s)):
#         print(s.count(s[i]), s[i])


# Сложность ?
# def symbolCounter(s: str):
#     for sym in set(s):
#         counter = 0
#         for i in s:
#             if sym == i:
#                 counter += 1
#         print(sym, counter)


# Сложность O(N)
# .get(index, accumulator)
def symbolCounter(s: str):
    syms_counter = {}
    for i in s:
        syms_counter[i] = syms_counter.get(i, 0) + 1
    return syms_counter


print(symbolCounter(input()))
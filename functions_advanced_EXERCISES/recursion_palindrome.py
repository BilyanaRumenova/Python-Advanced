# def palindrome(word, index=0, right_index=-1):
#     if index == len(word) // 2:
#         return f"{word} is a palindrome"
#     else:
#         if word[index] == word[right_index]:
#             return palindrome(word, index+1, right_index-1)
#         else:
#             return f"{word} is not a palindrome"

from collections import deque

def palindrome(word, index=0):
    current_word = deque(word)

    while current_word:
        if len(current_word) < 2:
            return f"{word} is a palindrome"

        first = current_word.popleft()
        last = current_word.pop()

        if first == last:
            palindrome(current_word)
        else:
            return f"{word} is not a palindrome"


print(palindrome("abcba", 0))
print(palindrome("peter", 0))


# You’ve been hired to help build a puzzle game that includes a secret code challenge.
# In one level, players must enter a magic word that is the same when read forwards and
# backwards — a palindrome — to unlock the next clue.
# Your job is to write a program that:
# Accepts a word (or sentence) from the player.
# Checks if it is a palindrome using string manipulation.

print("--Palindrome using string manipulation--")
word = input("Enter a word or sentence: ")
i = 0
j = len(word) -1

while i<j:
    if word[i] != word[j]:
        is_palindrome = False
    else:
        is_palindrome = True
    i += 1
    j -= 1

if is_palindrome:
    print("YES")
else:
    print("NO")
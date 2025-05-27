# You’ve been hired to help build a puzzle game that includes a secret code challenge.
# In one level, players must enter a magic word that is the same when read forwards and
# backwards — a palindrome — to unlock the next clue.
# Your job is to write a program that:
# Accepts a word (or sentence) from the player.
# Checks if it is a palindrome using string manipulation.


print("--Palindrome using string manipulation--")
word = input("Enter a word or sentence: ")
word = word.replace(" ", "")  # Removes spaces

print(word)
i = 0
j = len(word) - 1
is_palindrome = True

while i <= j:
    print(word[i])
    print(word[j])
    print("-------------------------")
    if word[i] != word[j]:
        is_palindrome = False
        break
    i += 1
    j -= 1

if is_palindrome:
    print("YES")
else:
    print("NO")

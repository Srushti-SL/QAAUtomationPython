# write a program that:
# Accepts a list of favorite movie titles.
# Uses a for loop to count how many times each movie was mentioned.
# Displays only the movie titles that were mentioned more than once.


def find_duplicates(movie_list):
    seen = set()
    duplicates = []  #create a list to store only duplicate titles
    for item in movie_list:
        if item in seen:
            duplicates.append(item)
        else:
            seen.add(item)
    return duplicates

movie_list = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQR", "GHI", "DEF", "MNO"]
duplicate_elements = find_duplicates(movie_list)
print(duplicate_elements)
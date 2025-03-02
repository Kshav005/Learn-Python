# We can use certain functions to enhance our programs
a = "<<<<Meow?????? There No Is Cat"

# 1. len() - returns the length of the string
print(len(a))

# 2. upper() - returns the string in upper case (REMEMBER IT DOESN'T CHANGE THE STRING, BUT INSTEAD IT RETURNS THE COPY OF THAT STRING)
print(a.upper())

# 3. lower() - returns the string in lower case 
print(a.lower())

# 4. rstrip() - deletes the unwanted characters from the end 
print(a.rstrip("?"))

# 5. lstrip() - deletes the unwanted characters from the start
print(a.lstrip("<"))

# 6. replace()- returns and replaces all the occuring words with another string you want
print(a.replace("ow", "Hi"))

# 7. split() - returns the string in a form of list 
print(a.split(" "))

# 8. capitalize() - returns the string where starting alphabet is capitalized and corrects the string if there are mistakenly added capital words
b = "once upon a time, therE Was no one found"
print(b.capitalize())

# 9. center() - centers the string (align), by giving number of spaces entered by user
print(b.center(50))

# 10. count() - counts and returns the number of occurence of a particular character in the string
print(a.count("?"))

# 11. endswith() - Checks if the strings ends with a certain word or character
print(a.endswith("t"))
print(a.endswith("?", 3, 10))   # Checks if there is '?' in the range from 3 to 10 index

# 12. find() - searches for the first occurence of a particular character and gives it index. 
print(a.find("?"))
print(a.find("23"))     # Gives '-1' if the character is not present in the string

# 13. index() - similiar to find() but throws error if the character is not present in the string
print(a.index("32"))

# 14. isalnum() - checks if the whole string contains only alphabets and numbers, not symbols
print(a.isalnum())

# 15. isalpha() - checks if the string has only alphabets
print(a.isalpha())

# 16. islower() - checks if the string is in lower case (every character)
print(a.islower())

# 17. isspace() - returns true if the strings contains spaces
print(a.isspace())

# 18. istitle() - returns true if the first alphabet of the string is capital
print(a.istitle())

# 19. isupper() - checks if the string is in upper case
print(a.upper())

# 20. startswith() - checks if the string starts with a certain word or character
print(a.startswith(">"))  

# 21. swapcase() - swaps the case of the string (lower to upper and vice versa)
print(b.swapcase())

# 22. title() - changes the every first character of word in sentence to capital
print(a.title())

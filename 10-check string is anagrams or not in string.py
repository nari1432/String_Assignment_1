#10.Write a python program to check string is anagrams or not in Python


str1 = "revr"
str2 = "rvre"
if sorted(str1) == sorted(str2):
    print("Anagrams")
else:
    print("Not Anagrams")
#2.Write a program to check String is Palindrome or not.


def isPalindrome(s):
    return s == s[::-1]
 

s = "Hannah"
a = isPalindrome(s)
 
if a:
    print("Yes")
else:
    print("No")
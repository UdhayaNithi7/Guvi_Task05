# Q-1 Calculate the total number vowels & number of individual vowel in the given String

string = "Guvi Geeks Network Private Limited"
count_of_vowels = 0     # it contains the number of vowels in  string

for i in string:
    if i in 'aeiouAEIOU':
        count_of_vowels = count_of_vowels + 1

print("Total count of vowels in string: ",count_of_vowels)

    # below varialbles denotes the number of individual vowels in the string
Count_A = 0
Count_E = 0
Count_I = 0
Count_O = 0
Count_U = 0

for char in string:
    if char in 'AEIOU':
        if char == A:
            Count_A = Count_A +1
        elif char == E:
             Count_E = Count_E +1
        elif char == I:
             Count_I = Count_I +1
        elif char == O:
             Count_O = Count_O +1
        elif char == U:
             Count_U = Count_U +1
print("Count_A: ",Count_A)
print("Count_E: ",Count_E)
print("Count_I: ",Count_I)
print("Count_O: ",Count_O)
print("Count_U: ",Count_U)


#Q-2  form pyramid using 1 to 20 numbers in for loop

def pyr(n):
    pyra = ""
    for i in range(1, n+1):
        pyra +=str(i)
        print(pyra)
s2 = int(input("enter the end limit: ")) 
pyr(s2)       



# Q-3 Takes the String & return it with removing the vowels
def remove_vowels(sentence):
    return_string =""   # stores the value which are not vowels
    for j in sentence:
        if j not in 'aeiouAEIOU':
            return_string = return_string + j
    if return_string:
        return return_string
s3 = input("Enter the s3: ")
return_value = remove_vowels(s3)
print("return_value: ",return_value)



# Q-4 Takes the string & return unique character of the string
def uni_char(string_4):
    uni_string = "" # contains the unique character in the string
    for i in string_4:
        if string_4.count(i) <= 1:
            uni_string =uni_string + i
    return uni_string

s4 = input("enter the strings: ")
unique_string = uni_char(s4)
if unique_string:
    print("unique_string:",unique_string)
else:
    print("there is no unique character in the string")


# Q-5 check given string is palindrome or not
def pallindrome(string_5):
    pali = string_5.replace(" ","").lower() #remove white spaces & make the letters into lower
    if pali == pali[::-1]:
        return "Given string is palindrome"
    else:
        return "Given string is not palindrome"

s5 =input("Enter the string_5: ")
pa = pallindrome(s5)
print(pa)


# # Q-6 find longest substring in given two strings

def longest_common_substring(str1, str2):
    longest = ""
    
    for i in range(len(str1)):
        for j in range(len(str2)):
            current = ""
            k = 0
            while i + k < len(str1) and j + k < len(str2) and str1[i + k] == str2[j + k]:
                current += str1[i + k]
                k += 1
            
            if len(current) > len(longest):
                longest = current
    
    return longest

str1 = input("Enter the str1: ")
str2 = input("Enter the str2: ")
result = longest_common_substring(str1, str2)
print("Longest common substring:", result)



# Q-7 find the most frequent character in string
def freq_char(string_7):

    rep_count = {}  # Dictionary to store character counts

    # Count the occurrences of each character in the string
    for char in string_7:
        if char in rep_count:
            rep_count[char] += 1
        else:
            rep_count[char] = 1

    # Find the maximum occurrence count
    max_count = max(rep_count.values())

    # Find the characters that have the maximum occurrence count
    most_repeated_chars = []
    for char, count in rep_count.items():
        if count == max_count:
            most_repeated_chars.append(char)
    return most_repeated_chars

s7 = input("enter the string_7: ")
print("Frequently appeared element: ", freq_char(s7))
        


# Q-8 Check given string is anagram are not
def anagram_two_string():
    s8_1 = input("Enter the string_81: ")
    s8_2 = input("enter the string_82: ")

    if sorted(s8_1) == sorted(s8_2):
        return "String is anagram"
    else:
        return "String is not anagram"
print("given string:", anagram_two_string())
    

# Q-9 find the number of words in the string
def No_word(word):
    word = s9.split()
    return len(word)
s9 = input("enter the s9: ")
print("No of Words:",No_word(s9))





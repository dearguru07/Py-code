# vowel = ['a', 'e', 'i', 'o', 'u']
# word = str(input('enter a str'))
# count = 0
# for character in word:
#     if character in vowel:
#         count += 1
# print(count)


# vowel = ['a', 'e', 'i', 'o', 'u']
# word = str(input('enter a str'))
# count = 0
# for character in word:
#     if character not in vowel:
#         count += 1
# print(count)


# max number finding-------------

# numberList = [15, 85, 35, 89, 125]

# maxNum = numberList[0]
# for num in numberList:
#     if maxNum < num:
#         maxNum = num
# print(maxNum)


# min number finding------------

# numberList = [15, 85, 35, 89, 125, 2]

# minNum = numberList[0]
# for num in numberList:
#     if minNum > num:
#         minNum = num
# print(minNum)


# # fing mid ele in list------------

# numList = [1, 2, 3, 4, 5]
# midElement = int((len(numList)/2)) 

# print(numList[midElement])


# # Anagrams or not-------------------

str1 = str(input('enter a str'))
str2 = str(input('enter a str'))

str1 = list(str1.upper())
str2 = list(str2.upper())
str1.sort(), str2.sort()

if(str1 == str2):
    print("True")
else:
    print("False")



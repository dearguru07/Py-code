vowel = ['a', 'e', 'i', 'o', 'u']
word = "programming"
count = 0
for character in word:
    if character in vowel:
        count += 1
print(count)


vowel = ['a', 'e', 'i', 'o', 'u']
word = "programming"
count = 0
for character in word:
    if character not in vowel:
        count += 1
print(count)


# max number finding-------------

numberList = [15, 85, 35, 89, 125]

maxNum = numberList[0]
for num in numberList:
    if maxNum < num:
        maxNum = num
print(maxNum)


# min number finding------------

numberList = [15, 85, 35, 89, 125, 2]

minNum = numberList[0]
for num in numberList:
    if minNum > num:
        minNum = num
print(minNum)

# fing mid ele in list------------

numList = [1, 2, 3, 4, 5]
midElement = int((len(numList)/2)) 

print(numList[midElement])

# Anagrams or not-------------------

str1 = "Listen"
str2 = "Silent"

str1 = list(str1.upper())
str2 = list(str2.upper())
str1.sort(), str2.sort()

if(str1 == str2):
    print("True")
else:
    print("False")

# pyramid partten-----------

floors = 3
h = 2*floors-1
for i in range(1, 2*floors, 2):
    print('{:^{}}'.format('*'*i, h))

numberList = [1, 10, 20, 30, 50]
newList = []

for index in range(len(numberList)):
    if index % 2 == 0:
        newList.append(numberList[index])
print(newList)

thisdict = {
}

for index, item in enumerate(numberList):
    if index % 2 == 0:
        newList.append(item)
print(newList)

#### Example 2

evenIndexDict = {
}

for index, number in enumerate(numberList):
    if index % 2 == 0:
        evenIndexDict[index] = number
print(evenIndexDict)

##### Example 3

# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

# loop 1...number


# givenNumber = int(input('Give me a number'))
givenNumber = 26

for i in range(1, int((givenNumber + 1) / 2) + 1):
    if givenNumber % i == 0:
        print(i)

print(givenNumber)

print('######')

my_list = [i for i in range(1, 10)]

print(my_list)

a = lambda x, y: x * y
print(a(7, 19))

print(numberList[0:: 2])

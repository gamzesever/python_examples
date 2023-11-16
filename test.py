import random

a = [1 , 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]
common = []

for i in a:
    for j in b:
        if i == j:
            common.append(i)
            print(common)
            print(dict.fromkeys(common))
print(list(dict.fromkeys(common)))
print(common)

asd = {}
asd['volvo'] = 'xc90'

print(list(asd.values()))

kelime='otto'
tersi=""
for i in kelime:
  tersi=i+tersi
  print(tersi)
if kelime==tersi:
  print("palindrome")
else:
  print("palindrome değil")

tersi=""
for i in range(len(kelime)-1,-1,-1):
    print(kelime[i], end=" ")
    tersi+=kelime[i]
    print()
if kelime == tersi:
    print("palindrome")
else:
    print("palindrome değil")
print(tersi)

print('#######')
kelime='kayak'
size = len(kelime)
palindrome = True
for i in range(int(size / 2)):
    print(kelime[i], kelime[size - i - 1])
    if kelime[i] != kelime[size - i - 1]:
        palindrome = False
        break
print("Palindrome:" + str(palindrome))



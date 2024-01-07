
#EXERCISE 1:
class absolute_computation:
    def __init__(self):
        pass

    def abs_dict(self):
        for i in abs.__dir__():
            print(i)

    def abs_calculation(self,a):
        return abs(a)

result=absolute_computation()

print("absolute value of -155 is: ", result.abs_calculation(-155))

print(result.abs_dict())


# EXECISE 2

class Student:
    school = 'Forward Thinking'
    address = '2626/Z Overlook Drive, COLUMBUS'
student1 = Student()
student2 = Student()
student1.student_id = "V12"
student1.email = "lelele@gmail.com"
student1.student_name = "Ernesto Mendez"
student2.student_id = "V12"
student2.marks_language = 85 #property
student2.marks_science = 93
student2.marks_math = 95
students = [student1, student2]


for student in students:
    print('\n')
    for attr in student.__dict__:
        print(f'{attr} -> {getattr(student, attr)}')
    

print(student.__dict__)
print(type(student.__dict__))

student.mahmut="mahmut"
print(student.__dict__)
student.__delattr__("mahmut")
print(student.__dict__)


# EXERCISE 3:

# Write a Python program to create two empty classes, Student and Marks. Now create some instances and check whether "
# "they are instances of the said classes or not. Also, check whether the said classes are subclasses of the built-in object "
# "class or not.)"""

class Student():
 pass
class Marks():
 pass
student1=Student()
mark1= Marks()

print(isinstance(student1, Student))
print(isinstance(mark1, Student))
print(isinstance(student1, Marks))
print(isinstance(mark1, Marks))

student1.name="ali"
student1.surname="özen"
mark1.math=95
mark1.science=80
mark1.social=85

for attr1 in mark1.__dict__:
 print("mark attr are:",attr1, getattr(mark1, attr1) )

for attr2 in student1.__dict__:
 print("student attr are:", attr2, getattr(student1, attr2))
 



# EXERCISE 4:
# Write a Python class to get all possible unique subsets from a set of distinct integers.
# Input : [4, 5, 6]

class Subsets:


    def __init__(self, givenArray):
        self.oneitemset = list()
        self.twoitemset = list()
        self.threeitemset = list()
        self.givenArray = givenArray

    def one_items(self):
        for i in range(len(self.givenArray)):
            self.oneitemset.append(self.givenArray[i])
        return self.oneitemset

    def two_items(self):
        for i in range(len(self.givenArray)-1):
            for j in range(i, len(self.givenArray)):
                if i==j:
                    pass
                else:
                    self.twoitemset.append((self.givenArray[i], self.givenArray[j]))
        return self.twoitemset

    def three_items(self):
        for i in range(len(self.givenArray)-2):
            for j in range(i,len(self.givenArray)-1):
                for k in range(j,len(self.givenArray)):
                    if i==j or i==k or j==k or i==j==k:
                        pass
                    else:
                        self.threeitemset.append((self.givenArray[i], self.givenArray[j],self.givenArray[k]))
        return self.threeitemset

sett=[3,4,5,6,7]

myClass = Subsets(sett)
a = myClass.one_items()
print(myClass.oneitemset)
print(a)





#shortcut

from itertools import combinations

class Subsets:

    def __init__(self, given_array):
        self.subsets = [list(combinations(given_array, r)) for r in range(0, len(given_array)+1)]

sett = [1,2,3,4,5,6,7,8,9,10]
myClass = Subsets(sett)
for i, subset in enumerate(myClass.subsets):
    print(f"{i}-item set:", subset)





#EXERCISE 5:
# Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.
#Note: There will be one solution for each input and do not use the same element twice.
#Input: numbers= [10,20,10,40,50,60,70], target=50
#Output: 2, 3

class FindPair:
    """
    this class find a pair of elements (indices of the two numbers)
    from a given array whose sum equals a specific target number.
    """

    def __init__(self, givenArray, target):
        """
        :param givenArray: given array by user
        :param target: given target number by user
        """
        self.givenArray= givenArray
        self.target=target
        self.grandTotal= {}
        self.sub_totals_max = {}
        self.sub_totals_min = {}
        self.sub_totals_equal = {}

    def sum_array_elements(self):
        """
        :return: all possible sums without using same elements twice.

        values of grand total indicates givenArray's index
        keys of grand total indicates sum of givenArray's elements
        """
        for index1, element1 in enumerate(self.givenArray):
            for index2, element2 in enumerate(self.givenArray):
                if index1 == index2:
                    pass
                else:
                    value= (index1,index2)
                    key= element1+element2
                    self.grandTotal[key]=value


    def pair_solution(self):

        """
        :return: find pairs from given array whose sum equals a target.
         if sum of pairs are not equal target, returns the pair which has the nearest upper value of target

        sub_totals_equal: if sum of pair == grandTotal items.
        sub_totals_min: if sum of pair > grandTotal items. find min value in this object because it gives nearest pair to target.
        sub_totals_max: if sum of pair < grandTotal items. find max value in this object because it gives nearest pair to target.
        k indicates keys of grandTotal dict
        v indicates values of grandTotal
        """

        self.sum_array_elements()
        for k, v in sorted(self.grandTotal.items()):
            if k == self.target:
                self.sub_totals_equal[k] = v
                return self.sub_totals_equal.items()
            elif k > self.target:
                self.sub_totals_min[k] = v
            elif k < self.target:
                self.sub_totals_max[k] = v


        if self.sub_totals_max != {}:
            return max(self.sub_totals_max.items())
        if self.sub_totals_min != {}:
            return min(self.sub_totals_min.items())


a= FindPair([1,2,4,7], 10)











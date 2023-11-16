import numpy as np

data = np.array([[1, 2, 3], [4, 5, 6]])

print(data[0])

# multiply array

print(data * 10)

print("dimension", data.ndim)

arr1 = np.zeros((3, 2, 4))
print(arr1)
arr2 = np.ones((3, 2, 4))
print(arr2)

# range in numpy

print(np.arange(10))

# we cannot do arithmatic calculation with python main list data. For example:
liste = [1, 2, 3, 4]
print(liste * 2)

# But we can do this easly with numpy arrays:

print(data * 2, data / 2, data + data, data - 1)

arr3 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
arr3[4] = 9999
print(arr3)

print(np.array([3, 2, 4]).dtype)

# nested arrays
d1 = np.array(([1, 2, 3], [4, 5, 6]))
d2 = np.array(([7, 8, 9], [10, 11, 12]))
print(d1, d2)

data2 = np.array((d1, d2))
print(data2)

print("0 ındex:", data2[0], "**********", "1. index:", data2[1])

print("0. index 1. item:", data2[0][1])

print("0. index 1. item 2. value:", data2[0][1][2])

print("slicing:", "data:", data2, data2[:1], "***", data2[1:], "***", data2[:1, :1], "***", data2[0:, 1:])
print("^^^^^^")
print(data2[1, :1], "selecting second row's first array")

data3 = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

arr2d = data3[1, :2]

print("arr2d:", arr2d)

data3[1, :2] = 0
print("data3", data3)

# Corresponding to arrays

names = np.array(["Bob", "Joe", "Will", "Bob", "Will", "Joe", "Joe"])

data4 = np.array([[4, 7], [0, 2], [-5, 6], [0, 0], [1, 2], [-12, -4], [3, 4]])

print(data4[names == "Bob"])

# we can use ~ ınstead of !=

print("print the data 4 except of Bob's index", data4[~(names == "Bob")])

given_condition = names == "Bob"  # return the bolean value for names if ıt is Bob = true if not False
given_condition2= ~(names=="Bob")
print(given_condition, given_condition2)

order_arr= np.zeros((8,4))
for i in range(len(order_arr)):
       order_arr[i]=i
print(order_arr)

print("order the array:", order_arr[[4,3,2,7]]) # first row 4. index, second row 3. index, third row 2. index, fourth row 7. ındex

print("order the array:", order_arr[[-4,-3,-2]])

# select the specific values (index) from array
select_array= np.arange(32).reshape((8,4))
print(select_array)
print ("select the values:", select_array[[1,3,5,6],[0,2,3,1]])

select_array[[1,3,5,6],[0,2,3,1]]=0 #equal this values zero
print("***",select_array)
print("this makes to select column order", select_array[[1, 5, 7, 2]][:, [0, 3, 1, 2]])
#here first [] is shows row's index and second [] shows columns


#TRANSPOSE

print(data4)
print("**************")
print("tranposing array", data4.T)

matrice_array = np.array([[1,2,3] , [1,1,1], [1,1,1]])
print(matrice_array * matrice_array.T) #this is not work. Because here every index multiply by other equvelent index


#To multiply matrices ".dot()" func is used.
print("inner matrix", np.dot(matrice_array, matrice_array.T))

#or @ can be used

print("@", matrice_array@ matrice_array.T)


swapping=np.array([[1,2,3],[4,5,6]])
print("swap", swapping.swapaxes(1,1)) #??


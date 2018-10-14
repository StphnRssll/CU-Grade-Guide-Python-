from random import randint


##importing teachers
import pickle
import os
##tsts if array is empty or not
if os.path.getsize("prof.pkl") > 0:
    with open("prof.pkl", "rb") as f:
        unpickler = pickle.Unpickler(f)
        # if file is not empty scores will be equal
        # to the value unpickled
        scores = unpickler.load()
        print("eeee")


with open("prof.pkl", "rb") as fp:
    teachers = pickle.load(fp)
print("hey")
##importing As
with open("percAArray.pkl", "rb") as fp:
    gradesA = pickle.load(fp)
print("we're moving")
##importing Bs
with open("percBArray.pkl", "rb") as fp:
    gradesB = pickle.load(fp)
print("moving more")
##importing Cs
with open("percCArray.pkl", "rb") as fp:
    gradesC = pickle.load(fp)
print("almost there")
##importing pass
with open("percPArray.pkl", "rb") as fp:
    gradepass= pickle.load(fp)
print("there")
"""teachers = []
for j in range (0, 10):
    teachers.append(randint(0, 100))

gradesA = []
for j in range (0, 10):
    gradesA.append(randint(0, 100))

gradesB = []
for j in range (0, 10):
    gradesB.append(randint(0, 100))

gradesAB = []
for j in range (0, 10):
    gradesAB.append(randint(0, 100))

gradesPass = []
for j in range (0, 10):
    gradesPass.append(randint(0, 100))"""

"""def insertionSort(arr, arr1):

    for i in range(1, len(arr)):

        key = arr[i]
        key1 = arr1[i]
        j = i-1
        while j >=0 and key > arr[j] :
                arr[j+1] = arr[j]
                arr1[j+1] = arr1[j]
                j -= 1
        arr[j+1] = key
        arr1[j+1] = key1
    return arr, arr1"""
def insertionSort1(arr, arr1, arr2, arr3, arr4):

    for i in range(1, len(arr)):

        key = arr[i]
        key1 = arr1[i]
        key2 = arr2[i]
        key3 = arr3[i]
        key4 = arr4[i]
        j = i-1
        while j >=0 and key > arr[j] :
                arr[j+1] = arr[j]
                arr1[j+1] = arr1[j]
                arr2[j+1] = arr2[j]
                arr3[j+1] = arr3[j]
                arr4[j+1] = arr4[j]
                j -= 1
                print("hi")
        arr[j+1] = key
        arr1[j+1] = key1
        arr2[j+1] = key2
        arr3[j+1] = key3
        arr4[j+1] = key4


    return arr, arr1, arr2, arr3, arr4

a = "Teachers:"
aa = "% of As:"
b = "% of Bs:"
c = "% of Cs:"
p = "% Pass:"
insertionSort1(gradesA, teachers, gradesB, gradesC, gradepass)
print("{:<15}".format(a), "{:<15}".format(aa), "{:<15}".format(b), "{:<15}".format(c), "{:<15}".format(p))
for i in range(0, len(gradesA)):
    print("{:<15}".format(teachers[i]), "{:<15}".format(gradesA[i]), "{:<15}".format(gradesB[i]), "{:<15}".format(gradesC[i]), gradesPass[i])
    print(i)
"""insertionSort(gradesA, teachers)
print("{:<15} % of As".format(a))
for i in range (0, len(gradesA)):
    print ("{:<15}".format(teachers[i]), gradesA[i])

print("\n{:<15} % of Bs".format(a))
insertionSort(gradesB, teachers)
for i in range (0, len(gradesB)):
    print ("{:<15}".format(teachers[i]), gradesB[i])

print("\n{:<15} % of Cs".format(a))
insertionSort(gradesAB, teachers)
for i in range (0, len(gradesAB)):
    print ("{:<15}".format(teachers[i]), gradesAB[i])"""

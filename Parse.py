import csv
import os
import pickle

deptArray = []
coursenumArray = []
honArray = []
profArray = []
numStudentsArray = []
percAArray = []
percBArray = []
percCArray = []
percDArray = []
percFArray = []
percWArray = []
percIArray = []
percSTARArray = []
percPArray = []
#profLastNameArray = []
#profFirstNameArray = []


with open ('data.csv', "r") as csv_file: #open and read the csv
    for index,line in enumerate(csv_file): #creates an array, index represents row number, line is made up of each word on the line
        string = line
        commacount = 0 #comma count variable: used to count commas (to account for inconsitoncies in the formating of the input)
        if (len(string) > 10): #accounts for blanks spaces in formatting
            for word in string: #loop
                for char in word: #loop
                    if (char == ','):
                        commacount += 1 #adds 1 to the counter every time a comma is encountered (per line)
            if(commacount < 15):
                dept = string.split(',')[0] #string.split takes the string (the entire line) and divides it into an array made of elements (in this case elements == words)
                coursenum = string.split(',')[1] #the ',' tells the split function where to split, and the [number in brackets] identifies a particular word in the line (element of the array)
                hon = string.split(',')[2]
                prof = string.split(',')[3]
                numStudents = string.split(',')[4]
                 percA = string.split(',')[5]
                percB = string.split(',')[6]
                percC = string.split(',')[7]
                percD = string.split(',')[8]
                percF = string.split(',')[9]
                percW = string.split(',')[10]
                percI = string.split(',')[11]
                percSTAR = string.split(',')[12]
                percP = string.split(',')[13]
            else:
                dept = string.split(',')[0]
                coursenum = string.split(',')[1]
                hon = string.split(',')[2]
                prof = (string.split(',')[4] +" "+ string.split(',')[3])
                numStudents = string.split(',')[5]
                percA = string.split(',')[6]
                percB = string.split(',')[7]
                percC = string.split(',')[8]
                percD = string.split(',')[9]
                percF = string.split(',')[10]
                percW = string.split(',')[11]
                percI = string.split(',')[12]
                percSTAR = string.split(',')[13]
                percP= string.split(',')[14]

            deptArray.append(dept) #the .append function makes a list and adds to it with every iteration. this section creates the arrays/lists of each field containing the names of all the depts, coursenums, etc
            coursenumArray.append(coursenum)
            honArray.append(hon)
            profArray.append(prof)
            numStudentsArray.append(numStudents)
            percAArray.append(percA)
            percBArray.append(percB)
            percCArray.append(percC)
            percDArray.append(percD)
            percFArray.append(percF)
            percWArray.append(percW)
            percIArray.append(percI)
            percSTARArray.append(percSTAR)
            percPArray.append(percP)


#create pickle file for each field
with open('deptArray.pkl','wb') as f:
    pickle.dump(deptArray,f)
with open('coursenumArray.pkl','wb') as f:
    pickle.dump(coursenumArray,f)
with open('honArray.pkl','wb') as f:
    pickle.dump(honArray,f)
with open('prof.pkl', 'wb') as f:
    pickle.dump(profArray,f)
with open('numStudentsArray.pkl','wb') as f:
    pickle.dump(numStudentsArray,f)
with open('percAArray.pkl','wb') as f:
    pickle.dump(percAArray,f)
with open('percBArray.pkl','wb') as f:
    pickle.dump(percBArray,f)
with open('percCArray.pkl','wb') as f:
    pickle.dump(percCArray,f)
with open('percDArray.pkl','wb') as f:
    pickle.dump(percDArray,f)
with open('percFArray.pkl','wb') as f:
    pickle.dump(percFArray,f)
with open('percWArray.pkl','wb') as f:
    pickle.dump(percWArray,f)
with open('percIArray.pkl','wb') as f:
    pickle.dump(percIArray,f)
with open('percSTARArray.pkl','wb') as f:
    pickle.dump(percSTARArray,f)
with open('percPArray.pkl','wb') as f:
    pickle.dump(percPArray,f)

#check that every field is equal in length
'''print(len(deptArray))
print(len(coursenumArray))
print(len(honArray))
print(len(profArray))
print(len(numStudentsArray))
print(len(percAArray))
print(len(percBArray))
print(len(percCArray))
print(len(percDArray))
print(len(percFArray))
print(len(percWArray))
print(len(percIArray))
print(len(percSTARArray))
print(len(percPArray))'''

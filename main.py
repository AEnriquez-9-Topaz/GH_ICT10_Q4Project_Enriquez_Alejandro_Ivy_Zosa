from pyscript import display, document
import numpy as np # np is just a common alias
import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)
import matplotlib.pyplot as plt

#Classmate list
class Classmate:
    def __init__(self, name, section, fav_sub):
        # attributes . . .
        self.name = name
        self.section = section
        self.fav_sub = fav_sub

    def introduce(self): # creating a method
        return f'Hi, I am {self.name} from {self.section}. My favorite subject is {self.fav_sub}'


# intantiating an object
classmate1 = Classmate('Ivy', 'Topaz', 'English')
classmate2 = Classmate('AJ', 'Topaz', 'Science')
classmate3 = Classmate('Harmony', 'Topaz', 'Social Studies')
classmate4 = Classmate('JR', 'Topaz', 'Math')
classmate5 = Classmate('Khloe', 'Topaz', 'Science')

Classmates = [classmate1, classmate2, classmate3, classmate4, classmate5]

def Listclassmates(e):
    document.getElementById('output1').innerHTML = ''
    document.getElementById('notification1').innerHTML = ''
    
    for i in Classmates:
        display(i.introduce(), target='output1')

def ClassmateInfo(e):
    document.getElementById('notification1').innerHTML = ''
    display(f'Your data has been added, please re-click the show list button.', target='notification1')
    
    document.getElementById('output1').innerHTML = ''
    username = document.getElementById('input1').value
    usersection = document.getElementById('input2').value
    userfavsub = document.getElementById('input3').value

    classmate6 = Classmate(username, usersection, userfavsub)

    Classmates.append(classmate6)


# Storage for absence data
absence_storage = [0] * 10

#Attendance record graph
def Graph(e):
    global absence_storage
    document.getElementById("output").innerHTML = ''
    
    absences = int(document.getElementById("absences").value)
    month = int(document.getElementById("month").value)

    # Saving the data
    absence_storage[month - 1] = absences

    months = list(range(1, 11))

    plt.figure(figsize=(8, 4))
    plt.bar(months, absence_storage, width=0.6)
    plt.title("Record of Absences")
    plt.xlabel("Month")
    plt.ylabel("Number of Absences")
    #Changing the tick label
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    
    #Displaying current figure
    display(plt.gcf(), target="output")

#For Highlights
img_visibility = {} 

#This code toggles images using python, using a togglable empty dictionary. 
def showimg(e):
    img_id = e.target.getAttribute('data-img')
    if img_id not in img_visibility:
        img_visibility[img_id] = False
    
    img_element = document.getElementById(img_id)
    
    if not img_visibility[img_id]:
        img_element.style.display = "block"
        img_visibility[img_id] = True
    else:
        img_element.style.display = "none"
        img_visibility[img_id] = False

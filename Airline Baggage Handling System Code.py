#Authors: Emmanuel Nimo, William Obese and Kwadwo Ntiamoah Hemeng
#Project: Airline Baggage Handling system
#Data collection
#Generate random ID
#Sorting
#Hastable for storage
#Lists

import random


class Flyer:
    def __init__(self, name, weight):
        self.name = name
        self.weight = []
        self.weight.append(weight)
        


#Accessor methods
    def getName(self):
        return self.name

    def getWeight(self):
        return self.food

    
#Mutator method

    def setName(self, newName):                    
        self.name = newName

    def setWeight(self, newFood):
        self.food = newFood



    def __str__(self):
        s = ""
        for i in self.food:
            s = s + i  + ' , '  
        return "Customer details: " + self.name + "\nItems: \n" + s + "\nAmount: " + str(self.amount)




class Passenger:                                                     
    def __init__(self, Name, Weight):
        self.Name = Name
        self.Weight = Weight
        self.NewList = [ ]

  #Accessor methods
        
    def getName(self):
        return self.Name

    def getWeight(self):
        return self.Weight


    #Mutator  methods
    def setName(self, newName):                    #Mutating name
        self.Name = newName

    def setWeight(self, newWeight):                #Mutating Weight
        self.Weight = newWeight

 


#other methods
    def addFlyer(self, name):       # A method for adding students
        return self.NewList.append(name)
    

    def removeFlyer(self, name):       #A method for dropping students
        self.NewList.remove(name)

    def countFlyer(self, name):      # Count the number of students
        return (len(self.NewList ))

    def ListFlyer(self, course):
        a = ' '
        for i in self.NewList:
            a += i + ' , '
        return a
        
   
    def Flyer(self):
        return '{0:20} {1:^15} '.format(self.Name, self.Weight)

##    
##class HashTable:
##    def __init__(self):
##        self.size = 1000
##        self.slots = [None] * self.size
##        self.data = [None] * self.size
##
##    def put(self,key,data):
##      hashvalue = self.hashfunction(key,len(self.slots))
##
##      if self.slots[hashvalue] == None:
##        self.slots[hashvalue] = key
##        self.data[hashvalue] = data
##      else:
##        if self.slots[hashvalue] == key:
##          self.data[hashvalue] = data  #replace
##        else:
##          nextslot = self.rehash(hashvalue,len(self.slots))
##          while self.slots[nextslot] != None and \
##                          self.slots[nextslot] != key:
##            nextslot = self.rehash(nextslot,len(self.slots))
##
##          if self.slots[nextslot] == None:
##            self.slots[nextslot]=key
##            self.data[nextslot]=data
##          else:
##            self.data[nextslot] = data #replace
##
##    def hashfunction(self,key,size):                 #Modified hashfunction
##        value = 0
##        if type(key)  is int:
##            value = key
##        else:
##            s = 0
##            for i in key:
##                s = s + ord(i)
##        return value%size
##        
##
##    def rehash(self,oldhash,size):
##        return (oldhash+1)%size
##
##    def get(self,key):
##      startslot = self.hashfunction(key,len(self.slots))
##
##      data = None
##      stop = False
##      found = False
##
##    def __getitem__(self,key):
##         return self.get(key)
##
##    def __setitem__(self,key,data):
##         self.put(key,data)
##
##
##def main():
##    x = HashTable()
##    b = int(GenerateID(2019))
##    k = 0
##    count = 0
##    while k<1000:                          #Generating the thousand IDs
##        if x[b] !=b:
##            x[b]=b
##            k +=1
##            b = int(GenerateID(2019))
##        else:
##            b = int(GenerateID(2019))
##            count = count +1
##    output = open("Storefile.txt", "w")
##    output.write(str(x.data))
##    output.close()
##    print("Check your stored file for the IDs")
##
##    
##    #print(x.slots)
##    print("Number of IDs generated: ", k)
##    print("Regenerated IDs: ", count)
##    #print(x.data)
##
##main()


def RandomID(Weight):  #Method for generating Students' IDs                                   
    x = random.randint(1, 500)
    return (('%03d' % x ) + str(Weight))

def CounterInfo():
    Name = input('Enter the your name: ')
    Weight = int(input('Enter the weight of luggage: '))
    x = RandomID(Weight)
    print(RandomID(Weight))
   

    
 


CounterInfo()




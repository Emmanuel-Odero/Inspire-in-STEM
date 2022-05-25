#A dictionary is collection of key value pair. key:value
#syntax: dictionary = {'key':'value'}
# names =['john', 'Mary']
colors= {'color':'red'}
vehicle= {'type':'toyota','plate_number':'KYZ45'}
# print(type(names)) #we use the type method to read the data type of a string
#Acessing values in a dictionary
# print(vehicle['type'])#You can acces the value of an element inside a dictionary using the key
#print vehicle type and the plate number
print(vehicle['type'],vehicle['plate_number'])
#Dictionary Person
person = {
    'name':'Joan',
    'gender':'Female',
    'Phone_number':'997765',
    'location':'Dagoretti'
    }
person['age']='21'
#print(type(person))
#print(person)
#looping over dictionaties
for key, value in person.items():
    print(f"{key}:{value}")
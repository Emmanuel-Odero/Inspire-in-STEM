#Learning about lists
motorcycle_owner = "Mojo Jojo"
plate_number = ['H1234', 'Y1234', 'S1234']
motorcycle = ['honda', 'yamaha','suzuki']
#accessing list items using index
#print(motorcycle)
# motorcycle[1]= "Bugatti"#changing element in a list
#print("I love "+str(motorcycle[1]))
#adding element in a List
#motorcycle.append('Bugatti')#adding Item into a list append()
#task --- print the motorcycle and their plate number
#deleting an Item from a list --del
# del motorcycle[2] #deleting an item from a list
# popped_motorcycle = motorcycle.pop()
# print(popped_motorcycle)
#task print a statement: 
#My name is Mojo Jojo and I own a motorcycle plate number
# p_statement =(f"My name is {motorcycle_owner} and I own a {motorcycle[0]} plate number {plate_number[0]}")
# removing an Item from a list
motorcycle.remove('suzuki')
print(motorcycle)
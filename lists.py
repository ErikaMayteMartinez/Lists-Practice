#first list.
names = ['Mark', 'Dylan', 'Jessica', 'Sprinkles']
print(names)

#Creating a sentance using the above list.
message = f"My old roommates were {names[1].title()} and {names[3].title()}"
print(message)

#creating a guestlist- The below is an alternative for making a list; just remove the # signs at the begining
#section = []
#section.append('Jessica')
#section.append('Sprinkles')
#section.append('Ray')
#section.append('BJ')
#section.append('Naomi')
#section.append('Nathan')
section = ['Jessica', 'Sprinkles', 'Ray', 'BJ', 'Naomi', 'Nathan']

#Adding and removing someone from the list
#Adding-
section.insert(4, 'Nick')
#Removing
del section[5]

#Add in 3 more guests
section.insert(0, 'Shaggy')
section.insert(4, 'Arbel')
section.append('Jessie')

#Remove guests until you have just 1 left
print(section)

print(f"Sorry {section.pop(0)}, we have too many people")
print(section)
print(f"Sorry {section.pop(1)}, we have too many people")
print(section)
print(f"Sorry {section.pop(2)}, we have too many people")
print(section)
print(f"Sorry {section.pop(3)}, we have too many people")
print(section)
print(f"Sorry {section.pop(1)}, we have too many people")
print(section)
print(f"Sorry {section.pop(-2)}, we have too many people")
print(section)
print(f"Sorry {section.pop(-1)}, we have too many people")
print(section)
#reconfirm the smaller guest list
print(f"Hey {section[0]}, can't wait to see you for dinner!")
print(f"Hey {section[1]}, can't wait to see you for dinner!")

print(section)

#length of a list
print(len(section))

#remove the last names left, so you have an 'empty' list
del section[-1]
del section[0]
print(section)



#organizing and sorting lists
places = ['France', 'UK', 'Peru', 'Mexico', 'Iceland', 'Japan', 'Bali']
print(places)
print(sorted(places))
print(places)
places.reverse()
print(places)
places.reverse()
print(sorted(places))

print(len(places))


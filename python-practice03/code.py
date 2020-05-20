# --------------
class_1=['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2=['Hilary Mason','Carla Gentry','Corinna Cortes']
new_class=class_1+class_2
print(new_class)
new_class.append('Peter Warden')
new_class.remove('Carla Gentry')
print(new_class)
courses={'math':65,'english':70,'history':80,'french':70,'science':60}
values=courses.values()
total=sum(values)
percentage=(total/500)*100
print(percentage)
mathematics={'Geoffrey Hinton':78,'Andrew Ng':95,'Sebastian Raschka':65,'Yoshua Benjio':50,'Hilary Mason':70,'Corinna Cortes':66,'Peter Warden':75}
topper=max(mathematics,key=mathematics.get)
print(topper)
name=topper.split(' ')
first_name=name[0]
last_name=name[1]
s=" "
full_n=last_name+s
full_name=full_n+first_name
certificate_name=full_name.upper()
print(certificate_name)



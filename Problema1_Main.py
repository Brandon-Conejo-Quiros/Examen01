# -----------------------------------
# declaring local arrayList
# -----------------------------------
vec1 = [5, 1, 7, 4, 9]
vec2 = [6, 8, 2, 5, 4, 3, 1]
vecIdeal = [6,8,2,9,3]
# -----------------------------------
# Declaring a joins functions
# -----------------------------------
def Join():
 salida = []
 for act in vec1:
   control = act in vec2
 if control:
   salida.append(act)
 return salida


def FullJoin():
 salida2 = vec1
 for act in vec2:
   control = act in salida2
 if not control:
   salida2.append(act)
 return salida2




#Basically checks the list of banned numbers (Those in vec 1)
#And then checks the output list
#If it finds any match, it anihilates it

#Where one side equals null
def RightJoin():
 output = vec2
 banned = vec1
 for act in output:
  for act in output:
   if act in banned:
    output.remove(act)
 return output


#Utter dissapointment
#Does basically the same as the last, but the remaining number/s manually

def Outer():
 output = vec2
 banned = vec1
 lista = vec1 + vec2
 for act in output:
  for act in output:

   control1 = act in vec1 and act in vec2
   if control1:
    output.remove(act)

 output.append(9)

 return output




# -----------------------------------
# Executing joins functions
# -----------------------------------
print("Join es: ", Join())
print("''")
print("Full Join es: ", FullJoin())
print()
print("El Right Join where a.key is null es: ", RightJoin())
print("Lo que no queremos es: [5, 1, 7, 4, 9]")
print()
print("Full Outer es:", Outer())
print("Lo que queremos es: ", vecIdeal)
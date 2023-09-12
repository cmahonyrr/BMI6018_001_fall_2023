# Problem 1: Lists, Sets and Coersion

##1.a Create a list of integers no fewer than 10 items from 0 to 9.
one_a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(one_a)
##1.b Add 3 to the 5th indexed element
one_b = one_a.copy()
one_b[5] = one_b[5] + 3
print(one_b)
##1.c Coerce all elements in the list to floats using list comprehension
one_c = [float(i) for i in one_b]
print(one_c)
##1.d Coerce the list to a set
one_d = set(one_c)
print(one_d)
##1.e Using a method, append int 10 to the set
one_e = one_d.copy()
one_e.add(10)
print(one_e)
##1.f Using a method, pop an item from the set
one_f = one_e.pop()
print(one_f)
print(one_e)
##1.g Using a length counting function, count the number of items in the set
one_g = len(one_e)
print(one_g)
##1.h Check if the number of items in the set is the same as the number of items in the list (I use last list c)
one_h = len(one_e) == len(one_c)
print(one_h)
##1.i Coerce the set to a list and use the "+" operator combine the list to the list from 1.a
one_i = list(one_e) + one_a
print(one_i)
##1.j Coerce 1.i to a set
one_j = set(one_i)
print(one_j)
##1.k Count the number of elements in the 1.j
one_k = len(one_j)
print(one_k)

# Problem 2: Dictionary woes

##2.a Combine the three sample dictionaries (given below) into a nested dictionary (nested in programming means joined), named two_a, ensure the key names are the same as the dictionary names.
two_patient_dictionary_kinoko = {
  "name" : "Kinoko",
  "year" : 2021
}
two_patient_dictionary_dango = {
  "name" : "Dango",
  "year" : 2019
}
two_patient_dictionary_mochi  = {
  "name" : "Mochi",
  "year" : 2020
}

two_a = {
    "kinoko": two_patient_dictionary_kinoko,
    "dango": two_patient_dictionary_dango,
    "mochi": two_patient_dictionary_mochi
}
print(two_a)
##2.b Using keys, retrieve the Dango's name from 2.a
two_b = two_a["dango"]["name"]
print(two_b)
##2.c Using keys, update the value of Mochi's year to 2018. This should not be a variable and should simply update 2.a.
two_c = two_a.copy()
two_c["mochi"]["year"] = 2018
print(two_c)
##2.d Manually create a dictionary that has a single level and contains each patient as the key and the year as the value. Set Mochi's year to 2019.'
two_d = {
    "Kinoko": 2021,
    "Dango": 2019,
    "Mochi": 2019
}
print(two_d)
##2.e Coerce the keys of 2.d into a list
two_e = list(two_d.keys())
print(two_e)
##2.f Coerce the values of 2.d into a list
two_f = list(two_d.values())
print(two_f)
##2.g Use the zip function to combine 2.e and 2.f into a dictionary again
two_g = dict(zip(two_e, two_f))
print(two_g)

#Problem 3: Set combinations

#Given the predefined sets below and using set methods
three_setA = {1,2,3,4,5}
three_setB = {2,3,4,5,6}
three_setC = {3,5,7,9}
three_setD = {2,4,6,8}
three_setE = {1,2,3,4}
##3.a Is set E a subset of set A
three_a = three_setE.issubset(three_setA)
print(three_a)
##3.b Is set E a strict subset of set A
three_b = three_setE.issubset(three_setA) and three_setE != three_setA
print(three_b)
##3.c Create a set that is the intersection of set A and set B
three_c = three_setA.intersection(three_setB)
print(three_c)
##3.d Create a set that is the union of sets C, D and E
three_d = three_setC.union(three_setD, three_setE)
print(three_d)
##3.e add 9 to the set
three_e = three_d.copy()
three_e.add(9)
print(three_e)
##3.f Using == compare this set to the list in one_a
three_f = three_e == one_a
print(three_f)
##3.g Explain why they are not the same. What would you need to change if you wanted this to be True?
print("They are not the same because sets and lists are different data structures in Python. Even if they contain the same elements (which is not the case), they won't be considered equal. To make them equal, we need to convert one of them to the other's type")

#Problem 4: Changing variable types

#For each step you will modify a variable, then append the type of the variable
#to a list. Do not recreate the list variable, it should be a running list of 
#types.
##4.a Create a variable of type int with the value of 8
four_a = 8
print (four_a)
##4.b Create an empty list 
four_b = []
print(four_b)
##4.c Using type(), add the type of 4.a to this list
four_b.append(type(four_a))
print(four_b)
##4.d Add 0.39 to 4.c
four_b.append(0.39)
print(four_b)
##4.e append the type of 0.39 to the list
four_b.append(type(0.39))
print(four_b)
##4.f exponentiate to the -10, ie: 4.d^-10,(hint: there might be an artihmetic operator to do so) round it to no decimal places, and append to list.
four_f = [round(x ** -10) if isinstance(x, (int, float)) else x for x in four_b]
four_b.append(four_f)
print(four_b)
##4.g append the type to the list
four_b.append(type(four_f))
print(four_b)

# Problem 5: More variable type changes

#Continue from where you left off in Problem 4.
##5.a Manually create a dictionary where the values are items in the list from where we left in problem 4, and the keys should be their index in the list. Print the dictionary.
five_a = {i: four_b[i] for i in range(len(four_b))}
print(five_a)
type(five_a)
##5.b Add 300 and coerce it into a string
five_b = five_a.copy()
five_b[len(five_b)]=str(300)
print(five_b)
##5.c append the type to the list
four_b.append(type(five_b))
print(four_b)
##5.d slice the string up to the 2nd element
five_d = five_b[max(five_b.keys())][:2]
print(five_d)
##5.e append the type to the list
four_b.append(type(five_d))
print(four_b)
##5.f use list comprehension to convert this into a new list of integers
five_f = [int(i) for i in four_b if (isinstance(i, (int, float)) or (isinstance(i, str) and i.replace('.', '', 1).isdigit()))]
print(five_f)
##5.g append the type to the list
four_b.append(type(five_f))
##5.h append the type of three_setA to the list
four_b.append(type(three_setA))

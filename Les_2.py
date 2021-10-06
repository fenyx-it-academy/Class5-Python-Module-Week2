

#LISTS
'''

a='ab cd'                              #string
b=('a','b','c','d')                  #tuple
c={'a','b','c','d'}                    #set
d={'a':1, 'b':2,'c':3,'d':4}           #dictionary

print(list(a))
print(list(b))
print(list(c))
print(list(d))

'''
'''
x=[1,2]

print(3*x)
print(x+x+x)

'''
'''
my_list=[0,3,12,8,2]

print(5 in my_list)
print(5 not in my_list)

'''
'''
n_list=["Hello",[1,2,3]]
print(n_list[0][2])

'''
'''
lst=["D","F","1","c",",",""," "]
lst.sort()
print(lst)
print(sorted(lst))
'''
'''
nums=[1,2,3]
vals=nums
del vals[1:2]
print(vals)
print(nums)

'''
'''

p_letters=[]

for letter in 'pycoders':
    p_letters.append(letter)
print(p_letters)

s=[[i for i in range(3)] for j in range(5)]

print(s)

'''
'''
number_list=[]

for x in range(20):
    if x%2==0:
        number_list.append(x)
print(number_list)

'''
'''
number_list=[x for x in range(29) if x%2==0]
print(number_list)

'''

#TUPLES

#SETS

#DICTIONARY

Dictionary={
    "cat" : "kat",
    "dog" : "hond",
    "horse": "paard"
}

for key in Dictionary.keys():

    print(key, "->", Dictionary[key])


Dictionary['lion']='leeuw'
Dictionary.update('liom'  'leeuw')

print(Dictionary)

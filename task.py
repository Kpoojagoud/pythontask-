student_marks = {'pooja' : 90 , 'shiva': 70, 'shekar':60}
print(student_marks.keys())
print(student_marks.values())
print(student_marks.items())
print(student_marks.get('pooja')) 

#========================================
# set 
a = {1,2,3,4} 
a.add(6) 
print(a)
a.remove(2) 
print(a)

#======================================= 
a = {1,2,3}
b = {5,3,7} 
print(a.union(b)) 
print(a.intersection(b))
print(a.difference(b)) 

#==============================================
#list 
a = [10,20,30]
a.append(60) 
a.insert(5,10) 
a.remove(20) 
print(a) 

#==================================== 
#tuple 
a = ('a','b','c')
print(a[0])

#==============================================
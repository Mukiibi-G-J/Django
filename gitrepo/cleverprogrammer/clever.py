# mutability
    # lists are a mutabel dictionaries
    # tuple is inmutable  can't be chaenge it str,int,floats
    
    # note:
         # a key in dictionaries has to be innmutable
from os import path


tu= ( 2,3,4,[5,6,7,8])
print(tu)
print(tu[3]) 
tu[3][1]=45
print(tu)  

# list comprehension  
names = ['joseph','sohife', 'jane', 'suzane']

l=[]
for i in names:
    l.append(i)
print(l)

# what ever u want in the list goes first is 
print([i for i in names])

l=[]
for i in names:
    l.append(i+'dumped me')
print(l)


print([i+'dumped me' for i in names])

movies_and_ratings={'insterelllar':56,
                    'Dark_night':3, 
                    '50 Shades darker':4, 
                    '50 shades':50 
}  

# NOTE
        # if you iterate through a dictionary you get only the keys
        #biut if u index it gives u the values
        
# for i in movies_and_ratings:
#     # print(i)
#     print(movies_and_ratings[i])  
                
l=[]
for movies in movies_and_ratings:
    if movies_and_ratings[movies]>5:
        l.append(movies)
print(l)

         
print([movies for movies in movies_and_ratings if movies_and_ratings[movies]>6])                    

  
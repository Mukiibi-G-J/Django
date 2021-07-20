list1=[1,2,3,4,5,6]
list2=['one','two','three','four','five','six']

zipped =list(zip(list1,list2))
print(zipped)

# unzippeding
unzipped = list(zip(*zipped))
print(unzipped)


for (l1,l2) in zip(list1,list2):
    print(l1)
    print(l2)
    
items = ['Apple','Banana','Orange',]
counts =[3,4,5]
prices = [88.9,89.0,65.4]
sentences=[]
for (item,count,price) in zip(items,counts,prices):
    sentence=f'I bought {count} {item} at {price}'
    sentences.append(sentence)
print(sentences)
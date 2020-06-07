listint = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
listchr = ['']*len(listint)
j=0
for i in listint:
    listchr[j]=chr(i)
    j+=1
print(''.join(listchr))

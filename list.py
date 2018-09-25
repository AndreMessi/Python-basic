#list itu mirip array
data=[1,4,9,16,26,36,49,64]
subdata=data[3]
subdata1=data[-5]
subdata2=data[3:6]
print(subdata)
print(subdata1)
print(subdata2)

#menambah list
data2=[100,200,300,400,500,600,700,800,900]
data2=data+data2
print(data2)

#merubah list
print(data)
data[4]=45
print(data)

#list dalam list
x=[data,data2]
y=x[0][4]
print(x)
print(y)
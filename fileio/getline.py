import linecache
data = []

for j in range(1,490/4+1):
 y=linecache.getlines('yes_f.wav')[j]
 z=y.split()
 for i in range(4):
  data.append(z[i])
  print(i,j,data[(j-1)*4+i])

j= j+1
y=linecache.getlines('yes_f.wav')[j]
z=y.split()
for i in range(2):
 data.append(z[i])
 print(i,j,data[(j-1)*4+i])

str1 = data[0]
str1s = str1.partition('[')
data[0]= str1s[2]

str2 = data[489]
str2s = str2.partition(']')
data[489]= str2s[0]

floatdata = []
for k in range(490):
 floatdata.append(float(data[k]))
 print(k,floatdata[k])



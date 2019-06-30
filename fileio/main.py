import struct

#a = [0x42,0x43,0x44,0x45,0x46,0x47]
a = [2,3,4,5,6,7]
with open('test.bin','ab') as f:
 for i in range(len(a)):
  print(a[i])
  s=struct.pack('f',a[i]) 
  print(i)
  print(s)
  f.write(s)
 f.close

with open('test.bin','r') as f:
 so = f.read()
 print(so)
 b = struct.unpack('f',so)
 print(b)
 f.close()

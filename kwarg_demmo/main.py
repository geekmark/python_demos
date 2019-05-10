#!/usr/bin/env python
def parrot(voltage, state='a stiff',action='voom',type='Norwegian Blue'):
    print("--this parrot wouldn't",action)
    print("if you put",voltage, "volts through it.")
    print("Lovely plumage, the",type)
    print("It's",state,"!")


#mark test 1
#mark test 2 
print('================================================')
parrot(1000)
print('================================================')
parrot(voltage=1000)
print('================================================')
parrot('a thousand', state='pushing up the daisies')
print('================================================')


# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 16:34:38 2024

@author: Administrator
"""

'''
MODE:
    r : only read (defaul'rt')
    r+ : read & write, overriding, without creating a new file
    rb : read binary
    rb+
    
    w : only write, opens a file & truncate its first , creates a new file
    w+ : write & read, ....
    wb
    wb+
    
    a: only append, always write in the end regardless of pointer, creates a new file
    a+:
    
'''

# A+
f = open('D:\\Learn Python\\file4.txt','a+', encoding = 'utf-8')
print(f,'\n')


# read when open
f.seek(0) # cần seek về 0 vì file when open, pointer ở cuối
r0 = f.read()
print('READ WHEN OPEN:\n',r0,'\n')


# no need seek as file pointer when write is always in the end
f.seek(0)
a = f.write('Hôm nay trời nắng đẹp,\n')

# read after first append
ps = f.seek(0)
r1 = f.read()
print('READ AFTER FIRST APPEND:\n',r1,'\n')


#
f.close()
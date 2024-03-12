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

# W+
f = open('D:\\Learn Python\\file3.txt','w+', encoding = 'utf-8')
print(f,'\n')

# read when open
r0 = f.read() # không đọc được gì vì lúc open đã bị xóa
print('READ FIRST WHEN OPEN:',r0,'\n')


# write
ps = f.seek(0)
w1 = f.write('TẠO MỚI FILE -----------------------')

# read after first writing
ps = f.seek(0)
r1 = f.read()
print('READ AFTER WRITE:\n',r1,'\n')



# overriding
ps = f.seek(0)
w2 = f.write('OVERRIDING ***')

# read after overriding
ps = f.seek(0)
r2 = f.read()
print('READ AFTER OVERRIDING:\n',r2,'\n')



# close
f.close()
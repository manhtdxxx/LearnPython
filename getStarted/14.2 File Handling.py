# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 12:07:01 2024

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
# R+
f = open('D:\\Learn Python\\file_2.txt','r+', encoding = 'utf-8')
print(f,'\n')

# read when open
r1 = f.read()
print('READ FIRST WHEN OPEN:\n',r1,'\n')



# overriding 1
f.seek(0)
w1 = f.write('Hôm này trời mưa to tầm tã\ntại sao phải ngồi trong nhà') # overriding từ vị trí con trỏ chuột

# read after overriding 1
f.seek(0)
r2 = f.read()
print('READ AFTER OVERRIDING 1:\n',r2,'\n')



# overiding 2
f.seek(0)
w2 = f.write('Vì em covid ghé thăm.') # overriding từ vị trí con trỏ chuột

# read after overriding 2
f.seek(0)
r3 = f.read()
print('READ AFTER OVERRIDING 2:\n',r3,'\n')



# CLOSE FILE
f.close()


#
print('CHECK ĐÓNG FILE:',f.closed)
print('CHECK MODE:',f.mode)
print('CHEK NAME:',f.name)



import os
# ĐỔI TÊN
#os.rename('D:\\Learn Python\\file2.txt','D:\\Learn Python\\file_2.txt')

# XÓA FILE
#os.remove('D:\\Learn Python\\file_2.txt')

# remove file if exists
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")

# TẠO THƯ MỤC (make directory)
#os.mkdir('hoc')

# GET CURRENT WORK DIRECTORY
print('GET CURRENT WORK DIRECTORY',os.getcwd())

# XÓA THƯ MỤC
#os.rmdir('hoc')


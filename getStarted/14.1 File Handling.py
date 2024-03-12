# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 10:35:16 2024

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

# MỞ FILE KHÔNG DẤU
f = open('D:\\Learn Python\\file.txt','r')
print(f)

r1 = f.read() # đọc từ vị trí con trỏ đến hết
print (r1,'\n')

pointer_tell = f.tell() # đã đọc hết nên file pointer ở cuối
print('Vị trí con trỏ file:',pointer_tell)

pointer_seek = f.seek(0) # adjust con trỏ về vị trí 0
print('Điều chỉnh con trỏ file:',pointer_seek)

pointer_tell = f.tell() 
print('Vị trí con trỏ file sau seek:',pointer_tell,'\n')

r2 = f.read(21)  # đọc từ vị trí con trỏ với giới hạn 22 kí tự
print(r2)

r3 = f.read(23) # đọc tiếp
print(r3,'\n')

f.close() # đóng file

print('----------------------------','\n')

# MỞ FILE CÓ DẤU
f = open('D:\\Learn Python\\file_unicode.txt','r',encoding = 'utf-8')
print(f)

r1 = f.read(22) 
print(r1)

pointer_tell = f.tell() 
print('Vị trí con trỏ file:',pointer_tell,'\n') # do có dấu

rline = f.readline() # nếu dòng trước chưa xong thì đọc nốt,
print(rline)         # xong rồi thì đọc dòng tiếp theo

rline = f.readline() # đọc dòng tiếp theo
print(rline,'\n')

pointer_seek = f.seek(0)
print('Điều chỉnh con trỏ file:',pointer_seek,'\n')

rlines = f.readlines()
print(rlines,'\n')

pointer_seek = f.seek(0)
print('Điều chỉnh con trỏ file:',pointer_seek,'\n')

for i in f.readlines():
    print(i)
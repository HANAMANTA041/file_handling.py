#Reading Character Data from text files:
f = open("PES_data.txt",'r')
data = f.read()
print(data)
f.close()

#ex:File Management
file_descriptors = []
for x in range(100000):
    file_descriptors.append(open('test.txt', 'w'))

"""Traceback (most recent call last):
  File "D:/pythoncodes/file_handl3.py", line 10, in <module>
OSError: [Errno 24] Too many open files: 'test.txt'"""
""" The above example is a 
case of file descriptor leakage. It happens because there are too many open 
files and they are not closed. There might be chances where a programmer 
may forget to close an opened file. So we will use “with” statement to do task 
as context manger."""

#Ex:File management using context-manager i.e with staetement
with open("PES_data.txt","a") as f:
    f.write("pesu\n")
    f.write("Electronic\n")
    f.write("City\n")
    print("Is File Closed: ",f.closed)

print("Is File closed: ",f.closed)


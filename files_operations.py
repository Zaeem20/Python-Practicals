# File operations in Python

file = open('hello.txt', 'r+')                            # Returns FileObject
print("Read File contents until 5 bytes:", file.read(5))
print("Current Position of Pointer:", file.tell())       # tell() returns position of pointer
file.seek(0)                                             # Reset Pointer Position to first character
print("Content with 35 bytes:",file.read(38))

file.close()   # Closing file using close() also can be done with context manager

print("Coded By Durani Mohammed Zaeem; Roll no: 425")
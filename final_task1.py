import functools
read= open("names.txt", 'r').read().split('\n')

#1
print(sorted(read, key=lambda x: len(x))[-1])

#2
print(functools.reduce(lambda x, y: int(x) + int(y), [len(i) for i in read]))

#3
words=sorted(read, key=lambda x: len(x))
length=sorted([len(i) for i in read], key=lambda x: x)[0]
[print(i) for i in words if len(i)==length]

#4
file= open("name_length.txt", 'w')
[file.write(str(i)+'\n') for i in ([len(i) for i in read])]

#5
num= int(input("Enter name length: "))
[print(i) for i in read if len(i)==num]



myfile = open('myfile.txt','w')
myfile.write('Привет Алекс!\n')
myfile.write('Как Дела?')
myfile.close()

read_stroke = open('myfile.txt')
read = read_stroke.readline()
print(read)
read = read_stroke.readline()
print(read)
import csv
# task 1
with open('new.txt', 'w') as file:
    file.write("Hello, world!\n")
# task 2
with open('new.txt', 'r') as file:
    line = file.readline()
    print(line)
# task 3
with open('new.txt', 'a') as file:
    file.write("new line!\n")
# task 4
with open('new.txt', 'r') as file:
    lines = file.readlines()
    count = len(lines)
    print("Number of lines in the file: ",count)
# task 5
inp = input("Enter the word u want to count: ")
i = 0
with open('new.txt', 'r') as file:
    all = file.read()
    word = all.split()
    for words in word:
        if(words == inp):
            i = i+1
print(f"{inp} has appeared {i} times in the file\n")
# task 6
file = open('new.txt', 'r')
file1 = open('new1.txt', 'w')
content = file.read()
file1.write(content)
file.close()
file1.close()
# task 7
inp = input("Enter the word u want to replace: ")
inp1 = input("Enter the new word: ")
i = 0
with open('new.txt', 'r') as file:
    all = file.read()
with open('new.txt', 'w') as file:
    all1 = all.replace(inp, inp1)
    file.write(all1)
# task 8
open('data.csv','w')
with open('data.csv', 'r') as file:
    read = csv.reader(file)
    for row in read:
        print(row)
# task 9
with open('data.csv', 'w', newline='') as file:
    writ = csv.writer(file)
    writ.writerow(['Name', 'Age'])
    writ.writerow(['Numan', 19])
    writ.writerow(['Ahmad', 21])

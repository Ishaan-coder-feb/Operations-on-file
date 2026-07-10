file=open("class-notes.txt","w")
file.write("Math:Algebra")
file.write("Science:Atoms")
file.write("English:Vocabulary")
file = open("class-notes.txt", "r")

characters = int(input("How many characters would you like to preview? "))
preview = file.read(characters)

print("Preview:", preview)

file.close()

file = open("class-notes.txt", "r")

lines = file.readlines()

file.close()

for i in range(len(lines)):
    print(i + 1, "->", lines[i].strip())

word = input("Lines to skip start with which subject: ")

file = open("class-notes.txt", "r")

for line in file:
    if line.startswith(word):
        print("skip ->", line.strip())
    else:
        print("keep ->", line.strip())

file.close()

new_file = open("odd-notes.txt", "w")

for i in range(len(lines)):
    if (i + 1) % 2 == 1:
        new_file.write(lines[i])
new_file.close()
    

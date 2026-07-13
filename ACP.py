file=open("Class-notes.txt","w")
file.write("Maths:Algebra \n")
file.write("Science:Gravity \n")
file.write("English:Vocabulary \n")
file.write("skip Geography:World Map \n")
file.write("skip History:Roman Empire \n")
file.close()
file=open("Class-notes.txt","r")
print("The first 40 characters are: \n",file.read(40))
file.close()
file=open("Class-notes.txt","r")
lines=file.readlines()
print("The number of lines in my class notes file is ",len(lines))
for i in range(len(lines)):
    print(i+1,"=>",lines[i].strip())
file.close()
file=open("Class-notes.txt","r")
for line in file:
    print(line.strip())
file.close()
file=open("Class-notes.txt","r")
for line in file:
    if line.startswith("skip"):
        print('skip ->', line.strip())
    else:
        print('keep ->', line.strip())
file.close()
file=open("Class-notes.txt","r")
cls_notes=open("Organised_notes.txt","w")
for line in file:
     if line.startswith(("Maths","Science","English")):
         cls_notes.write(line)
         print('skip ->', line.strip())
file.close()
cls_notes.close()

cls_notes=open("Organised_notes.txt","r")
print("Organised notes: \n",cls_notes.read())
file.close()

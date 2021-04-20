courses = ['math 3012', 'psyc 1101', 'cs 4001']
syllabus = open("out_text.txt","r")
doc = syllabus.readlines()
newDoc = []
for l in doc:
    newDoc.append(l.lower())
course = ""
for l in newDoc:
    for c in courses:
        if c in l:
            course = c

print(newDoc)
print(course)

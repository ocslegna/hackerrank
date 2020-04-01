# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())
dStudents = dict()
for i in range(0,N):
    sStudent = input()
    aWords = sStudent.split()
    sName = aWords[0]
    fTemp = (float(aWords[1]) + float(aWords[2]) + float(aWords[3])) / 3
    fPercentage = "%.2f" % (fTemp)
    dStudents[sName] = fPercentage
    
sSelectStudent = input()
if (sSelectStudent in dStudents):
    print(dStudents[sSelectStudent])
else:
    print(0)

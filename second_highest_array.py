all_stud = list()
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     tmp_stud = list()
#     tmp_stud.append(name)
#     tmp_stud.append(score)
#     all_stud.append(tmp_stud)

all_stud.append(['x',20])
all_stud.append(['y',40])
all_stud.append(['a',20])
all_stud.append(['y',27])

print(sorted(all_stud, key= lambda x : x[1]))
l = 0
sorted_stud = sorted(all_stud, key= lambda x : x[1])
marks = sorted(all_stud, key= lambda x : x[1])[1][1]
for i in range(len(sorted_stud)):

    if(marks == sorted_stud[i+1][1]):
        marks = sorted_stud[i+1][1]
#        print(sorted_stud[i+1][0])
    else :
        break

marksheet = all_stud
# for _ in range(0,int(input())):
#     marksheet.append([input(), float(input())])

second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
print(second_highest)
#print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))

print(a for a,b in sorted(marksheet))
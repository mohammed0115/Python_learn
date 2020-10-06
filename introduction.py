certificate={"Arabic languge":98,
"Quaran karim":78,"mathmatic":80,
"English language":85, "physic":90,
"chemical":80,"computer ":89}
list_values=certificate.values()
student_RealGPA=[degree/25 for degree in list_values]
GPA_list=[]
print(student_RealGPA)
for i in student_RealGPA:
    if i >3.5:
        GPA_list.append(4)
    elif i<=3.5 and i>3:
        GPA_list.append(3.5)
    elif i <=3 and i>2.5:
        GPA_list.append(3)
    elif i <=2.5 and i>2:
        GPA_list.append(2.5)
    elif i <=2 and i>1.5:
        GPA_list.append(2)
    elif i <=1.5 and i>1:
        GPA_list.append(1)
    elif i ==1 :
        GPA_list.append(1)
    else:
        GPA_list.append(0)
       

print(GPA_list)

Result =[i*3 for i in GPA_list]
Result=round(sum(Result)/(len(Result)*3),2)
print(Result)



def GetDict(**kwargs):
    for i, j in kwargs.items():
        print(i, j)

GetDict(**certificate)















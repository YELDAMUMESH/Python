#Receiving input form user
def user_input():
    a=int(input("Enter marks: "))
    marks.append(a)
    
#Calucalting percentage
def percentage(score):
    total_percenatge= (score[0]+score[1]+score[2]+score[3])/4
    print(f"Total percenatge: {total_percenatge}")
    if(total_percenatge>=90):
        grade="O"
    elif(total_percenatge>=80 and total_percenatge<90):
        grade="A"
    elif(total_percenatge>=70 and total_percenatge<80):
        grade="B"
    elif(total_percenatge>=60 and total_percenatge<70):
        grade="C"
    else:
        grade="F"
    
    return grade

#Main program

marks=[]
user_input()
user_input()
user_input()
user_input()
print(marks)
print(f"Grade: {percentage(marks)}")
    
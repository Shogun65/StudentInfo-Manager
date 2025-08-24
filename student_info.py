import sys
class Student:

    def __init__(self,student_name,student_age,student_class):
        self.student_name=student_name
        self.student_age=student_age
        self.student_class=student_class
        
    def get_student_name(self) -> str:
        return self.student_name
    
    def get_student_age(self)-> str:
        return self.student_age
    
    def get_student_class(self)-> str:
        return self.student_class
    
student_list=["Chahat","Raiden","Nahida","Furina"]
student_info={
"Chahat":Student(student_name="Chahat",student_age=16,student_class=11),
 "Raiden":Student(student_name="Raiden shogun",student_age=500,student_class=11),
"Nahida":Student(student_name="Nahida",student_age=500,student_class=11),
"Furina":Student(student_name="Furina",student_age=18,student_class=11)}

for i in student_list:
    print(i)
print("Those are student data we have!!\nif you want to see there data pleace login to admin!!")

def main():

    user_inputs=input("\nEnter admin password or type exit: ")
    if user_inputs.lower().startswith("exit"):
        sys.exit()
    elif user_inputs == "6511":
        reqest_data=input("Enter that student name: ").capitalize()
        student_data(reqest_data)
    else:
        print("I cant unserstand you!\n")
        main()

def student_data(reqested):

    if reqested in student_info:
        student=student_info[reqested]
        student_name=student.get_student_name()
        student_age=student.get_student_age()
        student_class=student.get_student_class()
        print("--------student-info-------")
        print(f"Name:{student_name}")
        print(f"Age:{student_age}")
        print(f"Class:{student_class}")
        print("---------------------------")
    else:
        print("Student_not_find!!\n")
        main()

if __name__ =="__main__":
    main()









class School:
    def __init__(self,name,id,standard,classTeacher):
        self.standard=standard
        self.id=id
        self.classTeacher=classTeacher
        self.name=name
        self.classTeacher=classTeacher
        
    def Teaching(self,subject):
            print("{} is Teaching".format(subject))
            print()
    
    def which_standard(self):
        print(" {}th standard".format(self.standard))
        print()
    
    def get_fee_details(self):
        print("{} fee is {}".format(self.name,self.standard*2000))
        print()
    
    def get_student_details(self):
        print("student name {} ".format(self.name))
       
        print("student id is {}".format(self.id))
        
        print(f"you are {self.standard}th standard")
        
        print("class teacher is {}".format(self.classTeacher),"\n")
        
       
        
        
vamshi=School("vamshi","007",10,"Nehan")
rajashekar=School("Rajashekar","008",9,"Nehan")
pushpa=School("Pushpa","009",8,"Nehan")
kalyan=School("Kalyan","010",7,"Nihan")
priyanka=School("priyanka","011",6,"Nihan")
dinesh=School("Dinesh","012",6,"Nihan")

def call_main():
    vamshi.get_student_details()
    vamshi.get_fee_details()
    
    rajashekar.get_student_details()
    rajashekar.get_fee_details()
    
    pushpa.get_student_details()
    pushpa.get_fee_details()
    
    kalyan.get_student_details()
    kalyan.get_fee_details()
    
    priyanka.get_student_details()
    priyanka.get_fee_details()
    
    dinesh.get_student_details()
    dinesh.get_fee_details()
call_main()

        
        

        
        
        
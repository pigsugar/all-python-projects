class Citizen:
    def __init__(self,name,age,dob,id_number):
         self.citizen_name = name
        self. citizen_age = age
        self.citizen_dob = dob
        self.citizen_id = id_number
        
    def add_citizen(self):
        print("name: "+self.citizen_name)
        print("age: "+str(self.citizen_age))
        print("dob: "+self.citizen_dob)
        print("id: "+self.citizen_id)
        
citizen1 = Citizen("peter",8,"19th october 2014","0198" )    
citizen1.add_citizen()  

citizen2 = Citizen("sophia",10,"19th october 2012","0199")
citizen2.add_citizen()
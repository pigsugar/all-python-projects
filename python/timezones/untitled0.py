class doctor():
    def __init__(self):
        print ("this is class doctor")
        
    def bmi(weight, height):
        bmi = weight/(height*height)
        print("your bmi is "+str(bmi))
        
    def heartrate(heart_rates):
        if heart_rates>60 and heart_rates<100:
            print("your heartrate is normal")
        else: 
            print("your heart rate is not normal visit the docter")
            
class patient(doctor):

    def __init__(self, name, weight, height, heart_rate):
        self.patient_name = name     
        self.patient_weight = weight  
        self.patient_height = height  
        self.patient_heartrates = heart_rate 
        
    def healthcheck(self):
        print("\n patient name: ",self.patient_name)
        doctor.bmi(self.patient_weight, self.patient_height)
        doctor.heartrate(self.patient_heartrates)
        
patient1 = patient("micheal",30, 0.9144,80 )
patient1.healthcheck()

patient2 = patient("jessica",40,1,120) 
patient2.healthcheck()       
            
            


class Cellphone:
    
    
    default_ring_tone = "chime1.mp3"
    default_mode = "light"
    
    def  __init__(self, phone_number:str):
        self.phone_number = phone_number
        self.ring_tone = Cellphone.default_ring_tone
        self.mode = Cellphone.default_mode
        
        
    def get_phone_number(self):
        return self.phone_number
    
    def set_phone_number(self, new_phone_number:str):
        if len(new_phone_number) == 10:
            self.phone_number = new_phone_number
        
        
    def call(self, other_phone:str):
            other_phone.ring()
        
    def ring(self):
        print(f"{self.phone_number} is ringing")
    
    def __str__(self):
        return self.phone_number
        
    
phone1 = Cellphone("1234567890")

print(phone1)

phone1.set_phone_number("12345677775")
print(phone1)
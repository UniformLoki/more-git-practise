class Cellphone:
    
    
    default_ring_tone = "chime1.mp3"
    default_mode = "light"
    
    def  __init__(self, phone_number:str):
        self.phone_number = phone_number
        self.ring_tone = Cellphone.default_ring_tone
        self.mode = Cellphone.default_mode
        
        
        #getter
    @property
    def phone_number(self):
        print("ha-i this is getter")
        return self._phone_number
    
    #setter
    @phone_number.setter
    def phone_number(self, new_phone_number:str):
        print("high this is setter")
        if len(new_phone_number) == 10:
            self._phone_number = new_phone_number
        
        
    def call(self, other_phone:str):
            other_phone.ring()
        
    def ring(self):
        print(f"{self.phone_number} is ringing")
    
    def __str__(self):
        return self.phone_number
        
    
phone1 = Cellphone("1234567890")

print(phone1)

from datetime import date


# das
class Kontakt:
    def __init__(self, nachname: str, vorname: str, room_id: int, date_of_birth: date):
        # nn -übergabeparameter
        self.nachname = nachname 
        self.vorname = vorname
        self.room_id = room_id
        self.date_of_birth = date_of_birth
        pass  

    @property
    def room_id(self):
        return self.__room_id

    @room_id.setter
    def room_id(self, value):
        if isinstance(value, int) and len(str(value)) == 4:
            self.__room_id = value
        else: 
            #print("Falscher Input. Room ID muss eine vierstellige Zahl sein.")
            raise ValueError("Falscher Input")

        
#room_id - attribute 
#__room_id - property
#_ protected 
#__ private
# in class funk = methode
# in class  Variable = att/prop

bene = Kontakt(1, "Benedict", 31788, date(1901,4,4))

date(1999,1,1)

sebastian = Kontakt("Essen", "Sebastian", 3165, "2")


print(bene.vorname)
print(bene.room_id)
print(sebastian.date_of_birth)

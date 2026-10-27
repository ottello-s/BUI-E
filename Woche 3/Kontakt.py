


# das
class Kontakt:
    def __init__(self, nachname: str, vorname: str, room_id: int):
        # nn -übergabeparameter
        self.nachname = nachname 
        self.vorname = vorname
        self.room_id = room_id
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

bene = Kontakt(1, "Benedict", 31788)

print(bene.vorname)
print(bene.room_id)


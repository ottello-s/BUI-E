from datetime import date

# -- class --
class Kontakt:
    def __init__(self, nachname: str, vorname: str, room_id: int, date_of_birth: date | None = None):
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
            # print("Falscher Input. Room ID muss eine vierstellige Zahl sein.")
            raise ValueError("Falscher Input.")

# -- skript --
bene = Kontakt("Harder", "Benedict", 3178)

seb_bd = date(1999, 1, 1)

sebastian = Kontakt("Esser", "Sebastian", 3165, seb_bd)

print(bene.nachname)
print(bene.room_id)
print(sebastian.date_of_birth)
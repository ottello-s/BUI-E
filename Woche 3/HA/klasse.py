import random
import datetime 
from faker import Faker




class Student:
    def __init__(self, nachname:str , vorname:str, matrikelnummer):
        self.nachname = nachname
        self.vorname = vorname
        self.matrikelnummer = matrikelnummer
        self.pruefungen = []
        pass

    @property
    def matrikelnummer (self):
        return self.__matrikelnummer

    @matrikelnummer.setter
    def matrikelnummer (self, value):
        if isinstance(value, int) and len(str(value)) == 7:
            self.__matrikelnummer = value
        else:
            raise ValueError("Falscher Input")

    def __str__(self):
        return f"{self.vorname} {self.nachname}, Matrikelnummer: {self.matrikelnummer}"

class Examiner:
    def __init__(self,nachname:str, vorname:str, mitarbeiter_id):
        self.nachname = nachname
        self.vorname = vorname
        self.mitarbeiter_id = mitarbeiter_id
        
        pass

    @property
    def mitarbeiter_id(self):
        return self.__mitarbeiter_id

    @mitarbeiter_id.setter
    def mitarbeiter_id(self,value):
        if isinstance(value, int):
            self.__mitarbeiter_id = value

    def __str__(self):
        return f"{self.nachname} {self.vorname} {self.mitarbeiter_id}"


class Exam:
    def __init__(self,name,datum,ort,dozent):
        self.name = name
        self.datum = datum
        self.ort = ort
        self.dozent = dozent
        self.teilnehmer = []
        pass

    @property
    def datum(self):
        return self.__datum
    
    @datum.setter
    def datum(self,value):
        if isinstance(value, datetime.date):
            self.__datum = value
        else:
            raise ValueError

    def anmeldung(self,value):
        if isinstance(value,Student):
            self.teilnehmer.append(value)
            value.pruefungen.append(self)

        else: 
            raise ValueError("Falscher Input")

    @property
    def dozent(self):
        return self.__dozent
    
    @dozent.setter
    def dozent(self,value):
        if isinstance(value, Examiner):
            self.__dozent = value


    def __str__(self):
        return f"{self.name} {self.datum} {self.ort} {self.dozent}"

fake = Faker()

Studenten = []
for i in range(5):
    Studenten.append(
        Student(fake.last_name(),
                fake.first_name(),
                random.randint(1000000,9999999)
        )
    )    

DozentI = Examiner("Schmidt","Andreas",1000000)
DozentII = Examiner("Mueller","Stefan",9999999)


BUIEPrüfung = Exam("BUI-Ergaenzung",datetime.date(2027, 2, 21),"CIP-Raum", DozentI)
StatikI = Exam("Statik I",datetime.date(2027, 3, 3),"Audimax", DozentII)
StatikII = Exam("Statik II",datetime.date(2027, 3, 6),"Audimax", DozentII)



for i in Studenten[0:3]:
    BUIEPrüfung.anmeldung(i)


for i in Studenten[3:]:
    StatikI.anmeldung(i)


for i in Studenten:
    StatikII.anmeldung(i)



for student in Studenten:
    print(student)

print(StatikI.teilnehmer)
print(StatikII.teilnehmer)
print(BUIEPrüfung.teilnehmer)

print(f"Prüfungen von {Studenten[3]}: ")
for i in Studenten[3].pruefungen:
    print(i)


for i in BUIEPrüfung.teilnehmer:
    print(i.vorname, i.nachname)
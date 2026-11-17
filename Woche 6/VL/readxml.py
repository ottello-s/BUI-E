from pprint import pprint 
from pathlib import Path
import xml.dom.minidom



class Person:
    def __init__(self, nation, vorname, nachname, geburtsdatum):
        self.nation = nation
        self.vorname = vorname
        self.nachname = nachname
        self.geburtsdatum = geburtsdatum

doc = xml.dom.minidom.parse("personen.xml")
personen = []
all_persons_xml = doc.getElementsByTagName("Person")

for i in all_persons_xml:

    n =  i.getAttribute("nation")
    vn =  i.getElementsByTagName("Vorname")[0].firstChild.data
    nn =  i.getElementsByTagName("Nachname")[0].firstChild.data
    gd =  i.getElementsByTagName("Geburtsdatum")[0].getAttribute("date")

    person = Person(nation=n,vorname=vn,nachname=nn,geburtsdatum=gd)
    personen.append(person)

pprint(personen)
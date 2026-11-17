import json

class Contact:
    def __init__(self, first, family, phone):
        self.first_name = first
        self.family_name = family
        self.phone = phone

    def __repr__(self):
        return "Contact: {} {}".format(self.first_name, self.family_name)


    @classmethod
    def from_json(cls, raw_data):
        first_name = raw_data["Vorname"]
        last_name = raw_data["Nachname"]
        phone = raw_data["Kommunikation"]["Handynummer"]

        return cls(first_name, last_name, phone)


if __name__ == "__main__":

    with open("ContactData_german.json") as f:
        data = json.load(f)


    print(data)


maxi = Contact.from_json(data)

print(maxi)

#RESTAPI vor?funktion danach argumente 
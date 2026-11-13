from Kontakt import Kontakt

class TUMKontakt(Kontakt):

    def __init__(self, nachname, vorname, room_id, date_of_birth = None):
        super().__init__(nachname, vorname, room_id, date_of_birth)
        self.email = self.build_tum_mail()

    def build_tum_mail(self):

        email = f"{self.vorname}.{self.nachname}@tum.de"

        return email

benedict = TUMKontakt("Harder", "Benedict", 3178)

print(benedict.email)
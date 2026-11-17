class Contact:

    def __init__(self, first, family, phone):
        self.first_name = first
        self.family_name = family
        self.phone = phone

    def __repr__(self):
        return "Contact: {} {}".format(self.first_name, self.family_name)

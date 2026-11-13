from Cuboid import Cuboid


class Cube(Cuboid):
    def __init__(self,length:float):
        super().__init__(length,length,length)

    #die Methode ist schon in der Cuboid-klasse angelegt
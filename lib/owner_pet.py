class Pet:
    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    
    def __init__(self, name, pet_type, owner = None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
    
    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, value):
        if value not in Pet.PET_TYPES:
            raise Exception("Pet not it types")
        self._pet_type = value

        


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [my_pets for my_pets in Pet.all if self == my_pets.owner]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("not a pet class")
        
        pet.owner = self

    def get_sorted_pets(self):
        return sorted([pets for pets in Pet.all if self == pets.owner], key=lambda pet: pet.name)
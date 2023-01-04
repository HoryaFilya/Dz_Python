class Pivo:

    def __init__(self, name, volume, IBU):
        self.name = name
        self.volume = volume
        self.IBU = IBU

    def drive_away(self):
        if self.IBU < 10:
            return 'Слабое пиво'
        elif 10 <= self.IBU < 30:
            return 'Среднее пиво'
        return 'Крепкое пиво'
    
    def performance(self):
        return f'{self.name} ({self.volume})' 
    
    def estimation(self):
        if self.IBU < 10:
            return 'Очень сладкое пиво'
        elif 10 <= self.IBU < 30:
            return 'Отличное пиво'
        return 'Очень горькое пиво'



class Barbie:

    def __init__(self, appearance, mentality, character):
        self.appearance = appearance
        self.mentality = mentality
        self.character = character
    
    def get_appearance(self):
        return self.appearance
    
    def get_mentality(self):
        return self.mentality
    
    def get_character(self):
        return self.character
    
    def set_appearance(self, new_appearance):
        self.appearance = new_appearance
    
    def set_mentality(self, new_mentality):
        self.mentality = new_mentality
    
    def set_character(self, new_character):
        self.character = new_character
    
    def print_info(self):
        print(f'Внешний вид: {self.appearance}, ментальность: {self.mentality}, характер: {self.character}')

class BarbieDoll(Barbie):

    def __init__(self, appearance, mentality, character, material, type_of_production, colour, eyes, skirt):
        super().__init__(appearance, mentality, character)
        self.material = material
        self.type_of_production = type_of_production
        self.colour = colour
        self.eyes = eyes
        self.skirt = skirt

    def get_material(self):
        return self.material
    
    def get_type_of_production(self):
        return self.type_of_production
    
    def get_colour(self):
        return self.colour
    
    def get_eyes(self):
        return self.eyes
    
    def get_skirt(self):
        return self.skirt
    
    def set_material(self, new_material):
        self.material = new_material
    
    def set_type_of_production(self, new_type_of_production):
        self.type_of_production = new_type_of_production
    
    def set_colour(self, new_colour):
        self.colour = new_colour

    def set_eyes(self, new_eyes):
        self.eyes = new_eyes
    
    def set_skirt(self, new_skirt):
        self.skirt = new_skirt

    def print_info(self):
        super().print_info()
        print(f'Материал: {self.material}, тип производства: {self.type_of_production}, цвет: {self.colour}, глаза: {self.eyes}, юбка: {self.skirt}')
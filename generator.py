class Teacher:
    def __init__(self, name, program, antiprogram, smeni):
        """Constructor"""
        self.program = program
        self.name = name
        self.antiprogram = antiprogram
        self.smeni = smeni
class ClassRoom:
    def __init__(self, name, places, type_of_discipline, differences, prioritet_discipline, anti_discipline):
        """Constructor"""
        self.name= name
        self.places = places
        self.type_of_discipline = type_of_discipline
        self.differences = differences
        self.prioritet_discipline = prioritet_discipline
        self.anti_discipline = anti_discipline

class Program:
    def __init__(self, name, hours, hours_proizv, hours_distant, day_offline, count_of_groups, zz):
        self.name = name
        self.hours = hours

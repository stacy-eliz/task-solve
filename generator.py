class Teacher:
    def __init__(self, number, name, program, antiprogram, smeni):
        """Constructor"""
        self.number = number
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
    def __init__(self, name, hours, hours_proizv, hours_distant, day_offline, count_of_groups, count_of_worker, count_of_listener, count_of_teacher, count_of_classroom, number_of_program):
        self.name = name
        self.hours = hours
        self.hours_proizv = hours_proizv
        self.hours_distant = hours_distant
        self.day_offline = day_offline
        self.count_of_groups = count_of_groups
        self.count_of_worker = count_of_worker
        self.count_of_listener = count_of_listener
        self.count_of_teacher = count_of_teacher
        self.count_of_classroom = count_of_classroom
        self.number_of_program = number_of_program


class School:
    def __init__(self, name):
        self.name = name
        self.roster = {}
        
    def add_student(self, full_name, grade):
        if grade not in self.roster:
            self.roster[grade] = []
            self.roster[grade].append(full_name)
        else:
            self.roster[grade].append(full_name)
    
    def grade(self, grade):
        return self.roster[grade]
    
    def sort_roster(self):
        new_dict = self.roster
        for key in new_dict:
            new_dict[key].sort()
        return new_dict
class Military:
    class Unit:
        def __init__(self, name, ID,  position):
            self.name = name
            self.ID = ID
            self.position = position
        
        def display_info(self):
            print(f"Name: Comrad {self.name}, ID: {self.ID}, Position: {self.position}")

    
    def __init__(self,name):
        self.name = name
        self.Soldiers = []
        self.total_soldiers = 0

    
    def add_Soldiers(self, name, ID, position):
        soldier = self.Unit(name, ID, position)
        self.Soldiers.append(soldier)
        self.total_soldiers += 1
    
    def display_soldier_info(self):
        for comrad in self.Soldiers:
             comrad.display_info()
            
            
    
    def show_total_army(self):
        print(f"Total Military Might of the Khaganate: {self.total_soldiers}")


'''
 # @ Author: Your name
 # @ Create Time: 2023-09-06 13:57:39
 # @ Modified by: Your name
 # @ Modified time: 2023-09-06 13:57:43
 # @ Description:
 '''

# single responsibility principle (SRP) AKA separation of concerns (SOC)

class Journal:
    def __init__(self) -> None:
        self.entries = []
        self.count = 0
    
    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")
        
    def remove_entry(self, pos):
        del self.entries[pos]
    
    def save(self, filename):
        file = open(filename, 'w')
        file.write(str(self))
        file.close()
    
    def load(self, filename):
        pass
    
    def low_from_web(self, uri):
        pass
    
    def __str__(self):
        return '\n'.join(self.entries)
    
class PersistenceManager():
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, "w")
        file.write(str(journal))
        file.close()



if __name__ == "__main__":
    j = Journal()
    j.add_entry('I cried today')
    j.add_entry('I ate a bug')
    print(f'Journal entries: \n{j}')
    
    manager = PersistenceManager()
    manager.save_to_file(j,"./test")
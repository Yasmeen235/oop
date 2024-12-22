class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")



class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)  
        self.team_size = team_size

    def display_info(self):
        super().display_info()  
        print(f"Team Size: {self.team_size}")



class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")



manager = Manager("Sara", 5000, 10)
developer = Developer("Ali", 4000, "Python")


manager.display_info()
print("---")
developer.display_info()

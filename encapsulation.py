from typing import List, Optional

class Employee:
    def __init__(self, name: str, age: List[int], project: List[str], employment_contract: List[str], salary: List[str]) -> None:
        """_summary_

        Args:
            name (str): names of the employees
            age: Their individual age
            project: The project htey work on
            employment_contract: The type of contract issued!
        """
        self.name = name
        self.__age = age
        self.project = project
        self.employment_contract = employment_contract
        self.__salary = salary

    def getMethod(self)-> None:
        """method returns the variable value
        """
        return self.setMethod()

    def setMethod(self, age) -> None:
        """setter method sets the value
        """
        self.age: List[str] =  age
        for i in age:
            if (self.__age == age) and (self.__age > age):
                return ("age is the same!")
            else:
                return ("Age is not the same!")

#Nexted method in encapsulation

    def fetch_employee_info(self, prefix):
        result = [i for i in self.name if i.startswith(prefix)]
        if self.__age == 31:
                return "The man is Tomek Sobiech, my crush!"
        elif self.employment_contract == "part_time":
            if self.name != "Lukasz":
                print("That is my manager, and he did not do well at all!")
        else:
            return "what a great experience to meet them!"

    def process(self, numbers):
        def helper(n):
            # This is a simple helper function
            return n * n

        results: List = []
        for number in numbers:
            results.append(helper(number))
        return results




def main():
    name = ["Abudu", "Tomek", "Lukasz", "Arr", "Mama"]
    age = [23, 45, 65, 31, 30, 33, 22]
    project = ["smart bathroom", "Zenlo", "Azoyen", "everything_is_project_here"]
    employment_contract = ["B2B", "contract of employment", "part time"]
    salary = ["15k", "7.33k", "30k", "15k"]
    emp = Employee(name=name, age=age, project=project, employment_contract=employment_contract, salary=salary)
    #print(emp.__age)
    #print(emp.__salary) #since it is private, we cannot access it directly, we need a sette and getter method to be able to access it
    #print(emp.name)
    #print(emp.setMethod(age=age))
    #print(emp.getMethod())
    print(emp.fetch_employee_info(prefix = "T"))
    processor = Employee(name=name, age=age, project=project, employment_contract=employment_contract, salary=salary)
    print(processor.process([1, 2, 3, 4]))

if __name__ == "__main__":
    main()
                
    
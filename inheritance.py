import tracemalloc

from introduction import Car
from typing import List


class File_Handling(Car):
    """We want to see how inheritance works.

    Args:
        Car: This is the class we are inheriting from, passing it as a parameter.
    """
    def __init__(self, colour: List[str], Mileage: int, RPM: int, result: int) -> int:
        super().__init__(colour, Mileage, RPM, result)
        self.__RPM = 8000
        print(f"we want to see how it works without a method in the child class: {self.calculate_distance(560,30)}")
        print(f"we want to see how it works without a method in the child class: {self.brake()}")
        print(f"To print the private attributes: {self.__RPM}")
    
    def understanding_inher(self) -> int:
        """We want to test how inheritance works here"""
        while True:
            if (self.Mileage == 40) and (time != 40):
                print(f"this is cool, to use the method and attributes of another class: {self.brake()}")
            else:
                print(self.calculate_distance())

class WithoutConstruct:
    """write classes without constructor ppties, and see how it works!
    """
    def calculate_memory_usage(self, k: int)-> None:
        tracemalloc.start()
        answer = "this is it"
        resutl_a = [i**2 for i in range(k)]
        result_b = [i.upper() for i in range(k, len(answer)) if answer[i].endswith("it")]
        current, peak = tracemalloc.get_traced_memory()
        print(f"Current memory usage is {current / 1024**2:.2f} MB; Peak was {peak / 1024**2:.2f} MB")
        tracemalloc.stop()
        return result_b


#obj = File_Handling(["black", "blue"], 2, 3800, result=3)
obj2 = WithoutConstruct()
print(obj2.calculate_memory_usage(5))
#obj.understanding_inher()
#print(obj)
#if __name__ == "__name__":
   # inher = file_handling(["black", "blue"], 2, 3800, result=None)
   #print(inher.understanding_inher())
   # print(inher)


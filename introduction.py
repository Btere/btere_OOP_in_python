from typing import List


class Car:
    def __init__(self, colour: List[str], Mileage: int, RPM: int, result: int) -> None:
        self.colour = colour
        self.Mileage = Mileage
        self.RPM = RPM
        self.result = 0
        #self.understanding_inher()

    def brake(self) -> List:
        if "black" in self.colour:
            self.colour.append("red")
            return self.colour
        elif (self.Mileage <= 3) or (self.RPM == 6500):
            return self.colour.pop()
        else:
            return None
    def calculate_distance(self, speed: int, time: int) -> int:
        """We want to calculate the distance travelled by car

        Args:
            speed: The speed of the car in km/hr
            time: The time taken in (sec).

        Returns:
            return an int answer
        """
        while(time < 40):
            if (speed < 450):
                self.result = speed * time
                print(self.result)
            elif (speed > 720) and (self.RPM < 4000):
                return (self.brake())
            elif (speed == 120) or (self.Mileage * time == 67600):
                return self.time
            else:
                return (speed * time)
    def __repr__(self) -> List[str]:
        return f"The Mileage of the car {self.Mileage}"
    
    def __str__(self) -> object:
        return f"how does this work: {self.colour}"   #this dunder methods enables us to see the varaibles when we create an object of the class!


if __name__ == "__main__":

    myobj = Car(["black", "blue"], 2, 3800, result=5)
    #print(myobj)                                                       #This will print the memory address of the  object/instance of the class, instead of the details we want to see
    #print(repr(myobj))
    # print(str(myobj))                                    
    print(myobj.brake())                                            #you can call the object.method
    print(myobj.colour)                                             #you can call the object.properties
    obj3 = Car(["black", "blue"], 2, 3800, result=5)
    #print(obj3)                                                #This print the memory address of the variable obj3
                                                                #To see the main properties, we could use a dataclass or a dunder method
    obje2 = Car(["black", "blue"], 2, 3800,result=5)
    print(obje2.calculate_distance(850, 20))
    
    

# If you want to run a code and suppress the result from appearing in the console while only allowing 
#logging messages to be shown, you can use Python's logging module. loguru, context manager and io.StringIO
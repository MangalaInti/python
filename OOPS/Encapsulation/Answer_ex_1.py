class Athlete:
    def __init__(self, name, gender):
        self.__name = name  # Private attribute
        self.__gender = gender  # Private attribute

    # Accessor methods (getters)
    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender

    # Mutator methods (setters)
    def set_name(self, name):
        self.__name = name

    def set_gender(self, gender):
        self.__gender = gender

    def running(self):
        if self.__gender == "girl":
            print(f"{self.__name} is running 150mtr")
        else:
            print(f"{self.__name} is running 200mtr")

# Create an instance of Athlete for Maria
maria = Athlete(name="Maria", gender="girl")

# Accessor methods to get and print attributes
print(f"Name: {maria.get_name()}")
print(f"Gender: {maria.get_gender()}")

# Mutator methods to change attributes
maria.set_name("Maria Rodriguez")
maria.set_gender("woman")

# Running method
maria.running()

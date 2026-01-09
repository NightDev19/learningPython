from Vechicle import Vehicle


class Motorcycle(Vehicle):
    def start_engine(self):
        print("Motorcycle engine started.")

    def stop_engine(self):
        print("Motorcycle engine stopped.")

    def drive(self):
        print("Motorcycle is driving.")

    def pop_wheelie(self):
        print("Motorcycle is popping a wheelie!")

from Vechicle import Vehicle


class Car(Vehicle):
    def start_engine(self):
        print("Car engine started.")

    def stop_engine(self):
        print("Car engine stopped.")

    def drive(self):
        print("Car is driving.")

    def brake(self):
        print("Car is braking.")

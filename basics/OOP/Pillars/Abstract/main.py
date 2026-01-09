import Car
import Motorcycle


def main():
    my_car = Car.Car()
    my_motorcycle = Motorcycle.Motorcycle()

    my_car.start_engine()
    my_car.drive()
    my_car.brake()
    my_car.stop_engine()

    print()  # Just for better readability in output

    my_motorcycle.start_engine()
    my_motorcycle.drive()
    my_motorcycle.pop_wheelie()
    my_motorcycle.stop_engine()


if __name__ == "__main__":
    main()

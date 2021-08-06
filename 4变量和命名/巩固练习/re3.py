cars = 100                                                  # the number of cars
space_in_a_car = 4.0                                        # the number of spaces in a car (a small car, isn't it?)
drivers = 30                                                # the number of drivers avaliable
passengers = 90                                             # the number of passengers
cars_not_driven = cars - drivers                            # the cars which cannot be driven because of the lack of driver
cars_driven = drivers                                       # the cars driven by drivers (assume that every driver drives one car)
carpool_capacity = cars_driven * space_in_a_car             # how many passangers the carpool can carry (is there any mistakes in this calculation?)
average_passengers_per_car = passengers / cars_driven       # average passengers in one car


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers avaliable")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
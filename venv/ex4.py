#affects 100 to the cars variable
cars = 100
#affects 4.0 to the space_in_a_car variable
space_in_a_car = 4.0
#affects 30 to the drivers variable
drivers = 30
#affects 90 to the passengers variable
passengers = 90
#affects the the subtraction of cars and drivers to the cars_not_driven variable
cars_not_driven = cars - drivers
#affects the value of drivers to the cars_driven variable
cars_driven = drivers
#affects the multiplication of cars_driven and space_in_a_car to the carpool_capacity variable
carpool_capacity = cars_driven * space_in_a_car
#affects the division passengers and cars_driven to the average_passengers_per_car variable
average_passengers_per_car = passengers / cars_driven
# display the value of car variable
print("There are", cars, "cars available.")
# display the value of drivers variable
print("There are only", drivers, "drivers available.")
# display the value of cars_not_driven variable
print("There will be", cars_not_driven, "empty cars today.")
# display the value of carpool_capacity variable
print("We can transport", carpool_capacity, "people today.")
# display the value of passengers variable
print("We have", passengers, "to carpool today.")
# display the value of average_passengers_per_car variable
print("We neeed to put about", average_passengers_per_car, "in each car.")
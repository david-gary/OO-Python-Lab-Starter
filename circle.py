import math  # use the math.pi value from this library


class Circle:

    # Add the constructor method here
    # - It should take one argument, the radius of the circle
    # - The radius argument should be stored in an attribute called "radius"
    # - Add an attribute called "area" that defaults to 0.0
    # - Add an attribute called "perimeter" that defaults to 0.0

    def __init__(self, radius):
        pass  # replace this with your code

    # Add a method called "calculate_area" that calculates the area of the circle
    # - The area should be stored in the class's "area" attribute
    # - The area of a circle is calculated using the formula (area = pi * radius^2)

    def calculate_area(self):
        pass  # replace this with your code

    # Add a method called "calculate_perimeter" that calculates the perimeter of the circle
    # - The perimeter should be stored in the class's "perimeter" attribute
    # - The perimeter of a circle is calculated using the formula (perimeter = 2 * pi * radius)

    def calculate_perimeter(self):
        pass  # replace this with your code


def main():
    user_radius = 1
    while user_radius > 0:
        user_radius = int(input("Enter the radius: "))
        user_circle = Circle(user_radius)
        # Call the calculate_area method
        # Call the calculate_perimeter method
        print("The area of the circle is: ", user_circle.area)
        print("The perimeter of the circle is: ", user_circle.perimeter)


if __name__ == "__main__":
    main()

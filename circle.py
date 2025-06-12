def calculate_circle_area(radius):
    """Calculate and return the area of a circle."""
    pi = 3.14159
    return pi * radius ** 2

def calculate_circle_perimeter(radius):
    """Calculate and return the perimeter (circumference) of a circle."""
    pi = 3.14159
    return 2 * pi * radius

def main():
    try:
        radius = float(input("Enter the radius of the circle: "))
        if radius < 0:
            print("Radius cannot be negative.")
            return

        area = calculate_circle_area(radius)
        perimeter = calculate_circle_perimeter(radius)

        print(f"Area of the circle: {area:.2f}")
        print(f"Perimeter (Circumference) of the circle: {perimeter:.2f}")

    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()
from triangle_package_v2 import triangle

def main():
    h = input("Enter hight of triangle: ")
    b = input("Enter base of triangle: ")
    print(triangle.calculate_area(h,b))

if __name__ == "__main__":
    main()
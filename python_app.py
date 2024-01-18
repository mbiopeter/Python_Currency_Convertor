def main():
    print("PYTHON CURRENCY CONVERTOR: DOLLEARS TO STERLING POUNDS")
    print()

    dollars = eval(input("Enter Amaunt In Dollears: "))

    pounds = convert_to_pounds(dollars)

    print("That is ", pounds, "Pounds")

convert_to_pounds = lambda dollars: dollars * 0.79

main()
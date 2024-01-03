def from_base_to_decimal(number, base):
    decimal_value = 0
    power = 0
    while number > 0:
        digit = number % 10
        if digit >= base:
            raise ValueError("Invalid digit in input number")
        decimal_value += digit * (base ** power)
        power += 1
        number //= 10
    return decimal_value
def from_decimal_to_base(number, base):
    if number == 0:
        return "0"
    output_digits = []
    while number > 0:
        digit = number % base
        output_digits.append(str(digit))
        number //= base
    output_digits.reverse()
    return "".join(output_digits)


def convert_number():
    number = input("Enter the number to convert: ")
    input_base = int(input("Enter the input base (between 2 and 16): "))
    if input_base < 2 or input_base > 16:
        print("Invalid input base")
        return
    try:
        decimal_value = from_base_to_decimal(int(number), input_base)
    except ValueError:
        print("Invalid digit in input number")
        return

    output_base = int(input("Enter the output base (between 2 and 16): "))
    if output_base < 2 or output_base > 16:
        print("Invalid output base")
        return

    output_number = from_decimal_to_base(decimal_value, output_base)

    print(f"{number} (base {input_base}) = {output_number} (base {output_base})")



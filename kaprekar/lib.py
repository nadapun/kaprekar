def try_me(four_digit_number):
    """
    Takes a 4 digit number whose digits are not all the same
    and prints the steps to return 6174, the Kaprekar number,
    as well as returning the number of steps.
    """
    if four_digit_number <= 0:
        print("Please input a positive 4 digit number.")
        return
    count = 0
    steps = []
    step = str(four_digit_number)
    if len(step) > 4:
        print("This number has too many digits.")
        return
    while step not in steps and count < 20 and step != "6174" and step != "0":
        steps.append(int(step))
        count += 1
        digits = [int(step[x]) for x in range(len(step))]
        digits.sort(reverse=True)
        while len(digits) < 4:
            digits.append(0)
        high = "".join(str(digits[x]) for x in range(len(digits)))
        digits.reverse()
        low = "".join(str(digits[x]) for x in range(len(digits)))
        next_step = int(high) - int(low)
        print(f"{count} :: {step} || {high} - {low} = {next_step}")
        step = str(next_step)
        if next_step == 0:
            print("This number does not reach the Kaprekar number.")

    if next_step == 0:
        print("Choose a different number with non-same digits.")
    elif count != 1:
        print(f"You reached 6174, the Kaprekar number, in {count} steps.")
        steps.append(int(step))
    else:
        print(f"You reached 6174, the Kaprekar number, in {count} step.")
        steps.append(int(step))
    return count, steps

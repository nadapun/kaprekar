def try_me(four_digit_number):
    """
    Takes a 4 digit number whose digits are not all the same
    and prints the steps to return 6174, the Kaprekar number,
    as well as returning the number of steps.
    """
    count = 0
    steps = []
    step = str(four_digit_number)
    while step not in steps and count < 20 and step != "6174":
        steps.append(step)
        count += 1
        digits = [int(step[x]) for x in range(len(step))]
        digits.sort(reverse=True)
        high = "".join(str(digits[x]) for x in range(len(digits)))
        digits.reverse()
        low = "".join(str(digits[x]) for x in range(len(digits)))
        next_step = int(high) - int(low)
        print(f"{count} :: {step} || {high} - {low} = {next_step}")
        step = str(next_step)
    if count != 1:
        print(f"You reached 6174, the Kaprekar number, in {count} steps.")
    else:
        print(f"You reached 6174, the Kaprekar number, in {count} step.")
    return count

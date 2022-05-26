# Answer: 232792560

# Find the number for 1 -> 20 because why not
for top in range(1, 20 + 1):
    print("For 1 to %d: " % top, end="")

    # Loop until we find a number divisible for 1 -> top
    highest_common_divisible = 0
    found_highest_common_divisible = False
    test_number = 0
    while not found_highest_common_divisible:
        test_number += 1

        # Test the divisibility of 1 -> top
        top_test_failed = False
        for i in range(1, top + 1):
            if test_number % i != 0:
                top_test_failed = True
                break

        if not top_test_failed:
            highest_common_divisible = test_number
            found_highest_common_divisible = True

    print(highest_common_divisible)

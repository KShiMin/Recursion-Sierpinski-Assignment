
seq = [2, 3, 5, 7, 8, 10, 15, 16, 23, 28]


def algo(seq, z):
    # last element index in the list
    n = len(seq) - 1

    for i in range(len(seq)):
        # Get the difference between wanted sum and last element in the list
        required_sum = z - int(seq[n])

        if required_sum in seq:
            return required_sum, seq[n], True
        elif n < i:
            return "Not Found", "Not Found", False
        else:
            n -= 1
            continue

    # Fail save
    return False


def main():
    z = 0
    try:
        z = int(input("Enter the sum for 2 digit you would like to check in seq: "))
    except ValueError:
        pass

    ans = algo(seq, z)
    print("X = " + str(ans[0]) + "\nY = " + str(ans[1]) + "\n" + str(ans[2]))


main()
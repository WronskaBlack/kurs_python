def is_lucky(serial):
    a = sum(map(int, serial[:3]))
    b = sum(map(int, serial[3:]))
    return a == b


def how_lucky():
    count = 0
    for i in range(10 ** 6):
        serial = str(i).zfill(6)
        if is_lucky(serial):
            count += 1
    return count


if __name__ == "__main__":
    print(how_lucky())

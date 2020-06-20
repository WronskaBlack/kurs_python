#from ..numbers import count_numbs   # doesn't work

def print_numbers(number):
    for i in range(number):
        print(i)


def print_names(names):
    for name in names:
        print(f"That's my name: {name}")

def main():
    print_numbers(4)


if __name__ == "__main__":
    main()
    count_numbs.print_numbers_v2()

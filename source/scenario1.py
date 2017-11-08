#!python
import sys


import strings

def one_time_route_cost_check(routes_file, numbers_file):
    """Clean up a file """
    routes = open(routes_file, "r")
    read_file = routes.read().split()
    read_file = list(map(lambda x: x.split(","), read_file))

    numbers = open(numbers_file, "r")
    numbers_read_file = numbers.read()

    return read_file


if __name__ == "__main__":
    print(one_time_route_cost_check("./Call_Routing/route-costs-100.txt", "./Call_Routing/phone-numbers-3.txt"))

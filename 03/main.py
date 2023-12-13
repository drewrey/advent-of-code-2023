import re

def read_data():
    lines = []
    with open('./input.txt') as f:
        lines = f.read().splitlines()
    return lines

fake_data = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""".strip("\n")

def find_symbol_locations(data):
    locations = []
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == "." or char.isdigit():
                pass
            else:
                locations.append((x, y))
    return locations

def find_possible_gears(data):
    possible_gears = []
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == "*":
                possible_gears.append((x, y))
    return possible_gears

def find_part_numbers(data, locations):
    part_numbers = []
    ranges_to_check = {}
    for x, y in locations:
        x_ranges_to_check = list(set([min(max(x + x0, 0), len(data[0]) - 1) for x0 in [-1, 0, 1]]))
        y_ranges_to_check = list(set([min(max(y + y0, 0), len(data) - 1) for y0 in [-1, 0, 1]]))
        for y0 in y_ranges_to_check:
            ranges_to_check[y0] = ranges_to_check.get(y0, set()).union(x_ranges_to_check)

    for y, line in enumerate(data):
        for match in re.finditer(r"\d+", line):
            match_span = set(range(*match.span()))
            if not match_span.isdisjoint(ranges_to_check.get(y, set())):
                part_numbers.append(match.group())
            
    return(part_numbers)

def find_gears(data, possible_gears):
    gear_ratios = []
    for x, y in possible_gears:
        x_ranges_to_check = list(set([min(max(x + x0, 0), len(data[0]) - 1) for x0 in [-1, 0, 1]]))
        y_ranges_to_check = list(set([min(max(y + y0, 0), len(data) - 1) for y0 in [-1, 0, 1]]))
        ranges_to_check = {}
        for y0 in y_ranges_to_check:
            ranges_to_check[y0] = ranges_to_check.get(y0, set()).union(x_ranges_to_check)

        possible_gear_ratios = []

        for y1, xs_in_y1 in ranges_to_check.items():
            line = data[y1]
            for match in re.finditer(r"\d+", line):
                match_span = set(range(*match.span()))
                if not match_span.isdisjoint(xs_in_y1):
                    possible_gear_ratios.append(match.group())
        if len(possible_gear_ratios) == 2:
            gear_ratios.append(possible_gear_ratios)
    return(gear_ratios)

if __name__ == "__main__":
    # data = fake_data.split("\n")
    data = read_data()
    # symbol_locations = find_symbol_locations(data)
    # part_numbers = find_part_numbers(data, symbol_locations)
    possible_gears = find_possible_gears(data)
    gears = find_gears(data, possible_gears)

    sum_of_gear_ratios = sum(int(x) * int(y) for x, y in gears)
    print(f"sum of gear ratios: {sum_of_gear_ratios}")
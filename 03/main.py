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


if __name__ == "__main__":
    # data = fake_data.split("\n")
    data = read_data()
    symbol_locations = find_symbol_locations(data)
    part_numbers = find_part_numbers(data, symbol_locations)
    print(f"sum of part numbers: {sum([int(x) for x in part_numbers])}")
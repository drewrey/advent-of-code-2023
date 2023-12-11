written_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def read_data():
    lines = []
    with open('./input.txt') as f:
        lines = f.readlines()
    
    return lines
def fake_data(part = 2):
    if part == 1:
        data = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
    if part ==2:
        data = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]
    return data

def find_calibration_value(line):
    first, last = 0, 0
    for i in range(len(line)):
        if first == 0:
            if line[i].isdigit():
                first = line[i]
            else:
                for name in written_digits:
                    if line[i:].startswith(name):
                        first = str(written_digits.index(name) + 1)
                        print(f"Found {name} at {i}")
                        break
        elif line[i].isdigit():
            last = line[i]
        else:
            for name in written_digits:
                if line[i:].startswith(name):
                    last = str(written_digits.index(name) + 1)
                    print(f"Found {name} at {i}")
                    break
    if last == 0:
        last = first
    return int(first + last)

if __name__ == "__main__":
    print("Hello World!")
    data = read_data()
    # data = fake_data()
    total_calibration_value = 0
    for line in data:
        total_calibration_value += find_calibration_value(line)
    
    print(f"Total Calibration Value: {total_calibration_value}")
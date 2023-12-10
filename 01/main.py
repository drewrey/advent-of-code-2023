
def read_data():
    lines = []
    with open('./input.txt') as f:
        lines = f.readlines()
    
    return lines
def fake_data():
    return ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]

def find_calibration_value(line):
    first, last = 0, 0
    for i in range(len(line)):
        if first == 0 and line[i].isdigit():
            first = line[i]
        elif line[i].isdigit():
            last = line[i]
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
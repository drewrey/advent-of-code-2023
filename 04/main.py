def read_data():
    lines = []
    with open('./input.txt') as f:
        lines = f.read().splitlines()
    return lines

fake_data = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".strip("\n").split("\n")

def parse_card(line):
    card, numbers = line.split(": ")
    card_number = int(card.split()[1])

    winning_numbers, my_numbers = numbers.split(" | ")
    winning_numbers = set([int(x) for x in winning_numbers.split()])
    my_numbers = [int(x) for x in my_numbers.split()]

    print(f"Card {card_number}: winning numbers: {winning_numbers}")
    print(f"Card {card_number}: my numbers: {my_numbers}")
    
    my_winning_numbers = [x for x in my_numbers if x in winning_numbers]

    if my_winning_numbers == []:
        point_value = 0
    else:
        point_value = 2**(len(my_winning_numbers) - 1)

    return {"card_number": card_number, "my_winning_numbers": my_winning_numbers, "point_value": point_value}
    


if __name__ == "__main__":
    print("Hello World!")
    data = read_data()
    # data = fake_data
    print(data)
    parsed_cards = []
    for line in data:
        parsed_cards.append(parse_card(line))
    
    sum_of_points = sum([card["point_value"] for card in parsed_cards])

    print(f"Sum of points: {sum_of_points}")
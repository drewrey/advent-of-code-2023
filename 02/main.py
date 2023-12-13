def read_data():
    lines = []
    with open('./input.txt') as f:
        lines = f.read().splitlines()
    return lines

def fake_data():
   return ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]

def parse_game(line):
    game, draws = line.split(": ")
    _, game_number = game.split("Game ")
    draws = [x.split(', ') for x in draws.split("; ")]
    tmp = []
    for i, draw in enumerate(draws):
        tmp.append({})
        for color_draw in draw:
            number, color = color_draw.split(" ")
            tmp[i][color] = int(number)
    return {"game_number": int(game_number), "draws": tmp}

def determine_if_possible(game, total_dice):
    is_possible = True
    for draw in game["draws"]:
        for color, count in draw.items():
            if count > total_dice[color]:
                is_possible = False
    return {"game_number": game['game_number'], "is_possible": is_possible}

def compute_power(game):
    needed_dice = {"red": 0, "green": 0, "blue": 0}
    for draw in game["draws"]:
        for color, count in draw.items():
            if count > needed_dice[color]:
                needed_dice[color] = count
    return needed_dice['red'] * needed_dice['green'] * needed_dice['blue']

def parse_games(lines):
    games = []
    for line in lines:
        games.append(parse_game(line))
    return games


if __name__ == "__main__":
    print("Hello World!")
    data = read_data()
    # data = fake_data()

    total_dice = {"red": 12, "green": 13, "blue": 14}
    parsed_games = parse_games(data)
    possibile_games = [determine_if_possible(game, total_dice) for game in parsed_games]
    powers = [compute_power(game) for game in parsed_games]
    print(powers)
    sum_of_powers = sum(powers)
    
    print(f"Sum of possible games: {sum_of_powers}")
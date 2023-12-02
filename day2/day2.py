
LIMITS = {
    "red": 12,
    "green":13,
    "blue": 14
}
with open("input.txt") as f:
    lines = f.readlines()
    res = 0
    for line in lines:
        game, rest = line.split(":")
        _, game_id = game.split(" ")
        subsets = rest.split(";")

        is_impossible = False
        for subset in subsets:
            subset = subset.strip()
            color_pairs = subset.split(",")
            for number, color in map(lambda x: x.strip().split(" "), color_pairs):
                if int(number) > LIMITS[color]:
                    is_impossible = True
                    break
            if is_impossible: break
        
        if not is_impossible:
            res += int(game_id)

    print(f"P1: {res}")

with open("input.txt") as f:
    lines = f.readlines()
    res = 0
    for line in lines:
        game, rest = line.split(":")
        _, game_id = game.split(" ")
        subsets = rest.split(";")

        is_impossible = False
        min_needed = {
            "red": 0,
            "green":0,
            "blue": 0
        }
        for subset in subsets:
            subset = subset.strip()
            color_pairs = subset.split(",")
            for number, color in map(lambda x: x.strip().split(" "), color_pairs):
                min_needed[color] = max(int(number), min_needed[color])

        power = min_needed["red"] * min_needed["green"] * min_needed["blue"]
        res += power
    print(f"P2: {res}")
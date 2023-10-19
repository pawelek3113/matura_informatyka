# wybieramy jedna najdrozsza pilke i jedna pare najdrozszych butow
shoes_n_balls: list[int] = []
with open("sport.txt", "r", encoding="UTF-8") as file:
    shoes_n_balls = [int(item) for item in file.read().split()]

bal: int = 20_000

shoes: list[int] = shoes_n_balls[:999]
balls: list[int] = shoes_n_balls[1000:]

shoes.sort()
balls.sort()


affordable_kit: list[int] = []
for shoe in shoes:
    for ball in balls:
        kit = shoe + ball
        if kit < bal:
            affordable_kit.append(kit)

print(max(affordable_kit))

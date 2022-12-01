
def main():
    f = open('day1.txt', 'r')
    lines = [line.strip('\n') for line in f]
    part1(lines)
    part2(lines)

def part1(lines):
    maxCalories = 0
    currCalories = []
    for idx, calorie in enumerate(lines):
        if calorie == '' or idx == len(lines) - 1:
            calories = sum(currCalories)
            maxCalories = max(maxCalories, calories)
            currCalories = []
        else:
            currCalories.append(int(calorie))
    print(maxCalories)

def part2(lines):
    calorieGroups = []
    currCalories = []
    for idx, calorie in enumerate(lines):
        if calorie == '' or idx == len(lines) - 1:
            calories = sum(currCalories)
            calorieGroups.append(calories)
            currCalories = []
        else:
            currCalories.append(int(calorie))
    calorieGroups = list(sorted(calorieGroups, reverse=True))
    top3Sum = sum(calorieGroups[:3])
    print(top3Sum)

if __name__ == '__main__':
    main()
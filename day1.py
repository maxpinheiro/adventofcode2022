
def main():
    f = open('day1.txt', 'r')
    lines = [line.strip('\n') for line in f]
    calorieGroups = []
    currCalories = 0
    for idx, calorie in enumerate(lines):
        if calorie == '' or idx == len(lines) - 1:
            calorieGroups.append(currCalories)
            currCalories = 0
        else:
            currCalories += int(calorie)
    calorieGroups.sort(reverse=True)
    maxCalories = calorieGroups[0]
    print(maxCalories)
    top3Sum = sum(calorieGroups[:3])
    print(top3Sum)

if __name__ == '__main__':
    main()
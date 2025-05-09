# Use this file to create dummy data to be read in by the neural network
# Ideally uses realistic data rather than random
import random


def main():
    gold = 50
    gov = 0
    num_cities = 0
    tech_level = 0
    num_allies = 0
    num_enemies = 7
    enemies_near = 0

    f = open("TurnData.txt", "w+")

    for i in range(300):
        if i < 100:
            gold = gold + random.randint(0, 5)
            if (i % 15 == 0) and gold > 200:
                gold -= 200
            f.write(str(gold) + ",")
            if (i > 25) and (gov == 0):
                gov = random.randint(0, 1)
            if (i > 50) and ((gov == 0) or (gov == 1)):
                gov = random.randint(1, 2)
            f.write(str(gov) + ",")
            if (i % 15) == 0:
                num_cities += 1
            f.write(str(num_cities) + ",")
            if i % 5 == 0:
                tech_level += 1
            f.write(str(tech_level) + ",")
            if (i % 75 == 0) and (i != 0):
                num_allies += 1
            f.write(str(num_allies) + ",")
            num_enemies = 7 - num_allies
            f.write(str(num_enemies) + ",")
            if (i % 40 == 0) and (i != 0):
                enemies_near = 1
            if (i % 45 == 0) and (i != 0):
                enemies_near = 0
            f.write(str(enemies_near))

        if (i >= 100) and (i < 200):
            gold = gold + random.randint(5, 15)
            if (i % 15 == 0) and gold > 300:
                gold -= 300
            f.write(str(gold) + ",")
            if (i > 100) and ((gov == 0) or (gov == 1) or (gov == 2)):
                gov = random.randint(1, 3)
            f.write(str(gov) + ",")
            if i % 25 == 0:
                num_cities += 1
            f.write(str(num_cities) + ",")
            if i % 5 == 0:
                tech_level += 1
            f.write(str(tech_level) + ",")
            if i % 75 == 0:
                num_allies += 1
            f.write(str(num_allies) + ",")
            num_enemies = 7 - num_allies
            f.write(str(num_enemies) + ",")
            if (i > 150) and (i < 165):
                enemies_near = 1
            else:
                enemies_near = 0
            f.write(str(enemies_near))

        if (i >= 200) and (i <= 300):
            gold = gold + random.randint(15, 30)
            if (i % 15 == 0) and gold > 400:
                gold -= 400
            f.write(str(gold) + ",")
            gov = random.randint(1, 4)
            f.write(str(gov) + ",")
            if i % 50 == 0:
                num_cities += 1
            f.write(str(num_cities) + ",")
            if i % 5 == 0:
                tech_level += 1
            f.write(str(tech_level) + ",")
            f.write(str(num_allies) + ",")
            num_enemies = 7 - num_allies
            f.write(str(num_enemies) + ",")
            if (i >= 250) and (i < 265):
                enemies_near = 1
            else:
                enemies_near = 0
            f.write(str(enemies_near))
        f.write("\n")
    f.close()


if __name__ == "__main__":
    main()

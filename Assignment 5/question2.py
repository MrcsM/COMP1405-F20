from math import sqrt

def euclidean_distance(distance1, distance2):
    #sqrt((x2-x1)^2+(y2-y1)^2) rounded to 2 decimals - Dec 4th 2020 (9:19pm)
    return round(sqrt(((distance2[0]-distance1[0])**2)+((distance2[1]-distance1[1])**2)), 2)

def closest_enemies(hero_position, enemy_positions):
    e_positions = list()
    for pos in enemy_positions:
        e_positions.append(euclidean_distance(hero_position, pos)) #works properly - Dec 4th 2020 (11:24pm)
    #Start of Cocktail Sort - Dec 4th 2020 (11:24pm)
    swapped = True
    start = 0
    end = len(e_positions) - 1
    while swapped == True:
        swapped = False
        for i in range(start, end):
            if (e_positions[i] > e_positions[i+1]):
                e_positions[i], e_positions[i+1] = e_positions[i+1], e_positions[i]
                swapped = True
        if swapped == False:
            break
        swapped = False
        end = end - 1
        for i in range(end-1, start-1, -1):
            if (e_positions[i] > e_positions[i+1]):
                e_positions[i], e_positions[i+1] = e_positions[i+1], e_positions[i]
                swapped = True
        start = start + 1
    #End of Cocktail Sort - Dec 4th 2020 (11:32pm)
    return(e_positions)


if __name__ == "__main__":
    hero_position = (50, 10)
    enemy_positions = [(10, 20), (55, 10), (23, -5), (0, 200)]
    print("Hero Position: " + str(hero_position) + " & Enemy Positions: " + str(enemy_positions))
    print("Sorted distances: \n" + str(closest_enemies(hero_position, enemy_positions)))

#question 2 finished - Dec 4th 2020 (11:42pm)
from collections import defaultdict


def card_to_value(card):
    if card == "A":
        return 14
    elif card == "K":
        return 13
    elif card == "Q":
        return 12
    elif card == "J":
        return 11
    elif card == "T":
        return 10
    else:
        return int(card)


def card_to_value_p2(card):
    if card == "A":
        return 14
    elif card == "K":
        return 13
    elif card == "Q":
        return 12
    elif card == "J":
        return 1
    elif card == "T":
        return 10
    else:
        return int(card)



def score_hand(a):
    cd = defaultdict(lambda: 0)
    for card in a:
        cd[card] += 1

    counts = {1: 0, 2:0, 3:0, 4:0, 5:0}
    for card, num in cd.items():
        counts[num] += 1

    if counts[5] == 1:
        score = 15**11
    elif counts[4] == 1:
        score = 15**10
    elif counts[3] == 1 and counts[2] == 1:
        score = 15**9
    elif counts[3] == 1:
        score = 15**8
    elif counts[2] == 2:
        score = 15**7
    elif counts[2] == 1:
        score = 15**6
    else:
        score = 0

    for i, card in enumerate(reversed(a)):
        score += card_to_value(card) * (15**((i+1)))

    return score


def score_hand_p2(a):
    cd = defaultdict(lambda: 0)
    for card in a:
        cd[card] += 1

    counts = {1: 0, 2:0, 3:0, 4:0, 5:0}
    jokers = 0
    for card, num in cd.items():
        if card == "J":
            jokers = num
        else:
            counts[num] += 1

    if counts[5] == 1 or (counts[4] == 1 and jokers == 1) or (counts[3] == 1 and jokers == 2) or (counts[2] == 1 and jokers == 3) or jokers >= 4: 
        score = 15**11
    elif counts[4] == 1 or (counts[3] == 1 and jokers == 1) or (counts[2] == 1 and jokers == 2) or jokers == 3:
        score = 15**10
    elif (counts[3] == 1 and counts[2] == 1) or (counts[2] == 2 and jokers == 1) or (counts[3] == 1 and jokers == 1) or (counts[2] == 1 and jokers == 2) or jokers == 3:
        score = 15**9
    elif counts[3] == 1 or (counts[2] == 1 and jokers == 1) or jokers == 2:
        score = 15**8
    elif counts[2] == 2 or (counts[2] == 1 and jokers == 1) or jokers == 2:
        score = 15**7
    elif counts[2] == 1 or jokers == 1:
        score = 15**6
    else:
        score = 0

    for i, card in enumerate(reversed(a)):
        score += card_to_value_p2(card) * (15**((i+1)))

    return score
        

def part1(fname="day7_input.txt"):
    with open(fname, 'r') as f:
        lines = f.readlines()
        handbets = []
        for line in lines:
            hand, bet = line[:-1].split(" ")[:2]
            handbets.append((score_hand(hand), hand, int(bet)))

    handbets.sort(key=lambda x: x[0], reverse=False)

    winnings = 0
    for i, hb in enumerate(handbets):
        winnings += (i+1)*hb[2]
    return winnings


def part2(fname="day7_input.txt"):
    with open(fname, 'r') as f:
        lines = f.readlines()
        handbets = []
        for line in lines:
            hand, bet = line[:-1].split(" ")[:2]
            handbets.append((score_hand_p2(hand), hand, int(bet)))

    handbets.sort(key=lambda x: x[0], reverse=False)


    winnings = 0
    for i, hb in enumerate(handbets):
        winnings += (i+1)*hb[2]
    return winnings


print(part1("day7_test.txt"))
#print(part1("day7_test2.txt"))
#print(part1("day7_test3.txt"))
print(part1("day7_input.txt"))
print(part2("day7_test.txt"))
print(part2("day7_input.txt"))

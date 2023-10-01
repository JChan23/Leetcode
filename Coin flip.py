import random


def gamblers_ruin(p, j, N, rounds):
    #p = probability of winning the coin flip
    #j = gambler's starting money
    #N = gambler's goal/target
    #round = number of rounds (round ends when money=N or money=0)
    
    wins = 0 #win counter
    for u in range(rounds):
        done = False
        money = j
        while not done:
            x = random.uniform(0, 1) #picks random decimal dumber between 0 and 1
            #logic for this selection: let's say p=0.5. There is a 50% chance the number generated is >p and a 50% chance the number is <p. The chances change depending on how large p is.
            if x < p:
                money = money + 1
            else:
                money = money - 1

            if money == 0 or money == N:
                done = True
        if money == N:
            wins = wins + 1
    return wins/rounds #win rate = wins/rounds played


print(f'Coin flip win rate: {gamblers_ruin(0.5, 50, 100, 10000)*100}%')

import random

def lottery_sim(my_picks, num_tickets):
    ticket = 1
    winners = {3:0,4:0,5:0,6:0}
    for i in range(num_tickets):
        ticket+=1
        drawing = random.sample(range(1, 53), 6)
        correct = 0
        for i in my_picks:
            if i in drawing:
                correct+=1
        if correct == 3:
            winners[3]+=1

        elif correct == 4:
            winners[4]+=1

        elif correct == 5:
            winners[5]+=1
            
        elif correct == 6:
            winners[6]+=1
        
    return winners

lottery_sim([17,3,44,22,15,37], 100000)
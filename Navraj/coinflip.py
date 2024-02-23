
import random

def coin():
    return random.choice(["Heads", "Tails"])

def game():
    numgames = int(input("How many games? "))
    numflips = int(input("How many coin tosses per game? "))

    totalwinA =0
    totalwinB =0
    totalwinC =0

    for gamenum in range(numgames):
        winA = 0
        winB = 0
        winC = 0

        for y in range(numflips):
            result1 = coin()
            result2 = coin()

            if result1 == "Heads" and result2 == "Heads":
                winA +=1
            elif result1 =="Tails" and result2 == "Tails":
                winB += 1
            else:
                winC += 1
                
        if winA > winB and winA > winC:
            totalwinA +=1 
        elif winB > winA and winB > winC:
            totalwinB +=1
        else: 
            totalwinC +=1

        print(f"Games {gamenum+1}: ")
        print(f" Group A: {winA} ({winA / numflips * 100:.1f}%); "
              f" Group B: {winB} ({winB / numflips * 100:.1f}%); "
              f" Prof: {winC} ({winC / numflips * 100:.1f})")
        
        

    print(f"\nWins: Group A={totalwinA} ({(totalwinA / numgames) * 100:.1f}%); "
          f" Group B= {totalwinB} ({(totalwinB / numgames) * 100:.1f}%); "
          f" prof = {totalwinC} ({(totalwinC / numgames) * 100:.1f}%)")

game()       



   
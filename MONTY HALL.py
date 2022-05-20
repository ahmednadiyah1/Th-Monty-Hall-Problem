import random

def chooseCar(n):
    p=random.randint(1,n)
    return p

def displayZonks(n,p,choose):
    print("You chose door ", choose)
    options, new_range=list(), list()
    new_range=[x for x in range(1,n+1) if x!=p and x!=choose]
    for j in range(n-2):
         options.append(random.choice(new_range))
         random.shuffle(new_range)
         print('The Zonk is: ', options[j])
    return options

def playAgain():
    print("Do you want to play again: ")
    return input().lower().startswith('y')

ntrials=int(input("Enter Number of trials: "))
n = input("How many doors: ")
p = chooseCar(int(n))
nwins_without_switch=0
nwins_with_switch=0
n_trial=ntrials
while(ntrials!=0):
    choose=int(input("Chose a car: "))
    options= displayZonks(int(n),p,int(choose))
    second_choice=int(input("switch or stick? "))
    if second_choice==p and choose==p:
       print("You have won the car!")
       nwins_without_switch+=1
    elif second_choice==p and choose!=p:
        print("You have won the car!")
        nwins_with_switch+=1
    else:
       print('The car is in door ',p," better luck next time")
    ntrials-=1

print("Proportions of wins with switching is {}".format(nwins_with_switch/n_trial) )
print("Proportions of wins without switching is {}".format(nwins_without_switch/n_trial) )





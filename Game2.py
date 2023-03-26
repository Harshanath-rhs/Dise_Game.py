import random
urupees=100
mrupees=1000
dummy=1

while (dummy!=2):

    if (urupees==0):
        print ("You lost all your money. I won the game!! Game over!")
        break
    elif (mrupees==0):
        print("Woh! I lost all my money. You won the game. Game over! You won", urupees, "Rupees. Congratulations!")
        break
    else:
        print("I have", mrupees, "rupees in my hand and you have", urupees, "rupees in your hand.")
        bet=input("How much do you bet? ")

        try:
            bet=float(bet)
        except:
            bet=-1
    
        if (bet<=0):
            print("Wrong input. Please correct it")
        elif(bet>urupees):
            print("you dont have that much of money. Correct it. You have only", urupees, "rupees in your hand")
        elif(bet>mrupees):
            print("I dont have that much of money to bet. I have only", mrupees, "rupees. Please reduce the bet")

        else:
            print("you bet", bet, "rupees. what is your expectation?")
            gside=str(input("less or more? (type 'less' for 1,2,3 and type 'more' for 4,5,6.):"))
            more="more"
            less="less"
            dise=random.randrange(1,7)
    
            if (gside!=less):

                if (gside!=more):
                    print("Rong input. Please check the spellings. Type correctly 'less' or 'more' with lower cast letter")
                else:
                    if (dise==4 or dise==5 or dise==6):
                        print("Wow! you won. The dise gives", dise)
                        urupees=bet+urupees
                        mrupees=mrupees-bet
                    
                    else:
                        print("you bet", bet, "rupees for higher values of dise. but the dise gave",dise)
                        print ("you lost", bet, "rupees")
                        urupees=urupees-bet
                        mrupees=mrupees+bet
            else:
                if (dise==1 or dise==2 or dise==3):
                    print("Wow! you won. The dise gives", dise)
                    urupees=bet+urupees
                    mrupees=mrupees-bet
                else:
                    print ("you bet", bet, "rupees for lower values of dise. but the dise gave",dise)
                    print ("you lost", bet, "rupees")
                    urupees=urupees-bet
                    mrupees=mrupees+bet
    
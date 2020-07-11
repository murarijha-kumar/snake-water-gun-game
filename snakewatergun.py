import random
#snake water gun
ch=0
w1=0
w2=0
while(ch<10):
    ch+=1
    n=input("enter the option to choose from snake water gun-")
    t=random.choice(["snake","water","gun"])
    print(f"computer choose-{t}")
    if(n==t):
        print("No point given for this as both have same choose ")
        print(f"chances left before game over-{10-ch}")
        continue
    elif(n=="snake" and t=="water"):
        w1+=1
        print(f"chances left before game over-{10-ch}")
    elif (n == "snake" and t == "gun"):
        w2 += 1
        print(f"chances left before game over-{10-ch}")
    elif (n == "water" and t == "snake"):
        w2 += 1
        print(f"chances left before game over-{10-ch}")
    elif (n == "water" and t == "gun"):
        w1 += 1
        print(f"chances left before game over-{10-ch}")
    elif (n == "gun" and t == "snake"):
        w1 += 1
        print(f"chances left before game over-{10-ch}")
    elif (n == "gun" and t == "water"):
        w2 += 1
        print(f"chances left before game over-{10-ch}")

if(w1>w2):
    print("user won the match")
    print("score of user-",w1)
    print("score of computer-",w2)
elif(w1<w2):
    print("computer won the match")
    print("score of computer-",w2)
    print("score of user-",w1)
else:
    print("game draw")





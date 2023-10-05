import random

print("WELCOME TO THE GAME OF CASINO")
print("\n")
print("You Have Only 5 Chanses to gusse the Number")

print("Choose any Lower Number")
L=int(input())

print("Choose any Higher Number")
H=int(input())

R=random.randrange(L,H)

                       
for i in range(5):
    print("Enter Your Number")
    User=int(input())
    
    print("Your Number = ",User)

    if User==R:
        print("|Congratulations You Win|")
        print("|These is Your Price|")
        break
    elif User<R:
        print("Enter Larger Number")
        
    else:
        print("Enter Smaller Number")
    print("You Have Ony",5-i-1,"Chances Left!")

print("Thanks For Playing Please Come Again")



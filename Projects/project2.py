Basketball_points = 0
Soccer_points = 0
Chill_points = 0

input("please answer all questions in capital letters!")
answer1 = input("Do you prefer A teamwork, B points, or C food?   ")
if answer1 == "A":
    Basketball_points += 1
elif answer1 == "B":
    Soccer_points += 1
elif answer1 == "C":
    Chill_points += 1

answer2 = input("Is your favorite Season A Summer, B Winter, or C Fall?   ")
if answer2 == "A":
    Soccer_points += 1
    Basketball_points += 1
elif answer2 == "B":
    Chill_points += 2
elif answer2 == "C":
    Basketball_points += 2

answer3 = input("Would you rather A go and play after practice, B don't go to practice, or C go and play hard during practice?")
if answer3 == "A":
    Basketball_points += 4
elif answer3 == "B":
    Chill_points += 3
elif answer3 == "C":
     Soccer_points += 3
     Basketball_points += 3

answer4 = input("Would you rather A go to the Fahbbes party, B Not go to the Fahbbes party, or C Start a rebellion agianst the Fahbbes party?")
if answer4 == "A":
    Basketball_points += 5
elif answer4 == "B":
    Soccer_points += 4
elif answer4 == "C":
    Soccer_points += 4
    Chill_points += 4

answer5 = input("Would you rather A get cooked Henry in a 1v1, B cook Henry in a 1v1, or C dont even play the 1v1?")
if answer5 == "A":
    Soccer_points += 4.5
elif answer5 == "B":
    Basketball_points += 6
elif answer5 == "C":
    Chill_points += 5

print(f"Your score is {Basketball_points} Basketball, {Soccer_points} Soccer, and {Chill_points} No sport yet")

if Basketball_points > Soccer_points and Basketball_points > Chill_points:
    print("your sport is Basketball")
elif Soccer_points > Basketball_points and Soccer_points > Chill_points:
    print("your sport is Soccer")
elif Chill_points > Basketball_points and Chill_points > Soccer_points:
    print("you dont have a sport")

# end of quiz 

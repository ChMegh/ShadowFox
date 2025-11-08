# Task 5: For Loops

print("-------- Program 1: Dice Rolling --------")
import random

rolls = []
count_6 = 0
count_1 = 0
two_6_in_row = 0

for i in range(20):
    r = random.randint(1, 6)
    rolls.append(r)
    if r == 6:
        count_6 += 1
    if r == 1:
        count_1 += 1

for i in range(len(rolls) - 1):
    if rolls[i] == 6 and rolls[i + 1] == 6:
        two_6_in_row += 1

print("Dice Rolls:", rolls)
print("Number of 6s:", count_6)
print("Number of 1s:", count_1)
print("Two 6s in a row:", two_6_in_row)

print("\n-------- Program 2: Jumping Jacks --------")

total = 100
done = 0

while done < total:
    done += 10
    print("Completed:", done, "jumping jacks")

    if done == total:
        print("Congratulations! You completed the workout")
        break

    tired = input("Are you tired? (yes/no): ")

    if tired.lower() in ["yes", "y"]:
        skip = input("Do you want to skip remaining sets? (yes/no): ")
        if skip.lower() in ["yes", "y"]:
            print("You completed a total of", done, "jumping jacks")
            break
    else:
        print("Remaining:", total - done)

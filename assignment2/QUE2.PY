#i
score=(45,89,5,76,45,4,89,92,58,45)
num=max(score)
print("highest score :",num)
print(" at index :",score.index(num))
#ii
num2=min(score)
print("lowest score :",num2)
print(" count=",score.count(num2))
#iii
reversed_score=list(reversed(score))
print("reversed score :",reversed_score)
#iv
sp_score=float(input("enter score to search"))
if sp_score in score:
    print(f"score {sp_score} found at index {score.index(sp_score)}")
else:
    print("specific score not found")


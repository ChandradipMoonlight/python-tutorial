
# traffic light code

color = input("color : ");

if(color.casefold == "green"):
    print("GO");
elif(color=="yellow"):
    print("LOOK");
elif(color=="red"):
    print("STOP");
else:
    print("traffic light is broken");

# ternary operator / single line if statement

food = input("food : ");

testOfFood = "sweet" if food == "cake" or food == "jalebi" else  "Not sweet";
print("Test of food : ", testOfFood);

# OR

print("sweet") if food == "cake" or food == "jelebi" else print("not sweet");

# cleaver if operator / ternary operator 

# syntax => (FalseValue, TrueValue) [Condition];

age = int(input("Age : "));

vote = ("Yes", "No") [age<18]
print("eligibleForVote : ", vote);


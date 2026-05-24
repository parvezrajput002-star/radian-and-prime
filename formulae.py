print("if Seconds exist then Enter Seconds to manage the equation !") 
User = input("Enter Seconds / No :") 
user = User.lower()

try:
    if user.isdigit():
        raise ValueError("do not enter integers !")
except ValueError as v:
    print("Enter only Seconds / No ")
    
    
if user == "seconds": 
    try: 
        Degree = int(input("Enter Degree Number :")) 
        Minute = int(input("Enter Minute Number :"))
        Seconds = int(input("Enter Seconds :")) 
    except ValueError as v : 
        print("Boss Enter only Numbers !")
    
    Equation = f"equation = {Degree}° + {Minute}′ + {Seconds}′′" 
    print(Equation) 
    print(" -- Solving --") 
    def solve(Degree , Minute , Seconds):
        Seconds_Answer = Seconds / 60
        Minute_Seconds = Minute + Seconds_Answer
        Minute_into_Degree = Minute_Seconds / 60 
        Answer= Degree + Minute_into_Degree 
        return Answer
    Answer = solve(Degree , Minute , Seconds) 
    print(f"your answer : {Answer}") 
elif user == "no": 
    try:
        Degree = int(input("Enter Degree Number :")) 
        Minute = int(input("Enter Minute Number :"))
    except ValueError as v : print("Boss Enter only Numbers !") 
    Equation = f"Equation = {Degree}° + {Minute}′" 
    print(Equation) 
    print(" -- Solving --")
    def solve(Degree , Minute): 
        Minute_answer = Minute / 60 
        Answer = Degree + Minute_answer 
        return Answer 
    Answer = solve(Degree , Minute) 
    print(f"your answer : {Answer}")
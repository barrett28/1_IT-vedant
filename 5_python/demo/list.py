letters = [
    ['g', 'a', 'r', 'd', 'e', 'n'],
    ['c', 'o', 'm', 'p', 'u', 't', 'e', 'r'],
    ['s', 'c', 'h', 'o', 'o', 'l'],
    ['t', 'r', 'a', 'i', 'n', 'i', 'n', 'g'],
    ['c', 'h', 'a', 'l', 'l', 'e', 'n', 'g', 'e']
]

words = [
    ["and", "age", "den", "ran", "red", "gear", "rage", "dare", "garden"], 
    ["to", "me", "up", "cut", "core", "mute", "cure", "computer"],          
    ["so", "ho", "cool", "loch", "solo", "school"],                         
    ["tin", "ran", "rain", "train", "giant", "rating", "training"],         
    ["can", "hen", "all", "call", "lean", "angle", "challenge"]             
]


lives, level, score = 5,0,0

while level<5:
    print(f"you are playing level: {level+1}")
    
    for c in letters[level]:
        print(f"{c}", end="\t")
    print()
    
    wordcount = 0
    enteredword = [] 
    
    while wordcount<3:
        word = input("enter word: ").lower()
        
        if word in words[level]:
            if word not in enteredword:
                enteredword.append(word)
                score +=1
                wordcount +=1
                print(f"correct {enteredword}")
            else:
                print("you repeated the word, choose something different")
        else:
            print("Wrong guess")
            lives -=1
            print(f"lives renaining: {lives}")
            
        if lives==0:
            print("better luck next time")
            print(f"your score is: {score}")
            exit()
        
    if level==4:
        print("Congrats you completed the game")
        print(f"your score is: {score}")
        break
    else:
        choice = input("do you want to enter another level y/n?: ")
        if choice.lower()[0]=="y":
            level +=1
        else:
            print("thanks for playing the game")
            print("your final score is {score}")
            exit()

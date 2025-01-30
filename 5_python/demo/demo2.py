# letters = [
#     ['g', 'a', 'r', 'd', 'e', 'n'],
#     ['c', 'o', 'm', 'p', 'u', 't', 'e', 'r'],
#     ['s', 'c', 'h', 'o', 'o', 'l'],
#     ['t', 'r', 'a', 'i', 'n', 'i', 'n', 'g'],
#     ['c', 'h', 'a', 'l', 'l', 'e', 'n', 'g', 'e']
# ]

# words = [
#     ["and", "age", "den", "ran", "red", "gear", "rage", "dare", "garden"], 
#     ["to", "me", "up", "cut", "core", "mute", "cure", "computer"],          
#     ["so", "ho", "cool", "loch", "solo", "school"],                         
#     ["tin", "ran", "rain", "train", "giant", "rating", "training"],         
#     ["can", "hen", "all", "call", "lean", "angle", "challenge"]             
# ]

# lives, level, score = 5,0,0

# while level<5:
#     print(f"This is your level: {level+1}")
    
#     print("Enter three words which shuold match the words in the list")
    
#     for c in letters[level]:
#         print(f"{c}", end="\t")
        
#         # print()
        
#     wordcount = 0
#     enteredwordlist=[]
        
#     while wordcount==0 or wordcount<3:
#         print()
#         word = input("enter the word to check if you are correct or not : ")
        
#         if not(word.lower() in enteredwordlist):
            
#             # print(word)
#             enteredwordlist.append(word)
            
#             print(enteredwordlist)
            
#         for w in words[level]:
#             if (word.lower()==w):
#                 wordcount +=1
#                 score +=1
#                 oldword = word
#                 break
                
#         if word.lower() not in words[level]:
#             print("wrong guess")
#             lives -=1
#             print("lives remain: ",lives)
            
#         if lives==0:
#             print("Game Over!, You are out")
#             print(f"Your score is {score}")
#             break
        
#     wordCount = 0
#     word = ''

#     if lives == 0:

#         break

#     if level == 4:

#         print('Thanks for playing the game!!!')

#         print(f"Your Final score is {score}")

#         level += 1

#     else:

#         choice = input('Do you want to continue to next level? (y/n) ')

#         if(choice.lower()[0] == 'y'):

#             level += 1

#         else:

#             print('Thanks for playing the game!!!')

#             print('Your score is {}'.format(score))

#             break                



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

lives, level, score = 5, 0, 0

while level < 5:
    print(f"This is your level: {level+1}")
    print("Enter three words that should match the words in the list:")

    # Show letters available
    for c in letters[level]:
        print(f"{c}", end="\t")
    print()

    wordcount = 0
    enteredwordlist = []

    while wordcount < 3:
        print()
        word = input("Enter a word: ").lower()

        if word in words[level]:  
            if word not in enteredwordlist:  # Prevent duplicate words
                enteredwordlist.append(word)
                wordcount += 1
                score += 1
                print(f"Correct! Words found: {wordcount}/3")
            else:
                print("You've already entered this word. Try a different one!")
        else:
            print("Wrong guess!")
            lives -= 1
            print(f"Lives remaining: {lives}")

        if lives == 0:
            print("\nGame Over! You ran out of lives.")
            print(f"Your final score is {score}")
            exit()

    if level == 4:
        print("\nCongratulations! You've completed all levels!")
        print(f"Your final score is {score}")
        break
    else:
        choice = input("\nDo you want to continue to the next level? (y/n): ")
        if choice.lower()[0] == 'y':
            level += 1
        else:
            print("\nThanks for playing the game!")
            print(f"Your final score is {score}")
            break

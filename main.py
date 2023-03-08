def minion_game(string): #Define the minion_game function
  vowels = 'AEIOU'
  kevin_score = 0
  stuart_score = 0

  for i in range(len(string)):# Iterate through all possible substrings of the input string
    
    if string[i] in vowels:# If the first letter of the substring is a vowel, add the number of possible substrings to Kevin's score
        kevin_score += (len(string)-i)
    else:# If the first letter of the substring is a consonant, add the number of possible substrings to Stuart's score
        stuart_score += (len(string)-i)

  if kevin_score > stuart_score:# Determine the winner or if it is a tie
    print("Kevin", kevin_score)
  elif stuart_score > kevin_score:
    print("Stuart", stuart_score)
  else:
    print("Draw")

if __name__ == '__main__':# input from keybord
    print("Enter the word for the contest:" )
    s = input()
    minion_game(s)

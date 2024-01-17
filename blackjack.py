import random

def deal_card(cards_deck): 
    dealt_card = random.choice(cards)    
    return dealt_card

def calculate_score(list_of_cards):
    score = sum(list_of_cards)
    return score        
       
def is_black_jack(list_of_cards):
    return len(list_of_cards) == 2 and 10 in (list_of_cards) and 11 in list_of_cards      


while True:
    play_game = input("Do you want to play a game of Blackjack? 'y' or 'n'? ")
    print()
    
    if play_game == 'y':

        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        player_cards = []
        computer_cards = []


        while len(player_cards) < 2 and len(computer_cards) < 2:
                dealt_card = deal_card(cards) 
                player_cards.append(dealt_card) 
                computer_card = deal_card(cards)         
                computer_cards.append(computer_card) 
    
        while True:        
            print(f"Your cards: {player_cards}. ")              
            player_score = calculate_score(player_cards)
                
            if is_black_jack(player_cards):
                print(f"Your score is {player_score}. It's Black Jack, you win!")
                break

            if player_score > 21 and 11 in player_cards:
                player_cards.remove(11)
                player_cards.append(1)            
                    
            player_score = calculate_score(player_cards)        
            computer_score = calculate_score(computer_cards) 
   
            print(f"Your current score: {player_score}. ")
            print()
            print(f"Computer first card: {computer_cards[0]}.")
            print()
    
   
            if player_score > 21:    
                break         
            else:
                another_card = input("Type 'y' for another card, 'no' to pass.  ")
                if another_card == 'y':
                    player_cards.append(deal_card(cards))
                    print()
                else: 
                    print(f"Your final cards: {player_cards}. Your final score: {player_score}.")
                    break
            
        while True: 
            if is_black_jack(player_cards):        
                break              
            
            computer_score = calculate_score(computer_cards)
            
            if is_black_jack(computer_cards):
                print(f"Computer score is {computer_score}. It's a Black Jack! Computer wins. ")
                break
    
            if computer_score > 21:
                if 11 in computer_cards:
                    computer_cards.remove(11)
                    computer_cards.append(1)
            computer_score = calculate_score(computer_cards)
            
            if player_score > 21:
                print(f"Your final hand: {player_cards}. Your final score: {player_score}. \nComputer final hand: {computer_cards}. Computer final score : {computer_score}. You went over, computer wins. ")
                break
            elif computer_score > 21:
                print(f"Computer final hand: {computer_cards}. Computer final score : {computer_score}.\nComputer went over, you win. ")
                break        
            else:    
                while computer_score < 17:
                    computer_cards.append(deal_card(cards))
                    computer_score = calculate_score(computer_cards)
                    if 11 in computer_cards:
                        computer_cards.remove(11)
                        computer_cards.append(1)
                        computer_score = calculate_score(computer_cards)
            
                print(f"Computer final hand: {computer_cards}, computer final score: {computer_score}.")
        
    
            if player_score <= 21 and computer_score <= 21:
                if 21 - player_score < 21 - computer_score:
                   print("You win.")
                   break
                elif 21 - player_score > 21 - computer_score:
                   print("Computer wins.")
                   break
                elif player_score == computer_score:
                    print("It's a draw")
                    break
            elif player_score <= 21 and computer_score > 21:
                print("You win.")
                break
            else:
                print("It's a draw.")
                break
    else:
        break
   

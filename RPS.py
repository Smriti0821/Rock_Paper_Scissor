import random

def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissor"])

def play_round(player, computer):
    if player == computer:
        return "Draw"
    elif (player == "Rock" and computer == "Scissor") or \
         (player == "Paper" and computer == "Rock") or \
         (player == "Scissor" and computer == "Paper"):
        return "You Won!!"
    else:
        return "You lose!!"

def main():
    player_point = 0
    computer_point = 0

    number = int(input("No. of times you want to play: "))

    for _ in range(number):
        player = input("Enter your Choice like Rock or Paper or Scissor: ").capitalize()
        computer = get_computer_choice()

        print(f"Computer has chosen: {computer}")

        result = play_round(player, computer)
        print(result)

        if result == "You Won!!":
            player_point += 1
        elif result == "You lose!!":
            computer_point += 1

    print(f"Your score out of {number} is: {player_point}")
    print(f"Computer's score out of {number} is: {computer_point}")

    if player_point > computer_point:
        print("Hurrayy!! You Won")
    elif player_point == computer_point:
        print("It's a draw!!")
    else:
        print("Ohhoo!! You Lose")

if __name__ == "__main__":
    main()

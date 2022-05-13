import random


class Player:

    score_player = 0
    score_computer = 0

    def __init__(self):
        self.human_player_move = None
        self.computer_move = None

    def learn(self, human_player_move, computer_move):
        self.human_player_move = human_player_move
        self.computer_move = computer_move


class RepeatRock(Player):
    def move(self):
        return 'rock'


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()
        self.bombers = "Human"

    def move(self):
        while True:
            move = input("Ready, steady, go!)"
                         "(Rock, Paper, Scissors)").lower()
            if move in moves:
                return move
            else:
                print("Oops you typed the wrong thing.")


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):
    def move(self):
        if self.computer_move is None:
            return random.choice(moves)
        else:
            return self.computer_move


class CyclePlayer(Player):
    def move(self):
        if self.human_player_move is None:
            return random.choice(moves)
        else:
            change = moves.index(self.human_player_move)+1
            if change == len(moves):
                change = 0
            return moves[change]


def beats(p1move, p2move):
    return ((p1move == 'rock' and p2move == 'scissors') or
            (p1move == 'scissors' and p2move == 'paper') or
            (p1move == 'paper' and p2move == 'rock'))


class Game:
    def __init__(self, Player1, Player2):
        self.p1 = Player1
        self.p2 = Player2
        self.score_player = 0
        self.score_computer = 0

    def play_round(self):
        p1move = self.p1.move()
        p2move = self.p2.move()
        print(f"Player 1: {p1move}  Player 2: {p2move}")
        if beats(p1move, p2move):
            self.score_player += 1
            print("I won!")
        elif p1move == p2move:
            print("Its a Tie!")
        else:
            self.score_computer += 1
            print("You lose!")
        self.p1.learn(p1move, p2move)
        self.p2.learn(p2move, p1move)
        print(f"Player 1: {self.score_player} | "
              f"Player 2: {self.score_computer}")

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round +1}:")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    moves = ['rock', 'paper', 'scissors']
    bombers = {
        "repeat": RepeatRock(),
        "human": HumanPlayer(),
        "random": RandomPlayer(),
        "reflect": ReflectPlayer(),
        "cycle": CyclePlayer()
    }

    while True:
        print("Bazinga!")
        possiblities = input("Pick your bomber!"
                             "repeat, human, random, reflect, cycle)").lower()
        if possiblities in bombers:
            game = Game(bombers["human"], bombers[possiblities])
            game.play_game()
        else:
            print("Nice pick!")

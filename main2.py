import random;

print('Rock-Paper-Scissors Game');
print('\n');
print('\n');
print('There are two players for this game: You the, player, and Computer the second player');

print('\n');
print('\n');

print('You are selecting from the list of options below:');

print('\n');
print('\n');

print('Options \n 1. Rock (R)  \n  2. Scissors (S)   \n    3. Paper (P)');
print('\n');

print('********************The rule is**********************');


print('\n');

print('If Rock beats Scissors or Paper beats Rock or Scissors beats Paper, there is a win');
print('You can choose to be a pair of Scissors, a Rock, or a Paper by selecting form the options S, R, and P respectively');
print('If you and computer picks the same character, its a tie');
print('If for instance you select R (a Rock) and the computer picks a P (a Paper), then the computer wins');

print('\n');
print('\n');

opt = ['R', 'P', 'S'];
print('The list of options to pick from is:   ', opt);

player = input('Kindly pick an option between R, P, and S from the list above: ');

for i in range(1):
    if player not in opt:
        print('an error');
        print('Option not on the list');
        print('\n');


        player = input('Kindly pick an option between R, P, and S from the list above: ');
        while player not in opt:
            print('\n');
            player = input('Kindly pick an option between R, P, and S from the list above: ');
            print('\n');
        if player in opt:
            print('Your option is on the list')
            print('\n');

            cpuls = random.choice(['R', 'P', 'S']);
            print('The cpu option is:   ', cpuls);
            print('\n');


            if player == 'S' and cpuls == 'S':
                print('Player(Scissors): CPU(Scissors)');
                print('Its a tie');
                print('\n');

                player = input('Kindly pick an option between R, P, and S from the list above: ');
                print('\n');
                cpuls = random.choice(['R', 'P', 'S']);
                print('The cpu option is:   ', cpuls);
                print('\n');

                if player == 'R' and cpuls == 'S':
                    print('Player(Rock): CPU(Scissors)');
                    print('You win');
                    print('Game completed');
                    print('\n');
                elif player == 'S' and cpuls == 'R':
                    print('Player(Scissors): CPU(Rock)');
                    print('CPU wins');
                    print('Game completed');
                    print('\n');
                elif player == 'P' and cpuls == 'R':
                    print('Player(Paper): CPU(Rock)');
                    print('You win');
                    print('Game completed');
                    print('\n');
                elif player == 'R' and cpuls == 'P':
                    print('Player(Rock): CPU(Paper)');
                    print('CPU wins');
                    print('Game completed');
                    print('\n');
                elif player == 'S' and cpuls == 'P':
                    print('Player(Scissors): CPU(Paper)');
                    print('You win');
                    print('Game completed');
                    print('\n');
                else:
                    #player == 'P' and cpuls == 'S':
                    print('Player(Paper): CPU(Scissors)');
                    print('CPU wins');
                    print('Game completed');
                    print('\n');

            elif player == 'R' and cpuls == 'R':
                print('Player(Rock): CPU(Rock)');
                print('Its a tie');
                print('\n');
                player = input('Kindly pick an option between R, P, and S from the list above: ');
                print('\n');
                cpuls = random.choice(['R', 'P', 'S']);
                print('The cpu option is:   ', cpuls);
                print('\n');

                if player == 'R' and cpuls == 'S':
                    print('Player(Rock): CPU(Scissors)');
                    print('You win');
                    print('Game completed');
                    print('\n');
                elif player == 'S' and cpuls == 'R':
                    print('Player(Scissors): CPU(Rock)');
                    print('CPU wins');
                    print('Game completed');
                    print('\n');
                elif player == 'P' and cpuls == 'R':
                    print('Player(Paper): CPU(Rock)');
                    print('You win');
                    print('Game completed');
                    print('\n');
                elif player == 'R' and cpuls == 'P':
                    print('Player(Rock): CPU(Paper)');
                    print('CPU wins');
                    print('Game completed');
                    print('\n');
                elif player == 'S' and cpuls == 'P':
                    print('Player(Scissors): CPU(Paper)');
                    print('You win');
                    print('Game completed');
                    print('\n');
                else:
                    #player == 'P' and cpuls == 'S':
                    print('Player(Paper): CPU(Scissors)');
                    print('CPU wins');
                    print('Game completed');
                    print('\n');
     
            elif player == 'P' and cpuls == 'P':
                print('Player(Paper): CPU(Paper)');
                print('Its a tie');
                print('\n');
                player = input('Kindly pick an option between R, P, and S from the list above: ');
                print('\n');
                cpuls = random.choice(['R', 'P', 'S']);
                print('The cpu option is:   ', cpuls);
                print('\n');

                if player == 'R' and cpuls == 'S':
                    print('Player(Rock): CPU(Scissors)');
                    print('You win');
                    print('Game completed');
                    print('\n');
                elif player == 'S' and cpuls == 'R':
                    print('Player(Scissors): CPU(Rock)');
                    print('CPU wins');
                    print('Game completed');
                    print('\n');
                elif player == 'P' and cpuls == 'R':
                    print('Player(Paper): CPU(Rock)');
                    print('You win');
                    print('Game completed');
                    print('\n');
                elif player == 'R' and cpuls == 'P':
                    print('Player(Rock): CPU(Paper)');
                    print('CPU wins');
                    print('Game completed');
                    print('\n');
                elif player == 'S' and cpuls == 'P':
                    print('Player(Scissors): CPU(Paper)');
                    print('You win');
                    print('Game completed');
                    print('\n');
                else:
                    #player == 'P' and cpuls == 'S':
                    print('Player(Paper): CPU(Scissors)');
                    print('CPU wins');
                    print('Game completed');
                    print('\n');

            else:
                if player == 'R' and cpuls == 'S':
                    print('Player(Rock): CPU(Scissors)');
                    print('You win');
                    print('Game completed');
                    print('\n');
                elif player == 'S' and cpuls == 'R':
                    print('Player(Scissors): CPU(Rock)');
                    print('CPU wins');
                    print('Game completed');
                    print('\n');
                elif player == 'P' and cpuls == 'R':
                    print('Player(Paper): CPU(Rock)');
                    print('You win');
                    print('Game completed');
                    print('\n');
                elif player == 'R' and cpuls == 'P':
                    print('Player(Rock): CPU(Paper)');
                    print('CPU wins');
                    print('Game completed');
                    print('\n');
                elif player == 'S' and cpuls == 'P':
                    print('Player(Scissors): CPU(Paper)');
                    print('You win');
                    print('Game completed');
                    print('\n');
                else:
                    #player == 'P' and cpuls == 'S':
                    print('Player(Paper): CPU(Scissors)');
                    print('CPU wins');
                    print('Game completed');
                    print('\n');
            
    else:
        cpuls = random.choice(['R', 'P', 'S']);
        print('The cpu option is:   ', cpuls);
        print('\n');

        if player == 'S' and cpuls == 'S':
            print('Player(Scissors): CPU(Scissors)');
            print('Its a tie');
            print('\n');
            player = input('Kindly pick an option between R, P, and S from the list above: ');
            print('\n');
            if player == 'R' and cpuls == 'S':
                print('Player(Rock): CPU(Scissors)');
                print('You win');
                print('Game completed');
                print('\n');
            elif player == 'S' and cpuls == 'R':
                print('Player(Scissors): CPU(Rock)');
                print('CPU wins');
                print('Game completed');
                print('\n');
            elif player == 'P' and cpuls == 'R':
                print('Player(Paper): CPU(Rock)');
                print('You win');
                print('Game completed');
                print('\n');
            elif player == 'R' and cpuls == 'P':
                print('Player(Rock): CPU(Paper)');
                print('CPU wins');
                print('Game completed');
                print('\n');
            elif player == 'S' and cpuls == 'P':
                print('Player(Scissors): CPU(Paper)');
                print('You win');
                print('Game completed');
                print('\n');
            else:
                #player == 'P' and cpuls == 'S':
                print('Player(Paper): CPU(Scissors)');
                print('CPU wins');
                print('Game completed');
                print('\n');

        elif player == 'R' and cpuls == 'R':
            print('Player(Rock): CPU(Rock)');
            print('Its a tie');
            print('\n');
            player = input('Kindly pick an option between R, P, and S from the list above: ');
            print('\n');
            
            if player == 'R' and cpuls == 'S':
                print('Player(Rock): CPU(Scissors)');
                print('You win');
                print('Game completed');
                print('\n');
            elif player == 'S' and cpuls == 'R':
                print('Player(Scissors): CPU(Rock)');
                print('CPU wins');
                print('Game completed');
                print('\n');
            elif player == 'P' and cpuls == 'R':
                print('Player(Paper): CPU(Rock)');
                print('You win');
                print('Game completed');
                print('\n');
            elif player == 'R' and cpuls == 'P':
                print('Player(Rock): CPU(Paper)');
                print('CPU wins');
                print('Game completed');
                print('\n');
            elif player == 'S' and cpuls == 'P':
                print('Player(Scissors): CPU(Paper)');
                print('You win');
                print('Game completed');
                print('\n');
            else:
                #player == 'P' and cpuls == 'S':
                print('Player(Paper): CPU(Scissors)');
                print('CPU wins');
                print('Game completed');
                print('\n');
     
        elif player == 'P' and cpuls == 'P':
            print('Player(Paper): CPU(Paper)');
            print('Its a tie');
            print('\n');
            player = input('Kindly pick an option between R, P, and S from the list above: ');
            print('\n');

            if player == 'R' and cpuls == 'S':
                print('Player(Rock): CPU(Scissors)');
                print('You win');
                print('Game completed');
                print('\n');
            elif player == 'S' and cpuls == 'R':
                print('Player(Scissors): CPU(Rock)');
                print('CPU wins');
                print('Game completed');
                print('\n');
            elif player == 'P' and cpuls == 'R':
                print('Player(Paper): CPU(Rock)');
                print('You win');
                print('Game completed');
                print('\n');
            elif player == 'R' and cpuls == 'P':
                print('Player(Rock): CPU(Paper)');
                print('CPU wins');
                print('Game completed');
                print('\n');
            elif player == 'S' and cpuls == 'P':
                print('Player(Scissors): CPU(Paper)');
                print('You win');
                print('Game completed');
                print('\n');
            else:
                #player == 'P' and cpuls == 'S':
                print('Player(Paper): CPU(Scissors)');
                print('CPU wins');
                print('Game completed');
                print('\n');

        else:
            if player == 'R' and cpuls == 'S':
                print('Player(Rock): CPU(Scissors)');
                print('You win');
                print('Game completed');
                print('\n');
            elif player == 'S' and cpuls == 'R':
                print('Player(Scissors): CPU(Rock)');
                print('CPU wins');
                print('Game completed');
                print('\n');
            elif player == 'P' and cpuls == 'R':
                print('Player(Paper): CPU(Rock)');
                print('You win');
                print('Game completed');
                print('\n');
            elif player == 'R' and cpuls == 'P':
                print('Player(Rock): CPU(Paper)');
                print('CPU wins');
                print('Game completed');
                print('\n');
            elif player == 'S' and cpuls == 'P':
                print('Player(Scissors): CPU(Paper)');
                print('You win');
                print('Game completed');
                print('\n');
            else:
                #player == 'P' and cpuls == 'S':
                print('Player(Paper): CPU(Scissors)');
                print('CPU wins');
                print('Game completed');
                print('\n');
        
        
    



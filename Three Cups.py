import random

my_list=['','0','']
def shuffled_list():
    random.shuffle(my_list)
    return my_list



def user_guess():
    guess = ''
    while guess not in ['0','1' or '2']:
        guess = int(input('Enter the position of ball  0 or 1 or 2:'))
        return(int(guess))



def check_guess(my_list,guess):
    if my_list[guess]=='0':
        print("You won!")
    else:
        print('You Lost! Keep Trying...')





#game begins


shuff_list = shuffled_list()
player_input = user_guess()
check_gue_ss= check_guess(shuff_list,player_input)
print(my_list)



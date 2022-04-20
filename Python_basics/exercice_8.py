from random import sample

lotto_numbers = sample(range(49+1), 6)
lotto_numbers.sort()



def lotto():
    """Get numbers from user.

        Compare with lotto numbers.

        :return: Information how many numbers did the player got right
        """
    good_numbers = False
    while not good_numbers:
        try:
            a = int(input("Give 1st number: "))
            b = int(input("Give 2nd number: "))
            c = int(input("Give 3rd number: "))
            d = int(input("Give 4th number: "))
            e = int(input("Give 5th number: "))
            f = int(input("Give 6th number: "))
            player_numbers = [a, b, c, d, e, f]
            player_numbers.sort()
        except ValueError:
            print("It's not a number")
            continue
        for number in player_numbers:
            if number not in range(1, 50):
                print("Give a number from 1 to 49")
                break
        if len(player_numbers) != len(set(player_numbers)):
            print("You gave the same number twice")
        else:
            good_numbers = True


            print(f'You numbers are : {player_numbers}')
            print(f'Lotto numbers are: {lotto_numbers}')

            combined_numbers = player_numbers + lotto_numbers
            guessed_numbers = len(combined_numbers) - len(set(combined_numbers))

            print(f'You got {guessed_numbers} numbers right')


lotto()



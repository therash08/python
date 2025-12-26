import random

jackpot = random.randint(1, 100)
guess = int(input("Guess koro (1-100): "))
counter = 1

while guess != jackpot:
    if guess < jackpot:
        print('Wrong number! Guess HIGHER.')
    else:
        # এখানে 'lower' হবে কারণ গেস করা নাম্বারটি জ্যাকপটের চেয়ে বড়
        print('Wrong number! Guess LOWER.')

    guess = int(input("Abar guess koro: "))
    counter += 1

print('Correct guess!')
print('Total attempts:', counter)

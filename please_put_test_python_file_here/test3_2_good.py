#3.2 lower_case_with_underscores? (snake-case)
import random
ONE = 1
TWO = 2

def main():
    foo_test()

def foo_test():
    orange_apple = random.randint(1, 3)
    if orange_apple < 3:
        orange_apple += 1
    if ONE:
        orange_apple = TWO - ONE
        orange_apple = TWO + ONE
    return orange_apple

main()

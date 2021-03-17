#   Purpose and version of program
# Required for random insertions for no bias.
from exit_with_q_module import quit_program
from license_input import *

__purpose__ = "This program utilizes Miller's test to find whether a number is prime (with a probalistic chance of error) and to determine whether a number is not prime (with absolute certainty)."
import random

__version__ = "Program Version: 1.0"

#   License and Author
__author__ = "Faycal Kilali"
__copyright__ = "Copyright (C) 2021 Faycal Kilali"
__license__ = "GNU GENERAL PUBLIC LICENSE"
__license_version__ = "3.0"

#   Display purpose and version, license and version of license.
print(__purpose__, "\n", __version__)
print(__copyright__, "\n", __license__, __license_version__, "\n")

# Importing License disclaimer and extra details input

reveal_license_options()

# Importing exit implementation


def DisplayError(ErrorNumber):
    if ErrorNumber == 0:
        print("Please follow the directions in the program")
    elif ErrorNumber == 1:
        print(
            "Illogical input: the number of coprime integers that you've plugged in is more than the possible coprime integers that are smaller than the prime number we are checking for primality."
        )
    elif ErrorNumber == 2:
        print("Input is not an integer, will not perform computation.")
    elif ErrorNumber == 3:
        print(
            "The numbers to check for primality need to be odd positive integers larger than or equal to 3."
        )


list_of_found_primes = []

# print("The coprime integers to test against reduce the probalistic chance of the integer we are testing for primality erroneously passing the test. If k is the amount of coprime integers we want to check against, then the chance of the integer we are checking for primality erroneously passing the test is less than (1/4) to the power of k \nYou may type 'primes' if you wish to see the list of primes you've found so far during this current session, each time you find a prime it is appended to that list of primes.")
show_details = input(
    "Would you like to see the details of every computation? input 1 if you wish to, otherwise just hit enter: "
)


def compute_primes(arg):
    n, k = 0, 0
    string_n = input("Input an integer to check for primality: ")
    if string_n == "primes":
        print(
            "The list of primes you've found so far during this session is: %s"
            % list_of_found_primes
        )
    elif string_n == "q":
        quit_program()
    string_k = input(
        "Input the strength of the test (1 = decent chance of error, 4+ very unlikely to have any chance of error) the larger the input, the longer the computation will take: "
    )
    if string_k == "primes":
        print(
            "The list of primes you've found so far during this session is: %s"
            % list_of_found_primes
        )
    elif string_k == "q":
        quit_program()
    try:
        n = int(string_n)
        k = int(string_k)
    except ValueError:
        DisplayError(2)
    if n % 2 == 0 or n == 1:
        DisplayError(3)
    elif n - 1 > k > 0:
        # Find all factors of 2 of (n-1), we do this now instead of later for optimization purposes.
        x = 1
        factors_of_2 = 0
        while (n - 1) % (2 * x) == 0:
            factors_of_2 += 1
            x = x * 2
        # Choose k integers coprime to n and smaller than n but still positive.
        KIntegersChosenAtRandom = random.sample(
            range(2, n), k
        )  # Randomly inserts k random numbers between n-1 and 2 (inclusive of endpoints) into a list with no repeats.
        chosen_at_random = 0
        g = 0
        bases_passed = 0
        while chosen_at_random < k and g != "not prime":
            chosen_at_random += 1
            b = KIntegersChosenAtRandom.pop(
                0
            )  # Pop command returns value of index it deletes, so in this case we are assigning the value we removed to b
            t = 1
            count_congruence_to_1 = 0
            iterated_over_factors_of_2 = 0
            while iterated_over_factors_of_2 <= factors_of_2:
                iterated_over_factors_of_2 += 1
                if ((b ** ((n - 1) // (t))) % n) == (n - 1):
                    if arg == "1":
                        print(
                            "%d passes miller's test with base %d, because %d^%d mod %d gives remainder %d"
                            % (
                                n,
                                b,
                                b,
                                (n - 1) // (t),
                                n,
                                ((b ** ((n - 1) // (t))) % n),
                            )
                        )
                    else:
                        bases_passed += 1
                        print(
                            "%d passed miller's test with %d coprime integers out of %d."
                            % (n, bases_passed, k)
                        )
                    iterated_over_factors_of_2 = factors_of_2 + 1  # Forces a stop
                elif ((b ** ((n - 1) // (t))) % n) == 1:
                    count_congruence_to_1 += 1
                    if count_congruence_to_1 == (factors_of_2 + 1):
                        if arg == "1":
                            print(
                                "%d passes miller's test with base %d, because %d to the power of f, where f is of the form %d/(2 to the power of i) and i can be any number between 0 and the count of how many copies of the factors of 2 that %d contains in its product, inclusive of the endpoints."
                                % (n, b, b, (n - 1), (n - 1))
                            )
                        else:
                            bases_passed += 1
                            print(
                                "%d passed miller's test with %d coprime integers out of %d."
                                % (n, bases_passed, k)
                            )
                else:
                    print(
                        "%d is not prime with absolute certainty, since %d^%d mod %d is congruent to %d."
                        % (n, b, (n - 1) // (t), n, ((b ** ((n - 1) // (t))) % n))
                    )
                    g = "not prime"
                    iterated_over_factors_of_2 = factors_of_2 + 1  # Forces a stop
                t = t * 2
        if not g == "not prime":
            print(
                n,
                "is prime with more than {:.10%}".format(1 - (1 / 4) ** k),
                "chance of a correct deduction.",
            )
            if not n in list_of_found_primes:
                list_of_found_primes.append(n)
    else:
        DisplayError(1)
    compute_primes(show_details)


compute_primes(show_details)

# sys module to better organize the module directory
import sys

sys.path.append("Modules")

from Modules import license_input
from Modules import exit_with_q_module
from Modules import primality_tester_impl

#   Purpose and version of program
__purpose__ = "This program utilizes Miller's test to find whether a number is prime (with a probalistic chance of error) and to determine whether a number is not prime (with absolute certainty)."
__version__ = "Program Version: 1.0"

#   License and Author
__author__ = "Faycal Kilali"
__copyright__ = "Copyright (C) 2021 Faycal Kilali"
__license__ = "GNU GENERAL PUBLIC LICENSE"
__license_version__ = "3.0"

#   Display purpose and version, license and version of license.
print(__purpose__, "\n", __version__)
print(__copyright__, "\n", __license__, __license_version__, "\n")

# License disclaimer and extra details input
license_input.reveal_license_options()


show_details = "1"
show_details = input(
    "Would you like to see the details of every computation? input 0 for result only (default), 1 for minimal details, 2 for full details: "
)


def interface():
    prime_input = input("Input an integer to check for primality: ")
    if prime_input == "primes":
        print(
            "The list of primes you've found so far during this session is: %s"
            % list_of_found_primes
        )
    elif prime_input == "q":
        exit_with_q_module.quit_program()
    coprime_sample = input(
        "Input the strength of the test (1 = decent chance of error, 4+ very unlikely to have any chance of error) the larger the input, the longer the computation will take: "
    )
    if coprime_sample == "primes":
        print(
            "The list of primes you've found so far during this session is: %s"
            % list_of_found_primes
        )
    elif coprime_sample == "q":
        exit_with_q_module.quit_program()
    else:
        primality_tester_impl.primality_tester(
            show_details, prime_input, coprime_sample
        )
    interface()


interface()

import argparse
from multiprocessing import Pool
import io
import os
import time
from typing import List, Tuple
import colorama
import random  # Added for random leetspeak selection
import dictionaries

colorama.init(autoreset=True)

LEET_DICT = dictionaries.leetspeak_dict
SUFFIXES = dictionaries.suffixes

# Function to display how the script works
def display_how_script_works():
    print(f"""
{colorama.Fore.YELLOW}HOW SCRIPT WORKS?
{colorama.Fore.GREEN}+ This script will take a file input which is a password list
+ Then it will apply leetspeak transformations to characters. For example: the character 'a' can become '@' or '4'.
+ It will also append common suffixes at the end.
+ The original passwords will also be preserved in the output.
+ Check the file dictionaries.py to understand more about the leetspeak transformations and suffixes.
{colorama.Style.RESET_ALL}
""")

# Function to return wordlist based on leetspeak transformations
def generate_wordlist(word_and_level: Tuple[str, int]) -> List[str]:
    wordlist = []
    word, level = word_and_level

    capitalized = word.capitalize()
    uppered = word.upper()
    swapcased = word.swapcase()
    capswapcased = capitalized.swapcase()

    def add_to_wordlist(key: int, word_variant: str) -> None:
        leeted_words = ''.join(
            [random.choice(LEET_DICT[key].get(x.lower(), [x])) if x.lower() in LEET_DICT[key] else x for x in word_variant]
        )
        wordlist.append(leeted_words)

    if level >= 0:
        wordlist.extend([word, capitalized, uppered, swapcased, capswapcased])
    if level > 1:
        add_to_wordlist(1, word)
    if level > 3:
        add_to_wordlist(1, swapcased)
    if level > 5:
        add_to_wordlist(1, capitalized)
    if level > 7:
        add_to_wordlist(1, capswapcased)

    return wordlist

# Function to generate lines from the input passlist
def generate_lines(source: io.TextIOWrapper, level: int) -> List[Tuple[str, int]]:
    favored_number_ranges = [
        range(24),
        range(50, 99, 10),
    ]

    word_variants = []

    for wrd in set(map(str.strip, map(str.lower, source))):
        for suffix in SUFFIXES:
            word_variants.append(wrd + suffix)

        for favored_range in favored_number_ranges:
            for number in favored_range:
                word_variants.append(wrd + "0" + str(number))
                word_variants.append(wrd + str(number))

        for i in range(1970, 2015):
            word_variants.append(wrd + str(i))

    lines = [(word_variant, level) for word_variant in set(word_variants)]
    return lines

# Function to munge the passwords
def munge(args: argparse.Namespace) -> None:
    if args.verbose:
        start = time.time()

    # Read the original password list from the input file (combinations.txt)
    with io.open(args.input, "r", encoding="utf-8", errors="ignore") as source:
        original_passwords = [line.strip() for line in source.readlines()]

    # Generate leetspeak transformations and variants
    with io.open(args.input, "r", encoding="utf-8", errors="ignore") as source:
        lines = generate_lines(source, args.level)

    wordlist = []
    with Pool() as pool:
        results = pool.imap_unordered(generate_wordlist, lines, chunksize=10000)
        for item in results:
            wordlist.extend(item)

    setted = list(set(list(wordlist)))

    if not args.output:
        filename, file_extension = os.path.splitext(args.input)
        args.output = f"{filename}_munged{file_extension}"

    # Append both original passwords and munged passwords to the output file
    with open(args.output, "a", encoding="utf-8", errors="ignore") as out:
        # Write original passwords first
        for word in original_passwords:
            out.write(word + "\n")
        
        # Write leetspeak-transformed passwords
        for word in setted:
            out.write(word.strip().replace(" ", "") + "\n")

    if args.verbose:
        settled_len = len(setted)
        print(
            colorama.Fore.GREEN
            + f"GENERATED {settled_len} passwords IN {str(int(time.time() - start))} seconds\n"
            + f"Output file -> {args.output}\n"
            + f"Level       -> {args.level}\n"
            + f"Verbose     -> {args.verbose}"
        )

# Custom error handler to display epilog (example)
class CustomArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        print(f"{colorama.Fore.RED}[!] Error: {message}{colorama.Style.RESET_ALL}")
        self.print_help()  # Print the help (usage and epilog)
        self.exit(2)

# Main function to handle argument parsing
if __name__ == "__main__":
    display_how_script_works()  # Show how the script works before parsing args

    parser = CustomArgumentParser(description="Generate variations of passwords")
    
    # Custom usage and example message
    parser.usage = f"{colorama.Fore.RED}[!] Usage: <script-name> -i <file-combination> -o <output> -l <level>{colorama.Style.RESET_ALL}"
    parser.epilog = f"{colorama.Fore.RED}[!] Example: <script-name> -i combinations.txt -o passwd_list.txt -l 8{colorama.Style.RESET_ALL}"
    
    parser.add_argument("-i", "--input", type=str, required=True, help="Passlist input file")
    parser.add_argument("-o", "--output", type=str, help="Munged passlist output file")
    parser.add_argument("-l", "--level", type=int, help="Level [0-8] (default 5)", default=5)
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Whether to print verbose output or not", default=False)

    arguments = parser.parse_args()

    # Check for valid level input
    if arguments.level > 8:
        print(f"{colorama.Fore.RED}[!] Error: Maximum level is 8.{colorama.Style.RESET_ALL}")
        parser.print_help()
        exit(1)

    # Run the munge function
    munge(arguments)

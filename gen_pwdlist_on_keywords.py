import itertools
import colorama
from colorama import Fore, Style
import os

colorama.init(autoreset=True)

# Function to display how the script works
def display_how_it_works():
    print(f"""
{Fore.YELLOW}HOW THIS SCRIPT WORKS:
{Fore.GREEN}+ Generates a list of passwords (combinations.txt) based on keyword combinations.
+ Ensures combinations end with only a valid word or number.
→ No special characters will be at the end.

{Fore.YELLOW}WHY NO SPECIAL CHARS AT THE END?
{Fore.GREEN}+ The generated combinations.txt will be used by munge.py, which also adds the most common suffixes at the end.
→ For more details, check dictionaries.py.
{Style.RESET_ALL}
""")

# Function to return lowercase, capitalized, and uppercase versions of the word
def generate_variants(word):
    if word.isalpha():  # If the word contains only alphabetic characters
        return [word.lower(), word.capitalize(), word.upper()]
    else:
        return [word]  # For non-alphabetic characters, just return the original

# Function to filter out combinations that end with special characters
def is_valid_combination(combination):
    # Ensure that the last word is not a special character
    return combination[-1].isalpha() or combination[-1].isdigit()

# Get user input for keywords
def get_keywords():
    # Display the prompt only once
    print(f"{Fore.CYAN}[+] Please provide the keywords, it could be a word, number, or special chars, and separate them by commas.")
    print(f"{Fore.CYAN}[+] Ex: du, cloud, 2023, 2024, @, `, ~")
    
    all_keywords = []
    
    while True:
        user_input = input(Fore.YELLOW + "[+] Enter your keywords: ").strip()
        
        if not user_input:
            print(Fore.RED + "[!] Please enter some keywords.")
            continue
        
        # Split the input by commas, remove extra spaces, and ensure no empty strings
        keywords = [word.strip() for word in user_input.split(',') if word.strip()]
        all_keywords.extend(keywords)
        
        # Force valid input for the "Do you want to add more?" question
        while True:
            more_input = input(Fore.YELLOW + "[?] Do you want to add more? [1] Yes [2] No: ").strip().lower()
            if more_input in ['no', 'n', '2']:  # Stop if user chooses 'no' or '2'
                return list(dict.fromkeys(all_keywords))  # Remove duplicates and return
            elif more_input in ['yes', 'y', '1']:  # Continue if user chooses 'yes' or '1'
                break
            else:
                print(Fore.RED + "[!] Invalid input, please choose either '1' (Yes) or '2' (No).")

def main():
    # Display the explanation before the script runs
    display_how_it_works()
    
    # Get keywords from the user
    keywords = get_keywords()

    # Display the final keywords list before proceeding
    print(f"{Fore.GREEN}[+] Final list of keywords: {keywords}")
    
    # Open a file to save the combinations
    output_file = "combinations.txt"
    with open(output_file, "w") as f:
        # Generate permutations of length 3 and 4
        for length in range(3, 5):
            combinations = itertools.permutations(keywords, length)
            for combination in combinations:
                if is_valid_combination(combination):  # Ensure no special character at the end
                    # Generate variants for each word in the combination
                    variants = [generate_variants(word) for word in combination]
                    # Create all possible combinations of lowercase/capitalized/uppercase versions
                    for variant_combination in itertools.product(*variants):
                        f.write(''.join(variant_combination) + '\n')  # Write to file

    # Print the path to the output file
    abs_path = os.path.abspath(output_file)
    print(f"{Fore.GREEN}[+] Please check file combinations.txt at {abs_path}")

if __name__ == "__main__":
    main()

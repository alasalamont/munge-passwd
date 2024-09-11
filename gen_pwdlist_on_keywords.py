import itertools

# Function to display how the script works
def display_how_it_works():
    print("""
HOW THIS SCRIPT WORKS:
+ Generates a list of passwords (combinations.txt) based on keyword combinations.
+ Ensures combinations end with only a valid word or number.
→ No special characters will be at the end.

WHY NO SPECIAL CHARS AT THE END?
+ The generated combinations.txt will be used by munge.py, which also adds the most common suffixes at the end.
→ For more details, check dictionaries.py.
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
    all_keywords = []

    while True:
        print("[+] Please provide the keywords, it could be a word, number, or special chars, and separate them by commas.")
        print("[+] Ex: du, cloud, 2023, 2024, @, `, ~")
        
        user_input = input("[+] Enter your keywords: ").strip()
        
        # Split the input by commas, remove extra spaces, and ensure no empty strings
        keywords = [word.strip() for word in user_input.split(',') if word.strip()]
        all_keywords.extend(keywords)
        
        # Ask user if they want to add more
        more_input = input("[?] Do you want to add more? [1] Yes [2] No: ").strip().lower()
        
        if more_input in ['no', 'n', '2']:  # Stop if user chooses 'no' or '2'
            break
        elif more_input not in ['yes', 'y', '1']:  # Re-prompt if invalid input
            print("[!] Invalid input, stopping the process.")
            break

    print(f"[+] Final list of keywords: {all_keywords}")
    
    return all_keywords

def main():
    # Display the explanation before the script runs
    display_how_it_works()
    
    # Get keywords from the user
    keywords = get_keywords()

    # Open a file to save the combinations
    with open("combinations.txt", "w") as f:
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

if __name__ == "__main__":
    main()
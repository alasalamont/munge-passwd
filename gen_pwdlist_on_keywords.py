"""
HOW THIS SCRIPT WORKS?
+ It will generate a list of passwords that based on the combination of keywords
+ It will check if the combination ends with a valid word or number
→ This means there is no special chars at the end

WHY?
+ After generating the combination.txt, we will provide this file to munge.py, because the munge.py also define the sufixes
→ Check file dictionaries.py to understand more
"""

import itertools

keywords = ['du', 'cloud', '2023', '2024', '.', '@', '#', '!', '_', '-']

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

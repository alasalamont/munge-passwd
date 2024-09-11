# Munge
A password variation generator inspired by [Th3S3cr3tAg3nt/Munge](https://github.com/Th3S3cr3tAg3nt/Munge).
<br>

**Why create a new version?**
1. Fully compatible with Python 3.
3. Expanded set of common leetspeak transformations.
4. More flexible and customizable password variations.
<br>

**How it work?**
1. First, script will generate the basic-passwd-list by combine all keywords together
2. Then it will apply leetspeak to transform characters. Ex: The character `a` can be come `@` or `4`
3. Finally, it will also append the most common suffixes at the end
<br>

**How to use?**
1. Run file gen_pwdlist_on_keywords.py to generate combinations.txt
3. Provide the combinations.txt to mungle.py to get the comprehensive password list


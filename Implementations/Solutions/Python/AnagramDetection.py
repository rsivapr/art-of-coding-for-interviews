def hashing_function(character):
    char_map = {
        'a' : 2,
        'b' : 3,
        'c' : 5,
        'd' : 7,
        'e' : 11,
        'f' : 13,
        'g' : 17,
        'h' : 19,
        'i' : 23,
        'j' : 29,
        'k' : 31,
        'l' : 37,
        'm' : 41,
        'n' : 43,
        'o' : 47,
        'p' : 53,
        'q' : 59,
        'r' : 61,
        's' : 67,
        't' : 71,
        'u' : 73,
        'v' : 79,
        'w' : 83,
        'x' : 89,
        'y' : 97,
        'z' : 101,
        'A' : 103,
        'B' : 107,
        'C' : 109,
        'D' : 113,
        'E' : 127,
        'F' : 131,
        'G' : 137,
        'H' : 139,
        'I' : 149,
        'J' : 151,
        'K' : 157,
        'L' : 163,
        'M' : 167,
        'N' : 173,
        'O' : 179,
        'P' : 181,
        'Q' : 191,
        'R' : 193,
        'S' : 197,
        'T' : 199,
        'U' : 211,
        'V' : 223,
        'W' : 227,
        'X' : 229,
        'Y' : 233,
        'Z' : 239}
    return char_map[character]  

def hash_product(word):
    product = 1
    for i in word:
        product *= hashing_function(i)
    return product

def f(parent_string, child_string):
    total = 0
    listing = []
    kchild = len(child_string)
    kparent = len(parent_string)
    child_prod = hash_product(child_string)
    for pos in range(kparent - kchild):
        check_string = parent_string[pos:pos+kchild]
        if hash_product(check_string) == child_prod:
            total += 1
            listing.append(check_string)
    print total, listing












































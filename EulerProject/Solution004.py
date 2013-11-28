def is_palindrome(k):
    return str(k)[::-1] == str(k)

def biggest_3d():
    big = 0
    for i in range(100,999)[::-1]:
        for j in range(100,999)[::-1]:
            if is_palindrome(i*j):
                big = i*j if big < i*j else big
    return big

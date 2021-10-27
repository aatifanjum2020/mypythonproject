
def odd_or_even (x = int(input("Enter the value of X "))):
    if x%2 == 0 :
        return  0
    else:
        return  1


def prime_or_composite(x = int(input("Enter the value of x :"))):
    y = odd_or_even(x)
    if y == 0:
        return "composite"
    else:
        for i in range(2 , x):
            if x%i == 0:
                return "composite"
            else:
                continue
    return "prime"  







def generate_pattern(n):


    for i in range(1, n + 1):

        print(''.join(str(x) for x in range(1, i + 1)))

number = int(input("chawere raime: "))
generate_pattern(number)
total_sum=(10000)

while True:
    user_input=int(input('Enter a number: '))
    if user_input == 0 :
        print('aq morcha')
        break
    else:
        if int(user_input)!= 0 :
            total_sum=total_sum+int(user_input)
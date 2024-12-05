

while True:
    user_input=input('Enter a text: ')
    if user_input == '0' :
        print('here ends')
        break
    else:
        if int(user_input)!=0:
            total_sum = total_sum + int(user_input)

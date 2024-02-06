choices = input('Enter what you want to calculate')
print(choices)


if(choices == 'area'):
    a = int(input('enter a '))
    print(a**2)
elif( choices=="perimeter"):
    a_1=int( input( "enter your a_1"))
    print(4*a_1)
else:
    print('error')

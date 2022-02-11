
try:
    x = int(input("Enter your weight: "))
    y = int(input("Enter your height: "))

    weight = x
    height = y

    BMI = int((x/(y**2)))

    if (BMI < 18.5):
        print ('underweight')
    elif (BMI >= 18.5 and BMI < 25):
        print('Normal')
    elif (BMI >= 25 and BMI< 30):
        print('Overweight')
    elif (BMI >= 30):
        print ('Obesity')
    else: 
        print('')
except ValueError:
    print("invalid input")
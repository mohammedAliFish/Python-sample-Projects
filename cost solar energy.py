import time
number_of_hourse = int(input('Enter Number of Hourse : '))

watt = 750

safef = 1.5

result_h = number_of_hourse*watt*safef

number_of_panel = result_h / 545

cost_of_panel = number_of_panel*180+number_of_panel*30

print('watt is : ')
print(result_h)

print('number of panel is : ')
print(int(number_of_panel))

if result_h/1.5 < 10000:
    cost_of_panel=cost_of_panel+500
    print('Inverter model GD11')

elif result_h/1.5 <= 15000 and result_h/1.5 >= 10000:
    cost_of_panel=cost_of_panel+600
    print('Inverter model GD18')

elif result_h/1.5 > 15000 and result_h/1.5 >= 18000 :
    cost_of_panel=cost_of_panel+700
    print('Inverter model GD22')
    
print('Cost of panel is : ')
print(int(cost_of_panel))


gas = int (input('Letter of gas : '))

cost = gas * 0.4

cost_per_year = cost * 365

print('cost of gas per year is : ')
print(cost_per_year)



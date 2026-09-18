import os
os.system('color')
RESET="\033[0m"
YELLOW = "\033[33m"
user=input('ENTER YOUR NAME: ')
age = int(input(f"{YELLOW}Enter your age{RESET} "))
if age < 18:
    print('NOT ELIGIBLE TO BOOK TICKETS')
    exit()
seat_type = input(f'{YELLOW}Enter seat type [Silver=5],[Gold=15],[Platinum=30]{RESET} ')
if seat_type=='Silver':
    base_price = 5
if seat_type=='Gold':
    base_price = 15
if seat_type=='Platinum':
    base_price=30
show_time = input(f'{YELLOW}Enter your showtime [Morning],[Evening],[Night]{RESET} ')

if age > 17:
    print(f'{YELLOW}User is eligible to book a ticket{RESET}')

if age >= 21:
    print(f'{YELLOW}User is eligible for Evening shows{RESET}')
else:
    print(f'{YELLOW}User is not eligible for Evening shows{RESET}')

is_member = input(f'{YELLOW}Are you member? True/False {RESET}')
is_weekend = input(f'{YELLOW}Are you booking for weekend? True/False{RESET} ')

discount = 0
if is_member:
    discount = 3
    print(f'{YELLOW}User qualifies for membership discount{RESET}')
else:
    print(f'{YELLOW}User does not qualify for membership discount{RESET}')
print('Discount:', discount)

extra_charges = 0
if is_weekend or show_time == 'Evening':
    extra_charges = 2
    print(f'{YELLOW}Extra charges will be applied{YELLOW}')
else:
    print(f'{YELLOW}No extra charges will be applied{RESET}')
print('Extra charges:', extra_charges)

if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print(f'{YELLOW}Ticket booking condition satisfied{RESET}')

    service_charges = 0
    if seat_type == 'Platinum':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1
    print(f'{YELLOW}Service charges:{RESET}', service_charges)

    final_price = base_price+ service_charges + extra_charges - discount
    print(f'{YELLOW}Final price of ticket:{RESET}',final_price)
    print('Enter your payment type: ')
    print('1 for cash (Only Payment option right now) ')  
    pay=int(input(' '))
    greet=True
    if pay==1:
        print('YOUR TICKETS LOCKED BUT WILL BE CONFIRMED ONCE YOU PAY ON THE CASH COUNTER') 
        greet=True
else:
    greet = False
    print(f'{YELLOW}Ticket booking failed due to restrictions{RESET}')
if greet == True:
    print('LETS MEET AT MOVIE')
elif greet== False:
    print('TICKET BOOKING FAILED!!!')
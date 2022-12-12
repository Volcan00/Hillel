import datetime
from threading import Thread


def get_start_number(start):
    while True:
        if len(start) > 6:
            print("Ticket number can't be longer then 6 digits. Please enter another ticket number.")
            break
        elif len(start) > 1 and (0 < int(start[1]) <= 9):
            print("Ticket number can't be non-ineger. Please enter another ticket number.")
            break
        else:
            return int(start)

def get_end_number(end):
    while True:
        if end[0] == "0" or len(end) > 7999:
            print("Ticket number shoudn't start with 0 and can't be longer then 6 digits. Please enter another number according to the parameters.")
            break
        else:
            return int(end)

def count_ticket(start_number, end_number):
    count = 0
    for i in range(start_number, end_number):
        num = str(i).rjust(6, "0")
        if int(num[0]) + int(num[1])+ int(num[2]) == int(num[3]) + int(num[4]) + int(num[5]):
            count += 1
    print(count)
    return count

start_number = get_start_number(input("Please enter the number of the start ticket: "))
end_number = get_end_number(input("Please enter the number of the end ticket: "))

print(f"Here is your amount of lucky tickets: {count_ticket(start_number, end_number)}")

t1 = Thread(target=count_ticket, args=[start_number, int(end_number / 2)])
t2 = Thread(target=count_ticket, args=[int(end_number / 2 + 1), end_number])

t1.start()
t2.start()

t1.join()
t2.join()
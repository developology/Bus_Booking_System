import random
from datetime import date, datetime

TotalSeatsAvailable = 50
TotalSeatsBooked = 0
PricePerTicket = 100
BookedList = []

user_choice = {
    "1": "Book a seat",
    "2": "Cancel a Booking",
    "3": "View seat Status",
    "4": "Exit"
}

def print_menu():
   
    for i in user_choice.values():
        print(i, end="\n")
    global User_choice_input
    User_choice_input = input("Select an option (1, 2, 3, 4): ")

def Confirming_ticket():

    global TotalSeatsAvailable, TotalSeatsBooked
    Confirmation_input = input("Please confirm your ticket [y/n]: ")
    if Confirmation_input == "Y" or Confirmation_input == "y":
        print("----------------------------")
        print("Ticket confirmed.")
        print("----------------------------")
        print("Your Unique Booking ID is: ", BookingID)
        print("Total Confirmed Seats are: ", HowmanySeats)
        print("Total Discount Applied:", Discount)
        print("----------------------------")
        print("Total Bill: ", TotalCostAfterDiscount)
        print("----------------------------")
        print("Thank you for booking with RAB Booking Services.")
        BookedList.append(BookingID)
        TotalSeatsAvailable -= HowmanySeats
        TotalSeatsBooked += HowmanySeats
        
        print_menu()
        action_on_menu()

    elif Confirmation_input == "N" or Confirmation_input == "n":
        print("Ticket not confirmed.")
        print("Please contact RAB Booking Services for further assistance.")
        print("Thank you for using RAB Booking Services.")
        print("----------------------------")
        print("Exiting...")
        exit()
    else:
        print("Invalid input. Please enter 'Y' or 'N'.")

def action_on_menu():
    
    global User_choice_input, TotalSeatsAvailable, TotalSeatsBooked, BookedList, PricePerTicket
    
    if User_choice_input == "1":
        print("...Welcome to RAB BOOKING SERVICES...")
        global BookingID, HowmanySeats, Discount, TotalCostAfterDiscount
        BookingID = random.randint(100, 999)
        
        HowmanySeats = int(input("Please enter how many seats you want to book: "))
        
        BookingDate = date.today()  # Get today's date
        
        TripDate = input("Enter a date (DD/MM/YYYY): ")
        try:
          #only objects can be subtracted or added in terms of dates. 
          #Dates here are converted into datetime object and not into string.
          #the date is formated into string just for printing purposes.

          #this line coverts user input into date object and format.
            TripDate = datetime.strptime(TripDate, "%d/%m/%Y").date()
        except ValueError:
            print("Invalid date format. Please enter the date in DD/MM/YYYY format.")
            return
        
        DayDifference = TripDate - BookingDate
        
        if DayDifference.days > 6:
            TotalCostBeforeDiscount = PricePerTicket * HowmanySeats
            print("Total cost before discount: ", TotalCostBeforeDiscount)
            Discount = 30
            print("Congratulations! You got", Discount, "% off on total Bill.")
            TotalCostAfterDiscount = TotalCostBeforeDiscount - (TotalCostBeforeDiscount * 30 / 100)
            print("Total cost after discount: ", TotalCostAfterDiscount)
            Confirming_ticket()

        elif DayDifference.days > 3:
            TotalCostBeforeDiscount = PricePerTicket * HowmanySeats
            print("Total cost before discount: ", TotalCostBeforeDiscount)
            Discount = 10
            print("Congratulations! You got", Discount, "% off on total Bill.")
            TotalCostAfterDiscount = TotalCostBeforeDiscount - (TotalCostBeforeDiscount * 10 / 100)
            print("Total cost after discount: ", TotalCostAfterDiscount)
            Confirming_ticket()
        
        elif DayDifference.days <= 1:
            TotalCostBeforeDiscount = PricePerTicket * HowmanySeats
            print("Total cost before discount: ", TotalCostBeforeDiscount)
            Discount = 0
            print("Oops! Its a last moment plan! No discounts Sorry!")
            TotalCostAfterDiscount = TotalCostBeforeDiscount
            print("Total cost after discount: ", TotalCostBeforeDiscount)
            Confirming_ticket()

    elif User_choice_input == "2":
        print("You chose to Cancel a Booking.")
      

    elif User_choice_input == "3":
        BookingIDenter = int(input("Enter your BookingID: "))
        if BookingIDenter in BookedList:
            print("Your seat is booked.")
            print(f"Seats available: {TotalSeatsAvailable}")
            print(f"Seats booked: {TotalSeatsBooked}")
            print_menu()
            action_on_menu()
        else:
            print("Your seat is not booked.")
            print(f"Seats available: {TotalSeatsAvailable}")
            print(f"Seats booked: {TotalSeatsBooked}")
            print_menu()
            action_on_menu()

    elif User_choice_input == "4":
        print("Exiting...")
        
        exit()

    else:
        print("Invalid choice. Please select from the list.")
        print_menu()
        action_on_menu()

# Initial call to start the program
print_menu()
action_on_menu()

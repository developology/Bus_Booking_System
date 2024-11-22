# Bus_Booking_System

### Program Overview: 
You are tasked with creating a Python program that simulates a bus booking system for 50 passengers. The system 
should allow passengers to book and cancel seats, applying discounts and cashback based on the timing of the booking 
and cancellation. The application will run in the terminal; no graphical user interface is required. 
 
### Requirements: 
1. Seat Reservation: 
   - The bus has a total of 50 seats available for reservation. 
   - Passengers can book or cancel each seat. 
 
2. Booking System: 
   - Booking a Week Before the Trip: 
     - If a passenger books a seat 7 or more days before the trip, they receive a 30% discount on the total fare. 
   - Booking 2-3 Days Before the Trip: 
     - If a passenger books a seat 2-3 days before the trip, they receive a 10% discount on the total fare. 
   - Booking 1 Day Before the Trip: 
     - If a passenger books a seat 1 day before the trip, no discount is applied. 
 
3. Cancellation System: 
- Unique Booking ID: 
     - Each booking should generate a unique ID for the passenger. 
     - The ID must be stored in the list of booked seats. 
- Cancellation Process: 
     - When a passenger requests a cancellation, they must provide their unique booking ID. 
     - The system should check if the ID is present in the list of booked seats. 
     - If the ID is valid, proceed with the cancellation.
- Refund System: 
     - Cancellation 5 Days Before the Trip: 
     - If a passenger cancels their seat 5 or more days before the trip, they receive a 100% refund. 
     - Cancellation Less Than 5 Days Before the Trip: 
     - The refund decreases as the trip date approaches. 
     - For example, if the passenger cancels 4 days before the trip, they get 80% cashback, 3 days before - 60%, and so on. 
 


### Flowchart Explanation: 
1. Initialize 50 Seats (All seats set to "Available")
   
2. Display Menu: - 1. Book a Seat - 2. Cancel a Booking - 3. View Seat Status - 4. Exit
   
3. User Input (Choose from the menu)

4. If 'Book a Seat' Chosen:
  
- Generate Unique Booking ID
- Get Booking Date and Trip Date
- Calculate Days Until Trip
- Apply Discount Based on Days Until Trip
- Store Booking ID in Booked Seats List
- Update Seat Status to 'Booked'
- Print Confirmation with Final Fare and Booking ID
  
5. If 'Cancel a Booking' Chosen:

- Request Unique Booking ID
- Check If ID Exists in Booked Seats List
- If Valid ID: - Get Cancellation Date and Trip Date
- Calculate Days Until Trip
- Calculate Refund Based on Days Until Trip
- Remove ID from Booked Seats List
- Update Seat Status to 'Available'
- Print Cancellation Confirmation with Refund Amount
- If Invalid ID: - Print Error Message

6. If 'View Seat Status' Chosen: - Print Current Seat Availability

7. If 'Exit' Chosen: - End Program
 

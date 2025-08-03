Bike Rental Shop 
This is a basic Python console application for a bike rental shop. It allows users to:

View available bikes in stock.

Rent bikes by specifying quantity.

See rental cost (at a fixed price per bike).

Exit the program.

📁 Features
View total stock of bikes.

Rent bikes by specifying quantity.

Each bike costs 100 units (currency not specified).

Basic input validation to ensure:

Quantity is positive.

Quantity does not exceed current stock.

🛠 How It Works
The program uses a class BikeShop with:

__init__(self, stock) – initializes stock.

displayBike() – displays current stock.

rentForBikes(q) – processes bike rentals.

A while loop allows continuous user interaction until exit.

🧪 Example
plaintext
Copy
Edit
1) Display Stocks
2) Rent a Bike
3) Exit 
If you choose 1:
yaml
Copy
Edit
Total Bikes: 100
If you choose 2 and enter 5:
mathematica
Copy
Edit
Total price 500
Total Bikes 95
⚠️ Limitations
The stock resets to 100 each time because the BikeShop object is created inside the loop.

No file or database persistence — all data is in memory during runtime.

No date/time handling for rental periods.

✅ To Improve
Move obj = BikeShop(100) outside the loop to retain stock across actions.

Add functionality for rental return and rental period calculation.

Integrate with file/database for persistence.

Improve input handling and user interface.

▶️ Run the App
To run the app:

bash
Copy
Edit
python bike_rental.py
Make sure you're using Python 3.

# zerodha-demo

A simple flask app to demo the Parsing the Bin stream from Kite Websockets & storing the data into mySQL. While a parallel request thread would fetch the data from the DB and display it on the screen.

## Steps to Run
  ### Prerequisites
   Setup mysql & run the sql file zerodhastreamquotes_modeltp.sql to create the Table
    
  ### Code Setup
   1. Setup venv
   2. pip install -r requirements.txt
   3. python runsever zerodha.py
   
  ### Access
   - From the browser hit http://localhost:5000
   - Hit http://localhost:5000/53397255,53426439,53427463,53426951,53329415,53405959 to add the instruments to be subscribed 
   - http://localhost:5000/fetch lists the results of the Tick Data from the DB
 

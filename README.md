# Stock Portfolio Tracker
https://github.com/petelah/Stock-Portfolio-Tracker
![Main screen image](img/mainscreen.png)


## Description
Welcome to the greatest terminal stock tracker ever made!

It utilises AlphaVantage to get end of day data to calculate the metrics. Currently 
only supports up to 6 stocks. But have included in future plans some pagination and 
support for bigger portfolio's and portfolio switching.

The metrics it performs are quite basic but it will show you:
 * Return %
 * Return $ on initial investment
 * Over all performance for all stocks in portfolio as well

Currently only supports stocks listed on US exhanges(NASDAQ, NYSE, AMEX).

The terminal GUI is built on top of npyscreen framework created by Nicholas Cole https://github.com/npcole/npyscreen.
Great framework to work with, I hope he releases more future updates.

If you ask nicely I may add in your beloved crypto markets too =)

## API Usage
The stock tracker itself is powered by AlphaVantage.co. I recommend getting key 
from here: https://www.alphavantage.co/support/#api-key.

Since we are using a free key, you can only grab up to 5 stocks/requests per minute.
Don't worry! We have a code that will sleep for you instead of returning a error, 
exiting the program and ruining your day. =)

## Workflow
Current workflow is setup to push through GitHub Actions CI/CD pipeline to and Amazon EC2 instance for deployment.
The pipeline looks like this:

Development machine -> Flake8/Mypy -> GitHub -> Automated testing -> Push to master -> Deploy & run on EC2

## Installation
#### Dependencies
* See requirements.txt

#### Setup & Run

Set up your desired method of python virtual environment.
Activate your environment and run the following:
```
pip install -r requirements.txt
```
Export your api key IE:
```
export API_KEY=IUGURH&3894F
```
From src directory:
```
python main.py
```

#### First Run
Your terminal screen will need to be certain size for it to run(122w x 32h) derived as 
lines x columns. Or you can just open it in a full screen window and resize to 
the appropriate height.

You will be asked to open the menu and add a stock to track. This can be done using 
^X(CTRL + X) to open the main menu. Select Add stock by pressing 1 or Enter on the 
menu item. Fill in the form and it will return the stock and update the portfolio if 
the provided symbol is valid

Once your first lot of stocks are in you can then run the 
update function whenever you want to get the latest end of day 
pricing and recalculation of your portfolio holdings.

The repo includes a demo portfolio to load, so please delete that if you would like to make your own.

#### Usage
The menu can be activated from the main menu using ^X(CTRL+X).
Navigating through the menu's you can either press enter on the desired selection, press the corresponding 
number or click to select and enter to proceed, clicking will work with all elements as well to select them.

## Release History

* 0.2.8
    * CHANGE: 11th hour refactor, packaged everything up.
* 0.2.6
    * CHANGE: Refactoring to be more modular between GUI and class's.
    * ADD: About page.
* 0.2.4
    * CHANGE: Docstring formatting.
    * ADD: Tests for verification.
* 0.2.2
    * FIX: Added a little solution to run even if the terminal height and width isn't right.
    You will just need to resize it out instead.
* 0.2.1
    * CHANGE: Update docs to reflect GUI addition.
* 0.2.0
    * CHANGE: Text based GUI goodness team!
    * CHANGE: Full refactoring of functions so all data is handled ouside GUI addition.
    Functions and class methods are standalone testable impartial to GUI.
* 0.1.9
    * ADD: Performance metrics for all stocks and overall portfolio.
* 0.1.7
    * ADD: Automated testing and CI/CD pipeline for all functions.
* 0.1.6
    * ADD: Delete stock function.
* 0.1.4
    * ADD: Update stocks function. Iterate through and update all stocks.
* 0.1.1
    * FIX: Added 60 second sleep function when adding more than 5 stocks as AV
    only lets you execute 5 calls per minute.
* 0.1.0
    * First major working release.
    * You can now save your portfolio to json format to recall later on.
    * Saving and loading features added, menu system added as well.
* 0.0.1
    * Basic terminal app that will display pulled stocks from Alpha Vantage API.


### Future Features

- Save to PDF
- Add colour
- About page
- Pagination for bigger portfolio
- Update tracking, if user already updated today, then don't update(NYC time after 4pm)
- Threading to pass off updating stocks in background


# Stock Portfolio Tracker

## Description
This little guy can be used as a basic performance 
tracker for your stock portfolio.

It utilises AlphaVantage to get end of day data to 
calculate the metrics.

If you are using a free API key it will wait 60 
seconds before pulling more data to avoid errors in 
your data collection.

## Installation
Set up your desired method of python virtual environment.
```
pip install requirements.txt
```
Export your api key IE:
```
export API_KEY=IUGURH&3894F
```
```
python main.py
```

##### First Run
You will be prompted to enter some stocks you are holding 
separated by ", " ie: IBM, AAPL, ZM.

Once your first lot of stocks are in you can then run the 
update function whenever you want to get the latest end of day 
pricing and recalculation of your portfolio holdings.

### Todo

- Text GUI
- Threading to pass off updating stocks in background


**Algorithmic Trading**

Three Quantitative finance projects

- The equal-weight version of the popular S&P 500 index
- Quantiative momentum strategy (Select the best stocks on variety of metrics)
- Quantitaive value screener (Select stocks based on the number of value metrics)

**Project Overview**
1. Algorithmic Trading Basics
2. API Basics and Course Configuration
3. Project 1: Equal-Weight S&P 500 screener
4. Project 2: Quantitative Momentum Screener
5. Project 3: Quantitative Value Screener

**Algorithmic Trading Basics**
- This means using computers to make investment decisions.
- There are many different types of algorithmic trading. The main difference is their speed of execution

**The Algorithmic Trading Landscape (Big players in this field)**
- Renaissance Technologies: $165B in AUM (Assets Under Management)
- AQR Capital Management: $61B in AUM 
- Citadel Securities: $32B in AUM

**The Algorithmic Trading Process**
1. Collect Data
2. Develop a hypothesis for a strategy
3. Backtest that strategy
4. Implement the strategy in production

**API Basics and Project Configuration**

API 
An API is an application programming interface

API allow you to interact with someone else's software using your own code.

In this project we will use IEX Cloud API

API Functionality
- GET
- POST
- PUT
- DELETE

GitHub link tp practice APIs
https://github.com/public-apis/public-apis

# Project 1 Equal-Weight S&P 500 Screener
S&P 500 is the world's most popular stock market index

**Code Overview:**

1. **Import librarires (numpy, pandas, requests, xlsxwriter, math)**
2. **Importing list of stocks i.e., reading the csv file which has all the S&P 500 stocks.** 
3. **Acquire API token, here we will use IEX Cloud API token in sandbox mode which is the free version.**
4. **After acquiring the token we will call API to get the data for example we can use API to get the current stock price for AAPL.**


# Project 2 Quantitative Momentum Screener
Momentum investing means investing in assets that have increased in the price the most.

For example, AAPL went up 35% and MSFT went up 20% last year, the momentum strategy will suggest to invest in AAPL for higher price return.


# Project 3 Quantitative Value Screener
Value investing means investing in stocks that are trading below their percieved intrinsic value.

For example: You buy a $1 stock for .75 cents and sell it again for $1

The stocks are selected using investing strategies which relies on a concept callled multiples

Multiples are calculated by dividing a company's stock price by some measure of the company's worth-like earnings or assets.

Common multiples used in value investing:
- Price to Earnings (P/E)
- Price to Book value (P/B)
- Price to free cash flow 

Each multiples haves its pros and cons, one way to minimize the impact of any specific multiple is by using composite.

import yfinance as yf
import sys

# Function to retrieve stock data

def getStockPrice(ticker):
	stock = yf.Ticker(ticker)

	# Get the latest stock price

	stockInfo = stock.history(period="1d")

	if not stockInfo.empty:
		currentPrice = stockInfo['Close'].iloc[0] # use .iloc for position - based indexing
		return f"The current stock price for {ticker.upper()} is ${currentPrice:.2f}"

	else:
		return f"No data available for {ticker}"


# Example usage

if __name__ == "__main__":
	tickerSymbol = sys.argv[1]
	print(getStockPrice(tickerSymbol))



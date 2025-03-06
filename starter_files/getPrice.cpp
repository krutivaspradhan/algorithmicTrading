#include <iostream>
#include <cstdlib>

void getStockPrice(const std::string& ticker) {
    // Construct command to execute Python script
    std::string command = "python3 getPrice.py " + ticker;
    
    // Execute Python script using system call
    int result = std::system(command.c_str());

    if (result == -1) {
        std::cerr << "Error executing Python script!" << std::endl;
    }
}

int main() {
    // Get stock price for Apple
    getStockPrice("AAPL");
    
    /*
    // Get stock price for Tata Steel
    getStockPrice("TATASTEEL.NS");
    */    

    return 0;
}


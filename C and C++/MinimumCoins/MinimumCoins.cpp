

#include <iostream>
#include <vector>
#include <climits>
using namespace std;
int minCoins(std::vector<int>& coins, int amount) {
    std::vector<int> dp(amount + 1, INT_MAX);
    dp[0] = 0;

    for (int i = 1; i <= amount; ++i) {
        for (int coin : coins) {
            if (i - coin >= 0 && dp[i - coin] != INT_MAX) {
                dp[i] = std::min(dp[i], dp[i - coin] + 1);
            }
        }
    }

    return dp[amount] == INT_MAX ? -1 : dp[amount];
}

int main() {
    std::vector<int> coins; // Example coin denominations
    int amount;
    char quit;
    cout<<":::PROGRAM TO FIND MINIMUM NUMBER OF COINS REQUIRED:::";
    cout<<"\nEnter the amount:\t";cin>>amount;
    int x=1;
    cout<<"\nEnter the value of coins:\t";
    while(x!=0)
    {   
        cin>>x;
        coins.push_back(x);
    }
    int result = minCoins(coins, amount);
    if (result != -1) {
        std::cout << "Minimum number of coins required: " << result << std::endl;
    } else {
        std::cout << "It's not possible to make the given amount with the provided coins." << std::endl;
    }
    cin>>quit;
    return 0;
}

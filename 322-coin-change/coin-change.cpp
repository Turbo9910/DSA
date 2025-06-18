class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
    int coinsSize = coins.size();
    vector<vector<int>> R(coinsSize + 1, vector<int>(amount + 1));

    for (int i = 0; i <= coinsSize; i++) {
        R[i][0] = 0;
    }

    for (int j = 1; j <= amount; j++) {
        R[0][j] = amount + 1; // Initialize with a value larger than any possible number of coins
    }

    for (int i = 1; i <= coinsSize; i++) {
        for (int j = 1; j <= amount; j++) {
            if (coins[i - 1] > j) {
                R[i][j] = R[i - 1][j];
            } else {
                R[i][j] = min(R[i - 1][j], 1 + R[i][j - coins[i - 1]]);
            }
        }
    }

    return R[coinsSize][amount] > amount ? -1 : R[coinsSize][amount];
}


};
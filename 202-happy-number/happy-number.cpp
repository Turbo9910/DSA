class Solution {
public:
    bool isHappy(int num) {
    int slowPtr = num, fastPtr = num;
    do {
        slowPtr = calculateSquareSum(slowPtr);
        fastPtr = calculateSquareSum(calculateSquareSum(fastPtr));
    } while (slowPtr != fastPtr && slowPtr != 1);
    return slowPtr == 1;
}

int calculateSquareSum(int n) {
    int sum = 0;
    while (n > 0) {
        int digit = n % 10;
        sum += digit * digit;
        n /= 10;
    }
    return sum;
}

};
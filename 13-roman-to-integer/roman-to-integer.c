int romanToInt(char* s) {
    int sum = 0; // Initialize sum to 0
    int i = 0;
    
    while (s[i] != '\0') {
        if (s[i] == 'M') {
            sum += 1000;
            i++;
        }
        else if (s[i] == 'D') {
            sum += 500;
            i++;
        }
        else if (s[i] == 'C' && s[i + 1] == 'M') {
            sum += 900;
            i += 2;
        }
        else if (s[i] == 'C' && s[i + 1] == 'D') {
            sum += 400;
            i += 2;
        }
        else if (s[i] == 'C') {
            sum += 100;
            i++;
        }
        else if (s[i] == 'L') {
            sum += 50;
            i++;
        }
        else if (s[i] == 'X' && s[i + 1] == 'C') {
            sum += 90;
            i += 2;
        }
        else if (s[i] == 'X' && s[i + 1] == 'L') {
            sum += 40;
            i += 2;
        }
        else if (s[i] == 'X') {
            sum += 10;
            i++;
        }
        else if (s[i] == 'V') {
            sum += 5;
            i++;
        }
        else if (s[i] == 'I' && s[i + 1] == 'X') {
            sum += 9;
            i += 2;
        }
        else if (s[i] == 'I' && s[i + 1] == 'V') {
            sum += 4;
            i += 2;
        }
        else if (s[i] == 'I') {
            sum += 1;
            i++;
        }
    }
    return sum;
}

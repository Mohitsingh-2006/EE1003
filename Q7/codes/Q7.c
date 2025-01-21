#include <stdio.h>
#include <string.h>

// Function to calculate net money
double calculate_net_money(char *outcome) {
    double money = 0.0;
    for (int i = 0; i < strlen(outcome); i++) {
        if (outcome[i] == 'H') {
            money += 1.0;  // Gain ₹1 for Head
        } else if (outcome[i] == 'T') {
            money -= 1.5;  // Lose ₹1.50 for Tail
        }
    }
    return money;
}


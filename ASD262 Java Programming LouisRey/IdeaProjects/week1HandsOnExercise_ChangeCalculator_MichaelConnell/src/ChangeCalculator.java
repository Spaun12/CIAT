import java.util.Scanner;

public class ChangeCalculator {
    public static void main(String[] args) {
        // Version Information
        // * Change Calculator
        // * Author: Michael Connell
        // * Course: ASD262 - Java Programming (CIAT) Professor Louis Rey
        // * Date: 27 June 2024
        // * Purpose: Calculate the minimum number of coins for a given amount of cents and to learn while creating

        // Create a Scanner object for reading input
        Scanner scanner = new Scanner(System.in);
        String continueResponse;

        // My welcome message
        System.out.println("Welcome to Michael Connell's Change Calculator");
        System.out.println("Calculating change, one cent at a time!");
        System.out.println("Thank you to all our veterans, and families that support them!");

        do {
            int cents = -1;

            // Input validation loop for cents
            while (cents < 0 || cents > 99) {
                System.out.print("Enter number of cents (0-99): ");
                if (scanner.hasNextInt()) {
                    cents = scanner.nextInt();
                    if (cents < 0 || cents > 99) {
                        System.out.println("Please enter a valid integer between 0 and 99.");
                    }
                } else {
                    System.out.println("Invalid input. Please enter a valid integer between 0 and 99.");
                    scanner.next(); // Clear the invalid input
                }
            }

            // Calculate the number of each coin type
            int quarters = cents / 25; // Calculate quarters
            cents %= 25; // Update cents to remainder after quarters
            int dimes = cents / 10; // Calculate dimes
            cents %= 10; // Update cents to remainder after dimes
            int nickels = cents / 5; // Calculate nickels
            int pennies = cents % 5; // Calculate pennies

            // Display the result
            System.out.println("Quarters: " + quarters);
            System.out.println("Dimes: " + dimes);
            System.out.println("Nickels: " + nickels);
            System.out.println("Pennies: " + pennies);

            // Input validation loop for continue response
            do {
                System.out.print("Continue? (y/n): ");
                continueResponse = scanner.next();
                if (!continueResponse.equalsIgnoreCase("y") && !continueResponse.equalsIgnoreCase("n")) {
                    System.out.println("Invalid input. Please enter 'y' or 'n'.");
                }
            } while (!continueResponse.equalsIgnoreCase("y") && !continueResponse.equalsIgnoreCase("n"));

        } while (continueResponse.equalsIgnoreCase("y"));

        // Close the scanner
        scanner.close();
    }
}
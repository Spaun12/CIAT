// Author: Michael Connell
// Assignment: Week 2 - Hands On Exercise - Dice Roller
// Project Title: Dice Roller
// Date: 07/06/2024

import java.util.Scanner;
import java.util.Random;

public class DiceRoller {

    public static void main(String[] args) {
        // Welcome screen with dice ASCII art and play prompt because it is too plain otherwise.
        // (◕‿◕✿)
        // Creating the Scanner object for user input
        Scanner scanner = new Scanner(System.in);

        // Display welcome screen with ASCII art ( ͡~ ͜ʖ ͡°)
        displayWelcomeScreen();

        // Ask if the user would like to play
        System.out.print("Would you like to play? (y/n): ");
        String play = scanner.next();

        // Validate input for starting the game
        while (!play.equalsIgnoreCase("y") && !play.equalsIgnoreCase("n")) {
            System.out.println("Invalid input. Please enter 'y' to play or 'n' to exit.");
            System.out.print("Would you like to play? (y/n): ");
            play = scanner.next();
        }

        if (play.equalsIgnoreCase("y")) {
            String rollAgain;
            do {
                // Display a random humorous statement before rolling the dice
                displayHumorStatement();

                // Roll two dice
                int die1 = rollDie();
                int die2 = rollDie();
                int total = die1 + die2;

                // Display the result of the roll
                System.out.println("Die 1: " + die1);
                System.out.println("Die 2: " + die2);
                System.out.println("Total: " + total);

                // Check for special cases
                if (die1 == 1 && die2 == 1) {
                    System.out.println("The dice gods must be watching over you! Snake eyes!");
                } else if (die1 == 6 && die2 == 6) {
                    System.out.println("Wow! Look at that! Boxcars!");
                }

                // Prompt the user to roll again with input validation
                do {
                    System.out.print("Roll again? (y/n): ");
                    rollAgain = scanner.next();

                    // Check for valid input
                    if (!rollAgain.equalsIgnoreCase("y") && !rollAgain.equalsIgnoreCase("n")) {
                        System.out.println("Invalid input. Please enter 'y' to roll again or 'n' to end the program.");
                    }

                } while (!rollAgain.equalsIgnoreCase("y") && !rollAgain.equalsIgnoreCase("n"));

            } while (rollAgain.equalsIgnoreCase("y"));
        }

        // Closing the scanner (•‿•)✌
        scanner.close();

        // Just because (¬‿¬)
        displayCoolExitMessage();
    }

    // Method to roll a single die and return a value between 1 and 6
    public static int rollDie() {
        return (int) (Math.random() * 6) + 1;
    }

    // Method to display welcome screen with ASCII art
    public static void displayWelcomeScreen() {
        System.out.println("Welcome to the Dice Roller!");
        System.out.println("  _____       _____ ");
        System.out.println(" |     |     | o o |");
        System.out.println(" | o o |     | o o |");
        System.out.println(" |  o  |     | o o |");
        System.out.println(" |_____|     |_____|");
        System.out.println();
    }

    // Method to display a random humorous (￣▽￣) statement
    public static void displayHumorStatement() {
        String[] statements = {
                "Rolling dice like a pro!",
                "You must have the luck of the Vault Dweller!",
                "Snake eyes or boxcars, which will it be?",
                "Feeling lucky today?",
                "Yoda needs a new pair of shoes!"
        };
        Random random = new Random();
        int index = random.nextInt(statements.length);
        System.out.println(statements[index]);
    }

    // Method to display a cool (⌐■_■) exit message
    public static void displayCoolExitMessage() {
        System.out.println("Thanks for playing! May the dice always roll in your favor.");
        System.out.println(" _____  _                _____         _    ");
        System.out.println("|  __ \\| |              |  __ \\       | |   ");
        System.out.println("| |  | | | __ _ _ __ ___| |  | | ___  | |_  ");
        System.out.println("| |  | | |/ _` | '__/ _ \\ |  | |/ _ \\ | __| ");
        System.out.println("| |__| | | (_| | | |  __/ |__| |  __/ | |_  ");
        System.out.println("|_____/|_|\\__,_|_|  \\___|_____/ \\___|  \\__| ");
        System.out.println();
    }
}



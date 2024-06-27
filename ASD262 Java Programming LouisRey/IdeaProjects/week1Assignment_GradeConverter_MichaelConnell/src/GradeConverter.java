import java.util.Scanner;

public class GradeConverter {
    public static void main(String[] args) {
        // Version Information
        // * Grade Converter
        // * Author: Michael Connell
        // * Course: ASD262 - Java Programming (CIAT) Professor Louis Rey
        // * Date: 27 June 2024
        // * Purpose: (Project 2-2): Grade Converter. Create an application that converts number grades to letter grades.

        // Scanner object to read user input
        Scanner scanner = new Scanner(System.in);

        // Z welcome message!
        System.out.println("Welcome to the Letter Grade Converter");

        // Loop to continue the program based on user input "Let's do this"
        String continueResponse = "y";
        while (continueResponse.equalsIgnoreCase("y")) {

            // Prompt user for numerical grade with validation of course
            int numericalGrade = 0;
            boolean validGrade = false;
            while (!validGrade) {
                System.out.print("Enter numerical grade (1-100): ");
                if (scanner.hasNextInt()) {
                    numericalGrade = scanner.nextInt();
                    if (numericalGrade >= 1 && numericalGrade <= 100) {
                        validGrade = true;
                    } else {
                        System.out.println("Invalid grade. Please enter a number between 1 and 100.");
                    }
                } else {
                    System.out.println("Invalid input. Please enter a number.");
                    scanner.next(); // Clear the invalid input
                }
            }

            // Determine the letter grade using if-else statements
            String letterGrade;
            if (numericalGrade >= 88) {
                letterGrade = "A";
            } else if (numericalGrade >= 80) {
                letterGrade = "B";
            } else if (numericalGrade >= 67) {
                letterGrade = "C";
            } else if (numericalGrade >= 60) {
                letterGrade = "D";
            } else {
                letterGrade = "F";
            }

            // Output the letter grade
            System.out.println("Letter grade: " + letterGrade);

            // Prompt user to continue or not with validation
            boolean validResponse = false;
            while (!validResponse) {
                System.out.print("Continue? (y/n): ");
                continueResponse = scanner.next();
                if (continueResponse.equalsIgnoreCase("y") || continueResponse.equalsIgnoreCase("n")) {
                    validResponse = true;
                } else {
                    System.out.println("Invalid response. Please enter 'y' or 'n'.");
                }
            }
        }

        // Close the scanner object to prevent resource leaks
        scanner.close();

        // Farewell message
        System.out.println("Thank you for using the Letter Grade Converter. Goodbye!");
    }
}

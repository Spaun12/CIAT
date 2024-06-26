package week1_HandsOnExercise_SR_MichaelConnell;

import java.util.Scanner;

public class StudentRegistration {

    public static void main(String[] args) {
        // Create a Scanner object for user input
        Scanner scanner = new Scanner(System.in);
        
        // Prompt user for first name
        System.out.print("Enter first name: ");
        String firstName = scanner.nextLine();
        
        // Prompt user for last name
        System.out.print("Enter last name: ");
        String lastName = scanner.nextLine();
        
        // Prompt user for year of birth
        System.out.print("Enter year of birth: ");
        int yearOfBirth = scanner.nextInt();
        
        // Close the scanner (no more input needed)
        scanner.close();
        
        // Construct full name and temporary password
        String fullName = firstName + " " + lastName;
        String tempPassword = firstName + "*" + yearOfBirth;
        
        // Display the completion message
        System.out.println("\nWelcome " + fullName + "!");
        System.out.println("Your registration is complete.");
        System.out.println("Your temporary password is: " + tempPassword);
    }
}

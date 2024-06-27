package Week1HandsOnExcercise_StudentRegistration_MichaelConnell;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class StudentRegistration {

    public static void main(String[] args) {
        try (var reader = new BufferedReader(new InputStreamReader(System.in))) {
            // Prompt user for first name
            System.out.print("Enter first name: ");
            var firstName = reader.readLine().trim();

            // Prompt user for last name
            System.out.print("Enter last name: ");
            var lastName = reader.readLine().trim();

            // Prompt user for year of birth
            System.out.print("Enter year of birth: ");
            var yearOfBirthStr = reader.readLine().trim();
            var yearOfBirth = Integer.parseInt(yearOfBirthStr);

            // Construct full name and temporary password
            var fullName = String.format("%s %s", firstName, lastName);
            var tempPassword = String.format("%s*%d", firstName, yearOfBirth);

            // Display the completion message
            System.out.println("\nWelcome " + fullName + "!");
            System.out.println("Your registration is complete.");
            System.out.println("Your temporary password is: " + tempPassword);

        } catch (IOException e) {
            System.err.println("An error occurred while reading input: " + e.getMessage());
        } catch (NumberFormatException e) {
            System.err.println("Invalid input for year of birth. Please enter a valid 4-digit year.");
        }
    }
}


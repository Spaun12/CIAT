package week1HandsOnExercise_StudentRegistration_MichaelConnell;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class StudentRegistration {

    public static void main(String[] args) {
        try {
            // Create a BufferedReader object for user input
            var reader = new BufferedReader(new InputStreamReader(System.in));
            
            // Prompt user for first name
            System.out.print("Enter first name: ");
            String firstName = reader.readLine();
            
            // Prompt user for last name
            System.out.print("Enter last name: ");
            String lastName = reader.readLine();
            
            // Prompt user for year of birth
            System.out.print("Enter year of birth: ");
            String yearOfBirthStr = reader.readLine();
            int yearOfBirth = Integer.parseInt(yearOfBirthStr);
            
            // Construct full name and temporary password
            String fullName = firstName + " " + lastName;
            String tempPassword = firstName + "*" + yearOfBirth;
            
            // Display the completion message
            System.out.println("\nWelcome " + fullName + "!");
            System.out.println("Your registration is complete.");
            System.out.println("Your temporary password is: " + tempPassword);
            
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

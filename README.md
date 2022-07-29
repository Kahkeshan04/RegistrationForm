# Registration Form

A simple registration form using Python without any libraries, using a text file as a database. It is non-GUI program.
The project contains two files and three functions
First-file is the main file that contains the whole code. 
The second file is a text file that stores the username and passwords.
The three Functions are:
     - registration()
     - logIn()
     - form()
 
 The following are the validation applied on input given by the user:
 
1. Username contains the following validation:
     - Username cannot be empty.
     - Username cannot start with Special Characters or Digits.
     - Username must contain '@' & '.'.
     - Username Exists - prevents repeatation. 

2. Password contain the following  validations:
     - Password cannot be empty.
     - Passwords don't match - Password Filed and Confirm Password don’t match.
     - Password should be between 5 to 16 character.
     - Password must have minimum one UpperCase Character, one LowerCase Character, one Digit, one Special Character.

The program start with two options - Login | Signup, where the user can sign up if it's a new registration or can login if they have already registered. 
If a user forget the password three options are show - 
     - Forget password - This will show the password of the UserId entered by the User. Although this is not the correct way to help users when they forget the password. But still it's just for practice purposes.
     - Try again - This will allow the user to enter the password again and if the username and password is matched Login successful!!! Will be displayed.
     - New password - This option is for those who wish to change their password. After the change, the new password will be updated in the database. 

This is the overall function of this project.
 
 

## In this project, I have created a Python script that reads a bunch of passwords from the text file and checks whether the password has been compromised in a hack before.
- An API call is made with the first 5 characters of hashed version of the given password and all the passwords which have matching first 5 characters are fetched. They are then compared with the remaining characters of the hashed password to see if there exists a match.

## Libraries used:
- requests
- hashlib

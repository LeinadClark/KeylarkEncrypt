from cryptography.fernet import Fernet
import os

def generate_key():
    """Generate a new Fernet key."""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    """Load the previously generated key."""
    return open("secret.key", "rb").read()

def encrypt_file(input_file, output_file):
    """Encrypt the contents of the input file and save to the output file."""
    # Load the key
    key = load_key()
    fernet = Fernet(key)

    # Read the file
    with open(input_file, "rb") as file:
        file_data = file.read()

    # Encrypt the data
    encrypted_data = fernet.encrypt(file_data)

    # Write the encrypted data to a new file
    with open(output_file, "wb") as file:
        file.write(encrypted_data)

    print(f"File '{input_file}' encrypted and saved as '{output_file}'.")

if __name__ == "__main__":
    # Check if the key exists, if not generate a new one
    if not os.path.exists("secret.key"):
        generate_key()

    # Specify the input and output file names
    input_filename = "example.txt"  # Change this to your input file
    output_filename = "encrypted_example.txt"  # Output file name

    # Encrypt the file
    encrypt_file(input_filename, output_filename)
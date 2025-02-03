import os

directory = "E:\\Haqdarshak\\Scheme-Research-Application"

if os.path.exists(directory):
    print(f"The directory {directory} exists.")
    
    # Test if the directory is writable
    test_file_path = os.path.join(directory, "test_permission_check.txt")
    try:
        with open(test_file_path, "w") as test_file:
            test_file.write("Write test successful!")
        os.remove(test_file_path)  # Clean up after test
        print("Write permission confirmed!")
    except PermissionError:
        print("You do not have write permission to this directory.")
else:
    print(f"The directory {directory} does not exist.")

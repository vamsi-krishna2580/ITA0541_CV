import os

# Create folders exp_7 to exp_15
for i in range(21, 30):
    folder_name = f"exp_{i}"
    os.makedirs(folder_name, exist_ok=True)

    # Create code.py inside each folder
    file_path = os.path.join(folder_name, "code.py")

    with open(file_path, "w") as f:
        f.write("# Your Python code goes here\n")

print("Folders and code.py files created successfully!")
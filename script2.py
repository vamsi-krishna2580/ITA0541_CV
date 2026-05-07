import os
import shutil

# Root directory
root_dir = os.getcwd()

# Loop from exp_8 to exp_15
for exp_no in range(16, 31):
    folder_name = f"exp_{exp_no}"
    
    source_path = os.path.join(root_dir, folder_name, "Figure_1.png")
    
    # New filename in root directory
    destination_path = os.path.join(root_dir, f"Figure_{exp_no}.png")

    # Check if source file exists
    if os.path.exists(source_path):
        shutil.copy(source_path, destination_path)
        print(f"Copied: {source_path} -> {destination_path}")
    else:
        print(f"File not found: {source_path}")
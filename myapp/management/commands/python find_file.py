import os

def find_file(filename, search_path):
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            return os.path.join(root, filename)
    return None

# Define the filename and the directory to search in
filename = 'US_State_and_County_Details_1.xlsx'
search_path = 'G:/admin_02_09_15'

# Find the file
file_path = find_file(filename, search_path)

if file_path:
    print(f"File found: {file_path}")
else:
    print("File not found")

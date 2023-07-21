import os
from urllib.parse import urlsplit


def extract_passwords(main_folder, output_folder, output_file):
    # Loop through all subdirectories in the main folder
    for subdir, dirs, files in os.walk(main_folder):
        # Loop through all files in the current subdirectory
        for file in files:
            # Check if the current file is a passwords.txt file
            if file == "passwords.txt" or "Passwords.txt" or "Password List.txt" or "_AllPasswords_list.txt":
                # Define the path to the current file
                file_path = os.path.join(subdir, file)
                # Open the current file for reading
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        # Read the contents of the file
                        contents = f.read()
                except UnicodeDecodeError:
                    print(f"Error: Unable to read file {file_path}. Skipping...")
                    continue
                # Split the contents of the file into individual password entries
                entries = contents.split("\n\n")
                # Loop through each password entry
                for entry in entries:
                    # Split the entry into individual lines
                    lines = entry.split("\n")
                    # Extract the URL, username, and password from the entry
                    url = ""
                    user = ""
                    password = ""
                    for line in lines:
                        if line.startswith("URL:"):
                            url = line.split("URL:")[1].strip()
                        elif line.startswith("url:"):
                            url = line.split("url:")[1].strip() if len(line.split("url:")) > 1 else ""
                        elif line.startswith("Url:"):
                            url = line.split("Url:")[1].strip() if len(line.split("Url:")) > 1 else ""
                        elif line.startswith("Host:"):
                            url = line.split("Host:")[1].strip() if len(line.split("Host:")) > 1 else ""
                        elif line.startswith("HOSTNAME:"):
                            url = line.split("HOSTNAME:")[1].strip() if len(line.split("HOSTNAME:")) > 1 else ""
                        elif line.startswith("USER:") or line.startswith("login:") or line.startswith("Login") or line.startswith("Username") or line.startswith("USER LOGIN:"):
                            user = line.split(":")[1].strip() if len(line.split(":")) > 1 else ""
                        elif line.startswith("PASS:") or line.startswith("password:") or line.startswith("Password") or line.startswith("USER PASSWORD:"):
                            password = line.split(":")[1].strip() if len(line.split(":")) > 1 else ""
                    # Format the entry as "URL:USER:PASS"
                    if url:
                        if url.startswith("android"):
                            package_name = url.split("@")[-1]
                            package_name = package_name.replace("-", "").replace("_", "").replace(".", "")
                            package_name = ".".join(package_name.split("/")[::-1])
                            package_name = ".".join(package_name.split(".")[::-1])
                            url = f"{package_name}android.app"
                        else:
                            url_components = urlsplit(url)
                            url = f"{url_components.scheme}://{url_components.netloc}"
                        formatted_entry = f'"{url}":{user}:{password}\n'
                        # Open the output file for appending
                        with open(os.path.join(output_folder, output_file), "a") as f:
                            # Write the formatted entry to the output file
                            f.write(formatted_entry)


def extract_passwords2(main_folder, output_folder, output_file2):
    # Loop through all subdirectories in the main folder
    for subdir, dirs, files in os.walk(main_folder):
        # Loop through all files in the current subdirectory
        for file in files:
            # Check if the current file is a passwords.txt file
            if file.lower() == "passwords.txt" or "Password List.txt" or "_AllPasswords_list.txt":
                # Define the path to the current file
                file_path = os.path.join(subdir, file)
                # Open the current file for reading
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        # Read the contents of the file
                        contents = f.read()
                except UnicodeDecodeError:
                    print(f"Error: Unable to read file {file_path}. Skipping...")
                    continue
                # Split the contents of the file into individual password entries
                entries = contents.split("===============\n")
                # Loop through each password entry
                for entry in entries:
                    # Split the entry into individual lines
                    lines = entry.strip().split("\n")
                    # Extract the URL, username, and password from the entry
                    url = ""
                    user = ""
                    password = ""
                    for line in lines:
                        if line.startswith("URL:") or line.startswith("url:") or line.startswith("Url:") or line.startswith("Host:") or line.startswith("HOSTNAME:"):
                            url = line.split(":", 1)[1].strip() if len(line.split(":")) > 1 else ""
                        elif line.startswith("USER:") or line.startswith("login:") or line.startswith("Login") or line.startswith("Username") or line.startswith("USER LOGIN:"):
                            user = line.split(":")[1].strip() if len(line.split(":")) > 1 else ""
                        elif line.startswith("PASS:") or line.startswith("password:") or line.startswith("Password") or line.startswith("USER PASSWORD"):
                            password = line.split(":")[1].strip() if len(line.split(":")) > 1 else ""
                    # Format the entry as "URL:USER:PASS"
                    if url:
                        if url.startswith("android"):
                            package_name = url.split("@")[-1]
                            package_name = package_name.replace("-", "").replace("_", "").replace(".", "")
                            package_name = ".".join(package_name.split("/")[::-1])
                            package_name = ".".join(package_name.split(".")[::-1])
                            url = f"{package_name}android.app"
                        else:
                            url_components = urlsplit(url)
                            url = f"{url_components.scheme}://{url_components.netloc}"
                        formatted_entry = f'"{url}":{user}:{password}\n'
                        # Open the output file for appending
                        with open(os.path.join(output_folder, output_file2), "a") as f:
                            # Write the formatted entry to the output file
                            f.write(formatted_entry)
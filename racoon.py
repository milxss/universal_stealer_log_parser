import os
from urllib.parse import urlsplit


def extract_passwords(main_folder, output_folder, output_file):
    # Loop through all subdirectories in the main folder
    for subdir, dirs, files in os.walk(main_folder):
        # Loop through all files in the current subdirectory
        for file in files:
            # Check if the current file is a passwords.txt file
            if file == "passwords.txt":
                # Define the path to the current file
                file_path = os.path.join(subdir, file)
                # Open the current file for reading
                with open(file_path, "r") as f:
                    # Read the contents of the file
                    contents = f.read()
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
                        if line.startswith("URL:") or line.startswith("url:"):
                            url = line.split("URL:")[1].strip() if line.startswith("URL:") else line.split("url:")[1].strip()
                            if url.startswith("android"):
                                package_name = url.split("@")[-1]
                                package_name = package_name.replace("-", "").replace("_", "").replace(".", "")
                                package_name = ".".join(package_name.split("/")[::-1])
                                package_name = ".".join(package_name.split(".")[::-1])
                                url = f"{package_name}android.app"
                            else:
                                url_components = urlsplit(url)
                                url = f"{url_components.scheme}://{url_components.netloc}"
                        elif line.startswith("USER:") or line.startswith("login:"):
                            user = line.split(":")[1].strip()
                        elif line.startswith("PASS:") or line.startswith("password:"):
                            password = line.split(":")[1].strip()
                    # Format the entry as "URL:USER:PASS"
                    if url:
                        formatted_entry = f'"{url}":{user}:{password}\n'
                        # Open the output file for appending
                        with open(os.path.join(output_folder, output_file), "a") as f:
                            # Write the formatted entry to the output file
                            f.write(formatted_entry)
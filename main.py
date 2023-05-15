from racoon import extract_passwords
from racoon_cc_parser import process_cc
main_folder = "..."
output_folder = "..."
output_file = "Treated_passwords.txt"

process_cc(main_folder)

extract_passwords(main_folder, output_folder, output_file)
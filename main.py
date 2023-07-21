from log_parser_body import extract_passwords_racoon, extract_passwords_redline
from cc_parser import process_cc, process_cc_v2


def main():
    output_file = "Treated_passwords_racoon.txt"
    output_file2 = "Treated_passwords_redline.txt"
    main_folder = input("Specify the main folder: ")
    print(f"The main folder is: {main_folder}")
    output_folder = main_folder
    process_cc(main_folder)
    process_cc_v2(main_folder)
    extract_passwords_racoon(main_folder, output_folder, output_file)
    extract_passwords_redline(main_folder, output_folder, output_file2)


if __name__ == "__main__":
    main()
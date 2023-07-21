import os


# define function to extract credit card information
def extract_cc_info(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            contents = f.read()
    except UnicodeDecodeError:
        print(f"Cannot read file '{file_path}' with encoding 'utf-8'. Skipping file...")
        return []
    cc_info_list = contents.split('\n\n')
    cc_info = []
    for info in cc_info_list:
        if info.strip() == '':
            continue
        cc_number = None
        if 'CC NUMBER: ' in info:
            cc_number = info.split('CC NUMBER: ')[1].split('\n')[0]
        elif 'Card: ' in info:
            cc_number = info.split('Card: ')[1].split('\n')[0]
        if cc_number:
            month = None
            year = None
            if 'EXPIRATION: ' in info:
                expiration_str = info.split('EXPIRATION: ')[1].split('\n')[0]
                month, year = expiration_str.split("/")
            elif 'Month: ' in info and 'Year: ' in info:
                month_str = info.split('Month: ')[1].split('\n')[0]
                year_str = info.split('Year: ')[1].split('\n')[0]
                month = month_str.strip()
                year = year_str.strip()
            if year is None:
                continue
            card_holder = None
            if 'CARD HOLDER: ' in info:
                card_holder = info.split('CARD HOLDER: ')[1].split('\n')[0]
            elif 'Name: ' in info:
                card_holder = info.split('Name: ')[1].split('\n')[0]
            if card_holder:
                cc_info.append((cc_number, f"{month}/{year}", card_holder))
    return cc_info


# define function to extract credit card information
def extract_cc_info_v2(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            contents = f.read()
    except UnicodeDecodeError:
        print(f"Cannot read file '{file_path}' with encoding 'utf-8'. Skipping file...")
        return []
    cc_info_list = []
    if 'Card: ' in contents:
        cc_number = contents.split('Card: ')[1].split('\n')[0]
        if 'Expire: ' in contents:
            exp_str = contents.split('Expire: ')[1].split('\n')[0]
            exp_month, exp_year = exp_str.split('/')
            if 'Holder: ' in contents:
                card_holder = contents.split('Holder: ')[1].split('\n')[0]
                cc_info_list.append((cc_number, f"{exp_month}/{exp_year}", card_holder))
    return cc_info_list


# define function to process all "CC.txt" and "CreditCards" files in a directory and its subdirectories
def process_cc_v2(main_folder):
    output_file_path = os.path.join(main_folder, 'merged_cc_info_redline.txt')
    with open(output_file_path, 'w') as f:
        for dirpath, dirnames, filenames in os.walk(main_folder):
            # Check if there are any subdirectories with a name containing "CC" or "CreditCards"
            cc_dirs = [d for d in dirnames if "CC" in d.upper() or "CREDITCARDS" in d.upper()]
            for cc_dir in cc_dirs:
                cc_dir_path = os.path.join(dirpath, cc_dir)
                for filename in os.listdir(cc_dir_path):
                    if filename.lower().endswith('.txt'):
                        file_path = os.path.join(cc_dir_path, filename)
                        cc_info_list = extract_cc_info_v2(file_path)
                        for cc_info in cc_info_list:
                            cc_number, expiration, card_holder = cc_info
                            f.write(f'{cc_number},{expiration},"{card_holder}"\n')
            # Process any ".txt" files in the current directory
            for filename in filenames:
                if filename.lower().endswith('.txt') and filename.lower() != 'merged_cc_info.txt':
                    file_path = os.path.join(dirpath, filename)
                    cc_info_list = extract_cc_info_v2(file_path)
                    for cc_info in cc_info_list:
                        cc_number, expiration, card_holder = cc_info
                        f.write(f'{cc_number},{expiration},"{card_holder}"\n')


# define function to process all "CC.txt" files in a directory and its subdirectories
def process_cc(main_folder):
    output_file_path = os.path.join(main_folder, 'merged_cc_info_racoon.txt')
    with open(output_file_path, 'w') as f:
        for dirpath, dirnames, filenames in os.walk(main_folder):
            # Check if there are any subdirectories with a name containing "CC"
            cc_dirs = [d for d in dirnames if "CC" in d.upper()]
            for cc_dir in cc_dirs:
                cc_dir_path = os.path.join(dirpath, cc_dir)
                for filename in os.listdir(cc_dir_path):
                    if filename.lower().endswith('.txt'):
                        file_path = os.path.join(cc_dir_path, filename)
                        cc_info_list = extract_cc_info(file_path)
                        for cc_info in cc_info_list:
                            cc_number, expiration, card_holder = cc_info
                            f.write(f'{cc_number},{expiration},"{card_holder}"\n')
            # Process any "CC.txt" files in the current directory
            for filename in filenames:
                if filename.lower() == 'cc.txt':
                    file_path = os.path.join(dirpath, filename)
                    cc_info_list = extract_cc_info(file_path)
                    for cc_info in cc_info_list:
                        cc_number, expiration, card_holder = cc_info
                        f.write(f'{cc_number},{expiration},"{card_holder}"\n')


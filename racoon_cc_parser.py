import os


# define function to extract credit card information
def extract_cc_info(file_path):
    with open(file_path, 'r') as f:
        contents = f.read()
    cc_info_list = contents.split('\n\n')
    cc_info = []
    for info in cc_info_list:
        if info.strip() == '':
            continue
        cc_number = info.split('CC NUMBER: ')[1].split('\n')[0]
        expiration = info.split('EXPIRATION: ')[1].split('\n')[0]
        card_holder = info.split('CARD HOLDER: ')[1].split('\n')[0]
        cc_info.append((cc_number, expiration, card_holder))
    return cc_info


# define function to process all "CC.txt" files in a directory and its subdirectories
def process_cc(main_folder):
    output_file_path = os.path.join(main_folder, 'merged_cc_info.txt')
    with open(output_file_path, 'w') as f:
        for dirpath, dirnames, filenames in os.walk(main_folder):
            for filename in filenames:
                if filename == 'CC.txt':
                    file_path = os.path.join(dirpath, filename)
                    cc_info_list = extract_cc_info(file_path)
                    for cc_info in cc_info_list:
                        cc_number, expiration, card_holder = cc_info
                        f.write(f'{cc_number},{expiration},"{card_holder}"\n')

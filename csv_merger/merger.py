"""
Please check format validation from this site
http://www.convertcsv.com/csv-viewer-editor.htm

"""

import glob
import csv
import os

# Use these to declare paths and file names
OUTPUT_FOLDER_PATH = "outputs"
INPUT_FOLDER_PATH = ""
RESULT_FILE = "final_result.csv"
PLACE_HOLDER_OWNER_MAIL = "someone@example.com"

files_to_read = []

# This headers are those which suggested to be added in result CSV file
column_names = ['First Name', 'Last Name', 'Title', 'Client Name', 'Direct Phone', 'Main Phone', 'Cell Phone',
                'Permanent Address 1', 'Permanent Address City', 'Permanent Address State',
                'Permanent Address Zip', 'Primary E-mail', 'Skills', 'Contact Owner']


def read_all_csv_files():
    """
    Read all the files having extension .CSV and store names inside @files_to_read

    If no file with CSV extension then won't proceed further
    else call @create_output_file

    :return: None
    """
    global files_to_read
    files_to_read = glob.glob(INPUT_FOLDER_PATH + "*.csv")

    if files_to_read:
        create_output_file()
    else:
        print("There are no CSV files available inside directory")


def create_output_file():
    """
    Creating Result file here, and adding headers as suggested from @column_names
    :return: None
    """

    if not os.path.exists(OUTPUT_FOLDER_PATH):
        os.makedirs(OUTPUT_FOLDER_PATH)

    with open(OUTPUT_FOLDER_PATH + '/' + RESULT_FILE, 'w', newline='') as target_file:
        writer_obj = csv.writer(target_file, delimiter=';')

        writer_obj.writerow(column_names)
        write_all_content(writer_obj)


def write_all_content(writer_obj):
    """
    :param writer_obj: CSV writer object of output file with headers. Here, we will add data from all CSV files
                       listed inside @files_to_read

    :return: None
    """

    for each_file in files_to_read:
        with open(each_file, "r") as current_file_writer:

            d_reader = csv.DictReader(current_file_writer)

            for each_line in d_reader:
                values_to_write = list()

                # For all other columns take value from CSV file.
                for column in column_names:
                    values_to_write.append(each_line.get(column))

                # Here the last column "Contact owner" added by us.Setting place holder value for that
                values_to_write[-1] = PLACE_HOLDER_OWNER_MAIL

                writer_obj.writerow(values_to_write)


if __name__ == "__main__":
    read_all_csv_files()

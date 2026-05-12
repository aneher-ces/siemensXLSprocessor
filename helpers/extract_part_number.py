"""
    Helper to loop through a converted csv file and extract the part number from the description column. The part number is then added to a new column in the csv file. 
"""

import csv

def clean_part_number(part_number):
    # Remove any unwanted characters from the part number
    return part_number.replace('ITEM#', '').replace(',', '').strip()

def extract_part_number(description):
    # Assuming the part number is always in the format "ITEM#XYZ123" within the description
    if 'ITEM#' in description:
        start_index = description.index('ITEM#')
        end_index = description.find(' ', start_index)  # Find the next space after the part number
        if end_index == -1:  # If there is no space, take the rest of the string
            end_index = len(description)
        return clean_part_number(description[start_index:end_index])
    return ''  # Return an empty string if no part number is found

def extract_part_number_from_csv(input_csv, output_csv):
    with open(input_csv, mode='r', encoding='utf-8') as infile, open(output_csv, mode='w', encoding='utf-8', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = list(reader.fieldnames or []) + ['Part Number']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            description = row.get('Item Description', '')
            part_number = extract_part_number(description)
            row['Part Number'] = part_number
            writer.writerow(row)


import csv
from pathlib import Path
from helpers.extract_part_number import extract_part_number_from_csv

def test_extract_part_number(tmp_path):
    # Create a sample CSV file for testing
    input_csv = tmp_path / "test_input.csv"
    output_csv = tmp_path / "test_output.csv"
    
    with open(input_csv, mode='w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Description'])
        writer.writerow(['This is a test description with ITEM#ABC123.'])
        writer.writerow(['No part number here.'])
        writer.writerow(['Another description with ITEM#XYZ789 and more text.'])
    
    # Call the function to extract part numbers
    extract_part_number_from_csv(input_csv, output_csv)
    
    # Read the output CSV and verify the results
    with open(output_csv, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        results = list(reader)
        
        assert results[0]['Part Number'] == 'ABC123'
        assert results[1]['Part Number'] == ''
        assert results[2]['Part Number'] == 'XYZ789'

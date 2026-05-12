import csv
from pathlib import Path
from helpers.extract_part_number import extract_part_number_from_csv

test_dir = Path("tests/test_sample_data")

def test_extract_part_number():
    # Create a sample CSV file for testing
    input_csv = test_dir / "test_input.csv"
    output_csv = test_dir / "test_output.csv"
    
    # with open(input_csv, mode='w', encoding='utf-8', newline='') as f:
    #     writer = csv.writer(f)
    #     writer.writerow(['Description'])
    #     writer.writerow(['This is a test description with ITEM#ABC123.'])
    #     writer.writerow(['No part number here.'])
    #     writer.writerow(['Another description with ITEM#XYZ789 and more text.'])
    
    # Call the function to extract part numbers
    extract_part_number_from_csv(input_csv, output_csv)
    
    # Read the output CSV and verify the results
    with open(output_csv, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        results = list(reader)
        
        assert results[0]['Part Number'] == 'B54-R-38'
        assert results[1]['Part Number'] == 'B54-Y-37'
        assert results[2]['Part Number'] == 'B54-T-104'
        assert results[3]['Part Number'] == 'B54-W-101'
        assert results[4]['Part Number'] == '31.36.1'
        assert results[5]['Part Number'] == 'RP342'
        assert results[6]['Part Number'] == '782L01'
        assert results[7]['Part Number'] == '1212'
        assert results[8]['Part Number'] == '1251'
        assert results[9]['Part Number'] == '378G'
        assert results[10]['Part Number'] == '375GS'
        assert results[11]['Part Number'] == 'TXC1-13ID'
        assert results[12]['Part Number'] == 'SG-59BMD-AF'
        assert results[13]['Part Number'] == 'FPD-500L90'
        assert results[14]['Part Number'] == 'PRP-FB10'
        assert results[15]['Part Number'] == '2760'
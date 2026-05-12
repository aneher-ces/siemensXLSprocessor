# Siemens Part Number Identifier - XLS

For processing excel files to find rows containing a Siemens part number.

## Convert Excel sheets to CSV

Use `main.py` to convert each worksheet in an Excel workbook into CSV files.

Example:

```bash
python main.py input.xlsx
```

To write CSV files into a separate folder:

```bash
python main.py input.xlsx --output-dir output_csv
```

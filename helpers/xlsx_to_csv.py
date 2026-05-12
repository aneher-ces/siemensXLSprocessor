import argparse
from pathlib import Path
import pyexcel as pe


def normalize_sheet_name(sheet_name: str) -> str:
    invalid_chars = '<>:"/\\|?*'
    safe_name = ''.join('_' if ch in invalid_chars else ch for ch in sheet_name)
    return safe_name.strip() or 'sheet'


def convert_excel_to_csv(input_filename: str, output_dir: str | None = None) -> list[str]:
    input_path = Path(input_filename)
    if not input_path.exists():
        raise FileNotFoundError(f"Input file does not exist: {input_filename}")

    output_path = Path(output_dir or input_path.parent)
    output_path.mkdir(parents=True, exist_ok=True)

    book = pe.get_book(file_name=str(input_path))
    sheet_names = book.sheet_names()
    output_files: list[str] = []
    base_name = input_path.stem

    for sheet in book:
        safe_name = normalize_sheet_name(sheet.name)
        csv_name = (
            f"{base_name}_{safe_name}.csv"
            if len(sheet_names) > 1
            else f"{base_name}.csv"
        )
        out_file = output_path / csv_name
        sheet.save_as(str(out_file))
        output_files.append(str(out_file))

    return output_files


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert each sheet in an Excel file into one or more CSV files."
    )
    parser.add_argument("input_file", help="Path to the Excel file to convert.")
    parser.add_argument(
        "--output-dir",
        "-o",
        help="Directory to save generated CSV files. Defaults to the input file directory.",
        default=None,
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    converted_files = convert_excel_to_csv(args.input_file, args.output_dir)
    print("Wrote CSV files:")
    for path in converted_files:
        print(path)

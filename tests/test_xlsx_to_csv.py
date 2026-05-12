import pyexcel as pe
from pathlib import Path
from helpers.xlsx_to_csv import convert_excel_to_csv


def create_excel_file(path: Path, bookdict):
    pe.save_book_as(bookdict=bookdict, dest_file_name=str(path))


def test_convert_excel_to_csv_multiple_sheets(tmp_path):
    input_path = tmp_path / "test.xlsx"
    create_excel_file(
        input_path,
        {
            "Sheet1": [["A", "B"], [1, 2]],
            "Second": [["X", "Y"], [3, 4]],
        },
    )

    output_dir = tmp_path / "csv_output"
    result = convert_excel_to_csv(str(input_path), str(output_dir))

    assert len(result) == 2
    assert (output_dir / "test_Sheet1.csv").exists()
    assert (output_dir / "test_Second.csv").exists()
    assert all(Path(path).suffix == ".csv" for path in result)


def test_convert_excel_to_csv_single_sheet(tmp_path):
    input_path = tmp_path / "single.xlsx"
    create_excel_file(input_path, {"Sheet1": [["A", "B"], [1, 2]]})

    output_dir = tmp_path / "csv_output"
    result = convert_excel_to_csv(str(input_path), str(output_dir))

    assert result == [str(output_dir / "single.csv")]
    assert (output_dir / "single.csv").exists()

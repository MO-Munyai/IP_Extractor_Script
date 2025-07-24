# xl ip extractor - fetch_ip.py

This script extracts all unique IPv4 addresses from an Excel file and saves them to a text file.

## How It Works

- Loads an Excel file using pandas.
- Scans every cell for IPv4 addresses using a regular expression.
- Collects all unique IPs found.
- Appends the sorted list of IPs to `ip_list.txt`.

## Usage

1. Place your Excel file in the same directory as the script.
2. Rename your Excel file to `file_name.xlsx` or update the script with your file's name.
3. Run the script:

    ```sh
    python fetch_ip.py
    ```

4. The extracted IPs will be saved in `ip_list.txt`.

## Requirements

- Python 3.x
- pandas
- openpyxl (for .xlsx files)

Install dependencies:

```sh
pip install pandas openpyxl
```

## Notes

- The script appends to `ip_list.txt` by default. Delete or rename the file before running if you want a fresh list.
- Only IPv4 addresses are extracted.

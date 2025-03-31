# Pocket Exported Links Converter

Convert your Pocket bookmarks export (CSV) to formats that can be imported into another bookmarking tool like Linkwarden.

## Requirements

- Python 3.6 or higher

## Usage

This repository provides two conversion scripts:

### 1. Convert to HTML Bookmarks (Netscape format)

```bash
python pocket_to_html.py path/to/pocket_export.csv [output_file.html]
```

If you don't specify an output file, it will default to `pocket_bookmarks.html`.

### 2. Convert to Wallabag-like JSON format

```bash
python pocket_to_wallabag_json.py path/to/pocket_export.csv [output_file.json]
```

If you don't specify an output file, it will default to `pocket_wallabag.json`.

## Example

```bash
# Convert using the HTML converter
python pocket_to_html.py part_000000.csv my_bookmarks.html

# Convert using the JSON/Wallabag converter
python pocket_to_wallabag_json.py part_000000.csv my_bookmarks.json
```

## Importing into Linkwarden

1. Go to Linkwarden's dashboard
2. Navigate to the import section
3. Choose the appropriate import format:
   - For HTML file: Select the HTML option
   - For JSON file: Select the Wallabag option
4. Upload your converted file and follow the import instructions

## Notes

- The HTML format is more widely supported and may provide better compatibility
- The JSON format includes additional metadata like archiving status

#!/usr/bin/env python3
import csv
import json
import sys
from datetime import datetime

def convert_pocket_to_wallabag_json(csv_file, json_file):
    """Convert Pocket CSV export to Wallabag-like JSON format."""
    
    entries = []
    
    # Read CSV file
    with open(csv_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            title = row['title'] or row['url']
            url = row['url']
            added_timestamp = int(row['time_added'])
            added_date = datetime.fromtimestamp(added_timestamp).strftime('%Y-%m-%dT%H:%M:%SZ')
            tags = row['tags'].split(',') if row['tags'] else []
            is_archived = row['status'] == 'archive'
            
            entry = {
                "title": title,
                "url": url,
                "created_at": added_date,
                "tags": tags,
                "archived": is_archived,
                "is_starred": False,
                "content": "",  # Pocket doesn't provide content in the export
                "language": "en"  # Default language
            }
            
            entries.append(entry)
    
    # Write to JSON file
    with open(json_file, 'w') as f:
        json.dump(entries, f, indent=2)
    
    print(f"Conversion complete. Wallabag-like JSON file saved as {json_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pocket_to_wallabag_json.py [csv_file] [json_file]")
        print("If json_file is not specified, it will default to pocket_wallabag.json")
        sys.exit(1)
        
    csv_file = sys.argv[1]
    json_file = sys.argv[2] if len(sys.argv) > 2 else "pocket_wallabag.json"
    
    convert_pocket_to_wallabag_json(csv_file, json_file)
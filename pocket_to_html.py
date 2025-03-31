#!/usr/bin/env python3
import csv
import html
import sys
from datetime import datetime

def convert_pocket_to_html(csv_file, html_file):
    """Convert Pocket CSV export to HTML bookmarks format."""
    
    with open(html_file, 'w') as f:
        # Write HTML header
        f.write('''<!DOCTYPE NETSCAPE-Bookmark-file-1>
<!-- This is an automatically generated file.
     It will be read and overwritten.
     DO NOT EDIT! -->
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<TITLE>Bookmarks</TITLE>
<H1>Bookmarks</H1>
<DL><p>
    <DT><H3 ADD_DATE="{0}" LAST_MODIFIED="{0}">Pocket</H3>
    <DL><p>
'''.format(int(datetime.now().timestamp())))

        # Read CSV file
        with open(csv_file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                title = html.escape(row['title'] or row['url'])
                url = html.escape(row['url'])
                added_time = row['time_added']
                tags = row['tags']
                
                tag_attr = f' TAGS="{html.escape(tags)}"' if tags else ''
                status = row['status']
                
                f.write(f'        <DT><A HREF="{url}" ADD_DATE="{added_time}"{tag_attr}>{title}</A>\n')
                
        # Write HTML footer
        f.write('''    </DL><p>
</DL><p>
''')

    print(f"Conversion complete. HTML bookmarks file saved as {html_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pocket_to_html.py [csv_file] [html_file]")
        print("If html_file is not specified, it will default to pocket_bookmarks.html")
        sys.exit(1)
        
    csv_file = sys.argv[1]
    html_file = sys.argv[2] if len(sys.argv) > 2 else "pocket_bookmarks.html"
    
    convert_pocket_to_html(csv_file, html_file)
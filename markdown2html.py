#!/usr/bin/python3
"""transform markdown to html"""
import sys
import os


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)
    if not os.path.isfile(sys.argv[1]):
        sys.stderr.write(f"Missing {sys.argv[1]}\n")
        sys.exit(1)

    markdown_file = sys.argv[1]
    html_file = sys.argv[2]
    html_output = ''

    with open(markdown_file, 'r') as file:
        lines = file.readlines()
        for l in lines:
            if l.startswith('#'):
                heading_level = l.count('#')
                heading_text = l.strip('#').strip()
                heading_html = f'<h{heading_level}>' + \
                    f'{heading_text}</h{heading_level}>\n'
                html_output += heading_html

    with open(html_file, 'w') as file:
        file.write(html_output)

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

        i = 0
        while i < len(lines):
            if lines[i].startswith('#'):
                heading_level = lines[i].count('#')
                heading_text = lines[i].strip('#').strip()
                heading_html = f'<h{heading_level}>' + \
                    f'{heading_text}</h{heading_level}>\n'
                html_output += heading_html

            elif lines[i].startswith('-'):
                if html_output != '':
                    html_output += '<ul>\n'
                else:
                    html_output += '<ul>\n'

                while i < len(lines) and lines[i].startswith('-'):
                    text_el = lines[i].strip('-').strip()
                    html_el_li = f'<li>{text_el}</li>\n'
                    html_output += html_el_li
                    i += 1
                html_output += '</ul>\n'
            i += 1

    with open(html_file, 'w') as file:
        file.write(html_output)

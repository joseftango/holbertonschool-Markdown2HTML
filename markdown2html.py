#!/usr/bin/python3
"""create a markdown2html.py that takes two arguments"""
from sys import argv, stderr, exit
from os.path import exists
from markdown import markdown


if __name__ == '__main__':
    """calling function convert_to_html"""
    def convert_to_html():
        """function that convert markdown to html"""
        num_of_arg = len(argv[1:])
        if num_of_arg < 2:
            stderr.write('Usage: ./markdown2html.py README.md README.html\n')
            exit(1)
        if not exists(f'{argv[1]}'):
            stderr.write(f'Missing {argv[1]}\n')
            exit(1)
        else:
            markdown_file = argv[1]
            html_file = argv[2]
            with open(markdown_file, "r") as file:
                content = file.read()
                html = markdown(content)
            with open(html_file, 'w') as f:
                f.write(html + '\n')

    convert_to_html()

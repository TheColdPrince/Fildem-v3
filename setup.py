import setuptools
import os
import sys

import fildem

with open('README.md', 'r') as fh:
    long_description = fh.read()


def fildem_startup():
    return input("Would you like to run fildem on startup? [Y/N]: ").lower()


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "install":
        response = fildem_startup()
        if response in ("y", "yes"):
            os.system("mv ./fildemstartup/* ~/.config/autostart/")
        elif response in ("n", "no"):
            print("")
        else:
            # Ask the question again
            main()


main()

setuptools.setup(
    name='fildem',
    version=fildem.__version__,
    author='Gonzalo',
    author_email='gonzaarcr@gmail.com',
    description='Fildem Global Menu for Gnome Desktop',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/gonzaarcr/Fildem',
    packages=setuptools.find_packages(),
    install_requires=[
        'PyGObject>=3.30.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux'
    ],
    project_urls={
        'Bug Reports': 'https://github.com/gonzaarcr/Fildem/issues',
        'Source': 'https://github.com/gonzaarcr/Fildem',
    },
    entry_points={
        'console_scripts': [
            'fildem = fildem.run:main',
        ]
    }
)

# Python-Instagram-Un_Followers

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

Simple python program to get the list of users on Instagram who don't follow you back and who you don't follow back.

## Usage:

1. Run the program

2. Enter your Instagram username and password

3. You will be prompted to save your username and password in `config.ini` to prevent asking for them again. Do not
   directly enter your username and password in `config.ini` (Optional)

4. Add the usernames of accounts that you want to be excluded (e.g., meme pages, celebrities) in `exceptions.txt`
   separated by newline (Optional)

5. You can set `include_exceptions` to `True` or `False` in `config.ini`. Set to `False` by default (Optional)

6. You can set `show_who_you_do_not_follow` to `True` or `False` in `config.ini`. Set to `True` by default (Optional)

## Dependencies:

- [instaloader](https://pypi.org/project/instaloader/) is used for authenticating and retrieving data from Instagram

# Python-Instagram-Un_Followers

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

Simple python program to get the list of users who are not following you back on Instagram.

## Usage:

1. Change `testusername` in `config.ini` to your own username

2. Change `testpassword` in `config.ini` to your own password

3. Add the usernames of accounts that you want to be excluded (e.g., meme pages, celebrities) in `exceptions.txt`
   separated by newline (Optional)

4. You can set `ignore_exceptions` to `True` or `False` in `config.ini`. Set to `True` by default (Optional)

5. Run the program

## Dependencies:

- [instaloader](https://pypi.org/project/instaloader/) is used for authenticating and retrieving data from Instagram

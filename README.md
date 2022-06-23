# Python-Instagram-Un_Followers

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

Simple python program to get the list of users on Instagram who don't follow you back and who you don't follow back.

## Usage:

1. Run the program

2. Enter your Instagram username and password

3. You will be prompted to save your username and password in `config.ini` to prevent asking for them again. Do not
   directly enter your username and password in `config.ini` (Optional)

## Features:

1. Display usernames of accounts that do not follow you back
    - You can hide this by setting `show_who_do_not_follow_you` to False in `config.ini`

2. Manually exclude selected accounts from list of users who do not follow you back
    - Add the usernames of accounts that you want to be excluded in `exceptions.txt` separated by newline
    - Usernames in the file will not be included when `include_exceptions`  is set to `False` in `config.ini`
    - If there are users that do no follow you back, you will be prompted to add all of them at once or one by one
      automatically to `exceptions.txt`. You can disable this prompt by setting `ask_to_add_to_exceptions` to False
      in `config.ini`
    - Accounts in `exceptions.txt` that you no longer follow will automatically be removed from it. You can disable this
      by setting
      `remove_obsolete_exceptions` to False in `config.ini`
    - Accounts in `exceptions.txt` will be sorted alphabetically when they are added. You can disable this by setting
      `sort_exceptions` to False in `config.ini`

3. Display usernames of accounts that you do not follow back
    - You can hide this by setting `show_who_you_do_not_follow` to False in `config.ini`

4. Display follower and following count of the user
    - You can hide this by setting `show_follower_following_count` to False in `config.ini`

5. You can disable verbose messages by setting `show_verbose_messages` to `False` in `config.ini`

## Dependencies:

- [instaloader](https://pypi.org/project/instaloader/) is used for authenticating and retrieving data from Instagram

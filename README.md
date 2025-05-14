# Python-Instagram-Un_Followers

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

Simple python program to get the list of users on Instagram who don't follow you back and who you don't follow back.

## Usage:

1. Log in to your Instagram account in your web browser and save your logged in status

2. Retrieve your Instagram browser cookies. [[Example Guide]](https://www.cookieyes.com/blog/how-to-check-cookies-on-your-website-manually/)

3. Open the `config.ini` file

4. Locate the `[credentials]` section and set `username` to your own (e.g., `username = your_instagram_username`)

5. Locate the `[cookie]` section and paste the retrieved cookie values corresponding to each key (e.g., `csrftoken`,
   `sessionid`, etc.)

6. Run the program

## Features:

1. Display usernames of accounts that do not follow you back
    - You can hide this by setting `show_who_do_not_follow_you` to `False` in `config.ini`

2. Manually exclude selected accounts from list of users who do not follow you back
    - Add the usernames of accounts that you want to be excluded in `exceptions.txt` separated by newline
    - Usernames in the file will not be included when `include_exceptions` is set to `False` in `config.ini`
    - If there are users that do no follow you back, you will be prompted to add all of them at once or one by one
      automatically to `exceptions.txt`
        - You can disable this prompt by setting `ask_to_add_to_exceptions` to `False`in `config.ini`
    - Accounts in `exceptions.txt` that you no longer follow will automatically be removed from it
        - You can disable this by setting `remove_obsolete_exceptions` to `False` in `config.ini`

3. Display usernames of accounts that you do not follow back
    - You can hide this by setting `show_who_you_do_not_follow` to `False` in `config.ini`

4. Display follower and following count of the user
    - You can hide this by setting `show_follower_following_count` to `False` in `config.ini`

5. Display the change in your followers since the last run

    - You can hide this by setting `show_changes_in_followers` to `False` in `config.ini`

6. Display the change in your following since the last run

    - You can hide this by setting `show_changes_in_following` to `False` in `config.ini`

7. Accounts when displayed and saved in any file will be sorted alphabetically
    - You can disable this by setting `sort_accounts` to `False` in `config.ini`

8. You can disable verbose messages by setting `show_verbose_messages` to `False` in `config.ini`

## Disclaimer:

> #### This software is in no way affiliated with, authorized, maintained or endorsed by Instagram or any of its affiliates or subsidiaries
>
> #### This is purely an enthusiast program intended for educational purposes only
>
> #### By downloading this software you acknowledge that you are using this at your own risk and that I am is not responsible for any damages that may occur to you due to the usage or installation of this program
>
> #### Potential consequences include but are not limited to account restrictions, permanent bans and legal action

## Dependencies:

- [instaloader](https://pypi.org/project/instaloader/) is used for authenticating and retrieving data from Instagram

from configparser import RawConfigParser
from secrets import compare_digest

from instaloader.instaloader import Instaloader, Profile

version: str = '2.7.1'

config_parser: RawConfigParser = RawConfigParser()
config_parser.read('config.ini')

username: str = config_parser.get('credentials', 'username')
username_not_set: bool = compare_digest(username, 'testusername')
if username_not_set:
    username = input('Enter your username: ')
else:
    username = eval(username).decode('utf-16')

password: str = config_parser.get('credentials', 'password')
password_not_set: bool = compare_digest(password, 'testpassword')
if password_not_set:
    password = input('Enter your password: ')
else:
    password = eval(password).decode('utf-16')

if username_not_set or password_not_set:
    print('Save Username/Password in config.ini? [y/n]')
    if input().lower() == 'y':
        config_parser.set('credentials', 'username', str(username.encode('utf-16')))
        config_parser.set('credentials', 'password', str(password.encode('utf-16')))
        with open('config.ini', 'w') as config:
            config_parser.write(config)
        print('Username/Password saved in config.ini')

show_verbose_messages: bool = config_parser.getboolean('settings', 'show_verbose_messages')


def verbose(message: str) -> None:
    if show_verbose_messages:
        print(message)


verbose('Attempting to log in')
loader: Instaloader = Instaloader()
loader.login(username, password)
verbose('Logged in successfully')
verbose('Retrieving profile information')
profile: Profile = Profile.from_username(loader.context, username)

verbose('Retrieving following and follower list\n')
follower_list: list[str] = [follower.username for follower in profile.get_followers()]
following_list: list[str] = [followee.username for followee in profile.get_followees()]

show_follower_following_count: bool = config_parser.getboolean('settings', 'show_follower_following_count')
if show_follower_following_count:
    print('Followers:', len(follower_list))
    print('Following:', len(following_list))

show_who_you_do_not_follow: bool = config_parser.getboolean('settings', 'show_who_you_do_not_follow')
verbose(f"\nUsers who you don't follow back will be {'ex' if not show_who_you_do_not_follow else 'in'}cluded")
unfollowing_list: list[str] = []

show_who_do_not_follow_you: bool = config_parser.getboolean('settings', 'show_who_do_not_follow_you')
verbose(f"\nUsers who don't follow you back will be {'ex' if not show_who_do_not_follow_you else 'in'}cluded")
unfollower_list: list[str] = []

if show_who_you_do_not_follow:
    for follower in follower_list:
        if follower not in following_list:
            unfollowing_list.append(follower)

    print(f"\nUsers who you don't follow back: {len(unfollowing_list)}")
    for followee in unfollowing_list:
        print(followee)

if show_who_do_not_follow_you:
    include_exceptions: bool = config_parser.getboolean('settings', 'include_exceptions')
    exception_list: list[str] = []
    if not include_exceptions:
        try:
            exception_list = open('exceptions.txt').read().split('\n')
            verbose('\nFound exceptions.txt')
            while '' in exception_list:
                exception_list.remove('')
        except FileNotFoundError:
            verbose('No exceptions.txt file found')
            include_exceptions = True

    verbose(f'Exceptions will be {"ex" if not include_exceptions else "in"}cluded')

    for followee in following_list:
        if followee not in follower_list:
            if not include_exceptions:
                if followee not in exception_list:
                    unfollower_list.append(followee)
            else:
                unfollower_list.append(followee)

    print(f"\nUsers who don't follow you back ({'ex' if not include_exceptions else 'in'}cluding exceptions): "
          f"{len(unfollower_list)}")
    for unfollower in unfollower_list:
        print(unfollower)

ask_to_add_to_exceptions: bool = config_parser.getboolean('settings', 'ask_to_add_to_exceptions')

# noinspection PyUnboundLocalVariable
if show_who_do_not_follow_you and ask_to_add_to_exceptions and not include_exceptions:
    remove_obsolete_exceptions: bool = config_parser.getboolean('settings', 'remove_obsolete_exceptions')
    if remove_obsolete_exceptions:
        obsolete_accounts_to_remove: list[str] = []
        # noinspection PyUnboundLocalVariable
        for account in exception_list:
            if account not in following_list:
                obsolete_accounts_to_remove.append(account)
        with open('exceptions.txt') as exceptions:
            accounts_to_update = exceptions.readlines()
            for account in obsolete_accounts_to_remove:
                accounts_to_update.remove(account + '\n')
        with open('exceptions.txt', 'w') as exceptions:
            exceptions.writelines(accounts_to_update)
        verbose('\nRemoved accounts you no longer follow from exceptions.txt')

# noinspection PyUnboundLocalVariable
if show_who_do_not_follow_you and ask_to_add_to_exceptions and not include_exceptions and len(unfollower_list) > 0:
    print('\nAdd all users who don\'t follow you back to exceptions.txt? [y/n]')
    add_to_exceptions: bool = True if input().lower() == 'y' else False
    if add_to_exceptions:
        with open('exceptions.txt', 'a+') as exceptions:
            for unfollower in unfollower_list:
                exceptions.write(f'{unfollower}\n')
        verbose('Added all users who don\'t follow you back to exceptions.txt')
    else:
        print('\nAdd selected users who don\'t follow you back to exceptions.txt? [y/n]')
        add_selected_to_exceptions: bool = True if input().lower() == 'y' else False
        if add_selected_to_exceptions:
            with open('exceptions.txt', 'a+') as exceptions:
                for unfollower in unfollower_list:
                    print(f'Add {unfollower} to exceptions.txt? [y/n]')
                    if input().lower() == 'y':
                        exceptions.write(f'{unfollower}\n')
                        verbose(f'Added {unfollower} to exceptions.txt')
                    else:
                        verbose(f'Skipped {unfollower}')
    # noinspection PyUnboundLocalVariable
    if add_to_exceptions or add_selected_to_exceptions:
        sort_exceptions: bool = config_parser.getboolean('settings', 'sort_exceptions')
        if sort_exceptions:
            with open('exceptions.txt') as exceptions:
                accounts_to_sort = exceptions.readlines()
                accounts_to_sort.sort()
            with open('exceptions.txt', 'w') as exceptions:
                exceptions.writelines(accounts_to_sort)
            verbose('Sorted exceptions.txt')

from configparser import ConfigParser
from secrets import compare_digest

from instaloader.instaloader import Instaloader, Profile

version: str = '2.0.0'

config_parser: ConfigParser = ConfigParser()
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

print('Attempting to log in')
loader: Instaloader = Instaloader()
loader.login(username, password)
print('Logged in successfully')
print('Retrieving profile information')
profile: Profile = Profile.from_username(loader.context, username)

print('Retrieving following and follower list\n')
follower_list: list[str] = [follower.username for follower in profile.get_followers()]
following_list: list[str] = [followee.username for followee in profile.get_followees()]

show_follower_following_count: bool = config_parser.getboolean('settings', 'show_follower_following_count')
if show_follower_following_count:
    print('Followers:', len(follower_list))
    print('Following:', len(following_list))

unfollower_list: list[str] = []

show_who_you_do_not_follow: bool = config_parser.getboolean('settings', 'show_who_you_do_not_follow')
print(f"\nUsers who you don't follow back will be {'ex' if not show_who_you_do_not_follow else 'in'}cluded")
unfollowing_list: list[str] = []

include_exceptions: bool = config_parser.getboolean('settings', 'include_exceptions')
exception_list: list[str] = []
if not include_exceptions:
    try:
        exception_list = open('exceptions.txt', 'r').read().split('\n')
        print('Found exceptions.txt')
        while '' in exception_list:
            exception_list.remove('')
    except FileNotFoundError:
        print('No exceptions.txt file found')
        include_exceptions = True
        pass

print(f'Exceptions will be {"ex" if not include_exceptions else "in"}cluded')

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

if show_who_you_do_not_follow:
    for follower in follower_list:
        if follower not in following_list:
            unfollowing_list.append(follower)

    print(f"\nUsers who you don't follow back: {len(unfollowing_list)}")
    for followee in unfollowing_list:
        print(followee)

from configparser import ConfigParser

from instaloader.instaloader import Instaloader, Profile

version: str = '1.0.0'

config_parser: ConfigParser = ConfigParser()
config_parser.read('config.ini')

username: str = config_parser.get('main', 'username')
password: str = config_parser.get('main', 'password')

print('Attempting to log in')
loader: Instaloader = Instaloader()
loader.login(username, password)
print('Logged in successfully')
print('Retrieving profile information')
profile: Profile = Profile.from_username(loader.context, username)

print('Retrieving following and follower list\n')
follower_list: list[str] = [follower.username for follower in profile.get_followers()]
following_list: list[str] = [followee.username for followee in profile.get_followees()]
print('Followers:', len(follower_list))
print('Following:', len(following_list))
unfollower_list: list[str] = []

show_who_you_do_not_follow: bool = config_parser.getboolean('main', 'show_who_you_do_not_follow')
print(f"\nUsers who you don't follow back will be {'ex' if not show_who_you_do_not_follow else 'in'}cluded")
unfollowing_list: list[str] = []

include_exceptions: bool = config_parser.getboolean('main', 'include_exceptions')
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

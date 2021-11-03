from configparser import ConfigParser

from instaloader.instaloader import Instaloader, Profile

config_parser: ConfigParser = ConfigParser()
config_parser.read('config.ini')

username: str = config_parser.get('main', 'username')
password: str = config_parser.get('main', 'password')

loader: Instaloader = Instaloader()
loader.login(username, password)
profile: Profile = Profile.from_username(loader.context, username)

follower_list: list[str] = [follower.username for follower in profile.get_followers()]
following_list: list[str] = [followee.username for followee in profile.get_followees()]
unfollower_list: list[str] = []

exception_list: list[str] = []
try:
    exception_list = open('exceptions.txt', 'r').read().split('\n')
    while '' in exception_list:
        exception_list.remove('')
except FileNotFoundError:
    pass

ignore_exceptions: bool = config_parser.getboolean('main', 'ignore_exceptions')

for followee in following_list:
    if followee not in follower_list:
        if not ignore_exceptions:
            if followee not in exception_list:
                unfollower_list.append(followee)
        else:
            unfollower_list.append(followee)

print(f'Unfollowers (with{"out" if not ignore_exceptions else ""} exceptions):')
if len(unfollower_list) == 0:
    print('There are no unfollowers')

for unfollower in unfollower_list:
    print(unfollower)

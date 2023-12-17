import requests
from colorama import Fore, Style



def get_github_profile(username):
    url = f'https://api.github.com/users/{username}'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None


def display_github_profile(data):
    if data:
        for info in data:
            if info.endswith('url'):
                print(f'{Fore.GREEN}{info}:{Style.RESET_ALL} {Fore.CYAN}{data[info]}{Style.RESET_ALL}')
    else:
        print(f'{Fore.RED}User Not Found!{Style.RESET_ALL}')



if __name__ == '__main__':
    username = input(f'{Fore.LIGHTRED_EX}Enter Github Username: {Style.RESET_ALL}')
    data = get_github_profile(username)
    display_github_profile(data)

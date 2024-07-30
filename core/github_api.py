import requests


def get_contributions(username, year):
    url = f"https://github-contributions-api.jogruber.de/v4/{username}?y={year}"

    req = requests.get(url)
    return req.json()['contributions']




if __name__ == '__main__':
    x = get_contributions("doctorixx", 2024)
    print(x)

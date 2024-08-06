import argparse

from core import process_github_stats

parser = argparse.ArgumentParser(
    prog='skyline_wizard',
    description='Utility to generate 3d github skylines models',
    epilog='by Doctorixx(https://github.com/doctorixx)')

parser.add_argument('-f', '--filename', dest="filename")
parser.add_argument('-u', '--username', dest="username")
parser.add_argument('-y', '--year', dest="year")


def cli_mode(parsed):
    filename = parsed.filename
    username = parsed.nickname
    year = parsed.year

    if filename is None:
        filename = f"{username}-{year}.stl"

    process_github_stats(username, year, filename)


def ui_mode():
    print("Welcome to github-skyline generator By doctorixx \n")
    print("Enter github username")
    username = input("> ")
    print("Enter year")
    year = input("> ")
    filename = f"{username}-{year}.stl"
    print("[/] Generation started")
    process_github_stats(username, year, filename)
    print("[+] Generation completed")
    print(f"[+] Saved to file {filename}")
    print("Press enter to exit...")
    input()


if __name__ == '__main__':
    parsed = parser.parse_args()
    used_cli_attrs = any(
        map(lambda attr: parsed.__getattribute__(attr), filter(lambda x: not x.startswith("_"), dir(parsed)))
    )

    if used_cli_attrs:
        cli_mode(parsed)
    else:
        ui_mode()

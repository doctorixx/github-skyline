import argparse
from art import tprint
import colorama
from colorama import Back, Fore

from github_skyline.core import process_github_stats

parser = argparse.ArgumentParser(
    prog='skyline_wizard',
    description='Utility to generate 3d github skylines models',
    epilog='by Doctorixx(https://github.com/doctorixx)')

parser.add_argument('-f', '--filename', dest="filename")
parser.add_argument('-u', '--username', dest="username")
parser.add_argument('-y', '--year', dest="year")


def cli_mode(parsed):
    filename = parsed.filename
    username = parsed.username
    year = parsed.year

    if filename is None:
        filename = f"{username}-{year}.stl"

    process_github_stats(username, year, filename)


def ui_mode():
    colorama.init()

    print(Fore.BLUE)
    tprint("github-skyline")
    print(Fore.RESET)

    print(Fore.BLACK + Back.MAGENTA, end="")
    print("Welcome to github-skyline generator By doctorixx", end="")
    print(Fore.RESET + Back.RESET, "\n")

    print(Fore.BLACK + Back.WHITE, end="")
    print("Enter github username", end="")
    print(Fore.RESET + Back.RESET)
    username = input("> ")
    print()

    print(Fore.BLACK + Back.WHITE, end="")
    print("Enter year", end="")
    print(Fore.RESET + Back.RESET)
    year = input("> ")
    print()

    filename = f"{username}-{year}.stl"
    print(Fore.YELLOW, end="")
    print("[/] Generation started")
    print(Fore.RESET, end="")
    process_github_stats(username, year, filename)

    print(Fore.GREEN, end="")
    print("[+] Generation completed")
    print(Fore.RESET, end="")

    print(Fore.GREEN, end="")
    print(f"[+] Saved to file ", end="")
    print(Fore.LIGHTGREEN_EX + Back.RESET, end="")
    print(filename, end="")
    print(Fore.RESET + Back.RESET)

    print(Fore.CYAN, end="")
    print("Press enter to exit...")
    print(Fore.RESET, end="")

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

from core import process_github_stats

print("Welcome to github-skyline generator By doctorixx \n")
print("Enter github username")
username = input("> ")  # CHANGE TO YOUR USERNAME
print("Enter year")
year = input("> ")  # CHANGE TO YOUR YEAR
filename = f"{username}-{year}.stl"  # <- Generated filename
print("[/] Generation started")
process_github_stats(username, year, filename)
print("[+] Generation completed")
print(f"[+] Saved to file {filename}")
print("Press enter to exit...")
input()


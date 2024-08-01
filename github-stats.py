from core import process_github_stats

if __name__ == '__main__':
    username = "doctorixx"  # CHANGE TO YOUR USERNAME
    year = "2023"  # CHANGE TO YOUR YEAR
    filename = f"{username}-{year}.stl"  # <- Generated filename

    process_github_stats(username, year, filename)

from core import process_github_stats

if __name__ == '__main__':
    username = "doctorixx"
    year = "2022"
    filename = f"{username}.stl"

    process_github_stats(username, year, filename)

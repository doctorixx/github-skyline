from core import process_github_stats

if __name__ == '__main__':
    username = "phenixrat007"
    year = "2017"
    filename = f"{username}-{year}.stl"

    process_github_stats(username, year, filename)

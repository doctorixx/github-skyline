# Github Skyline (Alternative)  ![](https://img.shields.io/badge/export-stl-blue)

Alternative of https://skyline.github.com/

This program generate 3d graph of your contributions to GitHub platform
___
![](images/render.png "Github skyline render")
___

## Usage

- Go to the latest release and select your platform
![](images/release_assets.png "Github skyline render")
- Download your system archive
- Unzip archive


### Windows
![](images/windows_open.png "Github skyline render")

- Double-click on downloaded file

![](images/windows_work_example.png "Github skyline render")

### Linux and Mac

- Run the download binary

```shell
./skyline-wizard.bin
```

![](images/linux_run_example.png "Github skyline render")


## Python usage

- Clone this repo

```shell
git clone https://github.com/doctorixx/github-skyline.git
cd github-skyline
```

- Install all python requirements

```shell
pip install -r requirement.txt
```

- Change variables (in **github-stats.py**)

```python
from core import process_github_stats

if __name__ == '__main__':
    username = "doctorixx"  # CHANGE TO YOUR USERNAME
    year = "2023"  # CHANGE TO YOUR YEAR
    filename = f"{username}-{year}.stl"  # <- Generated filename

    process_github_stats(username, year, filename)
```

- run **github-stats.py**

> Linux/MacOS:
> ```shell
> python3 github-stats.py
> ```
> Windows:
> ```shell
> python github-stats.py
> ```

Check "*.stl" fies in project root

![](images/stl_file.png "Stl file in explorer")

## Developments builds
You can find developments build in GitHub Actions  

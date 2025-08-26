# GitHub Skyline (Alternative)

![Export STL](https://img.shields.io/badge/export-stl-blue)
[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

**An alternative implementation of [GitHub Skyline](https://skyline.github.com/) that generates 3D models of your GitHub contribution history.**

Transform your GitHub contributions into stunning 3D landscapes that you can 3D print, display, or share!

![GitHub Skyline Render](images/render.png)

---

## ✨ Features

- 🎯 **Faithful Design**: Follows the original GitHub Skyline design (unlike the official CLI)
- 🖥️ **Multiple Interfaces**: GUI, CLI, and Python library support
- 📦 **Cross-Platform**: Works on Windows, macOS, and Linux
- 🎨 **STL Export**: Ready-to-print 3D models
- 🚀 **Easy Installation**: Simple pip install or standalone binaries

## 🚀 Quick Start

### Installation

```bash
pip install github-skyline
```

### Generate Your Skyline

**GUI Mode:**
```bash
python -m github_skyline
```
![img.png](images/gui_example.png)


**CLI Mode:**
```bash
python -m github_skyline --help
python -m github_skyline -u your-username -y 2024
```

## 📖 Detailed Usage

### Method 1: Python Package (Recommended)

1. **Install the package:**
   ```bash
   pip install github-skyline
   ```

2. **Launch GUI:**
   ```bash
   python -m github_skyline
   ```

3. **Or use CLI:**
   ```bash
   python -m github_skyline -u your-username -y 2024
   ```

### [DEPRECATED] Method 2: Standalone Binaries

1. **Download:** Go to [Releases](https://github.com/doctorixx/github-skyline/releases) and download the appropriate binary for your system:

   ![Release Assets](images/release_assets.png)

2. **Extract** the downloaded archive

3. **Run the application:**

   **Windows:**
   - Double-click `skyline-wizard.exe`
   
   ![Windows Example](images/windows_work_example.png)

   **macOS/Linux:**
   ```bash
   ./skyline-wizard.bin
   ```
   
   ![Linux Example](images/linux_run_example.png)

## 🔧 CLI Options

![CLI Options](images/cli_options.png)

### Available Commands

| Option | Description | Example |
|--------|-------------|---------|
| `-u, --username` | GitHub username | `-u doctorixx` |
| `-y, --year` | Year to generate | `-y 2024` |
| `-o, --output` | Output filename | `-o my-skyline.stl` |
| `-h, --help` | Show help message | `--help` |

### Examples

```bash
# Generate skyline for user 'doctorixx' for 2024
python -m github_skyline -u doctorixx -y 2024

# Custom output filename
python -m github_skyline -u doctorixx -y 2024 -o my-contributions.stl
```

> **Official CLI Differences:** While GitHub has released an [official CLI tool](https://github.com/github/gh-skyline), it uses a different design. This project maintains compatibility with the original GitHub Skyline website design.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Support

- 🐛 **Bug Reports:** [Open an issue](https://github.com/doctorixx/github-skyline/issues)
- 💡 **Feature Requests:** [Start a discussion](https://github.com/doctorixx/github-skyline/discussions)
- 📧 **Questions:** Check existing issues or start a new discussion

## 🎉 Showcase

Share your GitHub Skylines! Tag us or open a discussion to show off your 3D printed contributions.

---

**Made with ❤️ by the community | Star ⭐ this repo if you find it useful!**

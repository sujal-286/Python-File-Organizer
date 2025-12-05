# Smart File Organizer

A Python script that automatically organizes your cluttered directories (like Downloads or Desktop) by sorting files into categories based on their extensions.

## Features
- **Auto-Categorization**: Sorts files into Images, Documents, Archives, Video, Audio, etc.
- **Customizable**: Edit `config.json` to add your own categories and extensions.
- **Safe**: Handles duplicate filenames by timestamping instead of overwriting.
- **Detailed Reporting**: Tells you exactly what was moved.

## Setup
1. Ensure you have Python installed.
2. Clone this repository.
3. (Optional) Customize `config.json`.

## Usage
Run the script and pass the directory you want to organize:

```bash
python organizer.py "C:\Users\YourName\Downloads"
```

Or simply run it in the current directory:
```bash
python organizer.py
```

## Project Structure
- `organizer.py`: The magic script.
- `config.json`: The rules for sorting.
- `/.kiro`: Challenge metadata.

## Why I Built This
I hate seeing my Downloads folder as a mess of PDFs, installers, and random images. I wanted a one-click solution to tidy it up instantly.

## Author
Made by **Sujal Chavan**.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
Copyright (c) 2025 Sujal Chavan.

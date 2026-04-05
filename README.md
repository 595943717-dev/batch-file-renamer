# Batch File Renamer

A simple Python CLI tool for batch renaming files in a folder.

## Features

- Add prefix to filenames
- Add suffix to filenames
- Replace text in filenames
- Auto-number renamed files
- Preview changes with dry-run mode

## Requirements

- Python 3.8+

## Usage

```bash
python renamer.py ./test_files --prefix img_
python renamer.py ./test_files --suffix _backup
python renamer.py ./test_files --replace old new
python renamer.py ./test_files --prefix img_ --dry-run

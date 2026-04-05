import os
import argparse


def rename_files(folder, prefix="", suffix="", replace_text=None):
    if not os.path.isdir(folder):
        print(f"Folder not found: {folder}")
        return

    files = os.listdir(folder)
    files = [f for f in files if os.path.isfile(os.path.join(folder, f))]

    if not files:
        print("No files found.")
        return

    for index, filename in enumerate(files, start=1):
        old_path = os.path.join(folder, filename)
        name, ext = os.path.splitext(filename)

        new_name = name

        if replace_text and len(replace_text) == 2:
            old, new = replace_text
            new_name = new_name.replace(old, new)

        if prefix:
            new_name = f"{prefix}{new_name}"

        if suffix:
            new_name = f"{new_name}{suffix}"

        new_filename = f"{index:03d}_{new_name}{ext}"
        new_path = os.path.join(folder, new_filename)

        os.rename(old_path, new_path)
        print(f"Renamed: {filename} -> {new_filename}")


def main():
    parser = argparse.ArgumentParser(description="Batch rename files in a folder.")
    parser.add_argument("folder", help="Target folder path")
    parser.add_argument("--prefix", default="", help="Prefix to add")
    parser.add_argument("--suffix", default="", help="Suffix to add")
    parser.add_argument(
        "--replace",
        nargs=2,
        metavar=("OLD", "NEW"),
        help="Replace text in filename"
    )

    args = parser.parse_args()
    rename_files(args.folder, args.prefix, args.suffix, args.replace)


if __name__ == "__main__":
    main()

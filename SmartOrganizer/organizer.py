import os
import shutil
import json
import argparse
from datetime import datetime

class SmartOrganizer:
    def __init__(self, target_dir, config_path="config.json"):
        self.target_dir = target_dir
        self.config = self.load_config(config_path)
        self.log = []

    def load_config(self, path):
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Config file {path} not found. Using defaults.")
            return {}

    def get_category(self, file_extension):
        for category, extensions in self.config.items():
            if file_extension.lower() in extensions:
                return category
        return "Others"

    def organize(self):
        if not os.path.exists(self.target_dir):
            print(f"Directory {self.target_dir} does not exist.")
            return

        print(f"Organizing {self.target_dir}...")
        
        files_moved = 0
        for filename in os.listdir(self.target_dir):
            file_path = os.path.join(self.target_dir, filename)
            
            if os.path.isfile(file_path) and filename != "organizer.py" and filename != "config.json":
                _, extension = os.path.splitext(filename)
                category = self.get_category(extension)
                
                category_dir = os.path.join(self.target_dir, category)
                if not os.path.exists(category_dir):
                    os.makedirs(category_dir)
                
                dest_path = os.path.join(category_dir, filename)
                
                # Handle duplicate files
                if os.path.exists(dest_path):
                    base, ext = os.path.splitext(filename)
                    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                    new_filename = f"{base}_{timestamp}{ext}"
                    dest_path = os.path.join(category_dir, new_filename)
                
                try:
                    shutil.move(file_path, dest_path)
                    self.log.append(f"Moved: {filename} -> {category}/")
                    files_moved += 1
                except Exception as e:
                    self.log.append(f"Error moving {filename}: {str(e)}")

        self.generate_report(files_moved)

    def generate_report(self, count):
        print(f"\n--- Organization Report ---")
        print(f"Total files moved: {count}")
        if self.log:
            print("\nDetails:")
            for entry in self.log[:10]: # Show first 10
                print(entry)
            if len(self.log) > 10:
                print(f"...and {len(self.log) - 10} more.")
        else:
            print("No files needed organizing.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Smart File Organizer")
    parser.add_argument("directory", nargs="?", default=".", help="Directory to organize (default: current)")
    args = parser.parse_args()

    # If running from the same dir, look for config in current dir
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, "config.json")

    organizer = SmartOrganizer(args.directory, config_path)
    organizer.organize()

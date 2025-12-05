import os
import shutil
import argparse

class SmartUndo:
    def __init__(self, target_dir):
        self.target_dir = target_dir
        self.log = []

    def undo(self):
        if not os.path.exists(self.target_dir):
            print(f"Directory {self.target_dir} does not exist.")
            return

        print(f"Restoring files in {self.target_dir}...")
        
        files_moved = 0
        # Iterate over all items in the target directory
        for item in os.listdir(self.target_dir):
            item_path = os.path.join(self.target_dir, item)
            
            # If it's a directory, check if it has files to move back
            if os.path.isdir(item_path) and item not in [".kiro", ".git", "__pycache__"]:
                for filename in os.listdir(item_path):
                    file_path = os.path.join(item_path, filename)
                    
                    if os.path.isfile(file_path):
                        dest_path = os.path.join(self.target_dir, filename)
                        
                        # Handle duplicate files (if file already exists in root)
                        if os.path.exists(dest_path):
                            base, ext = os.path.splitext(filename)
                            new_filename = f"{base}_restored{ext}"
                            dest_path = os.path.join(self.target_dir, new_filename)
                        
                        try:
                            shutil.move(file_path, dest_path)
                            self.log.append(f"Restored: {item}/{filename} -> ./")
                            files_moved += 1
                        except Exception as e:
                            self.log.append(f"Error restoring {filename}: {str(e)}")
                
                # Try to remove the directory if it's empty
                try:
                    os.rmdir(item_path)
                    print(f"Removed empty directory: {item}")
                except OSError:
                    pass # Directory not empty

        self.generate_report(files_moved)

    def generate_report(self, count):
        print(f"\n--- Undo Report ---")
        print(f"Total files restored: {count}")
        if self.log:
            print("\nDetails:")
            for entry in self.log[:10]:
                print(entry)
            if len(self.log) > 10:
                print(f"...and {len(self.log) - 10} more.")
        else:
            print("No files found to restore.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Smart File Undo")
    parser.add_argument("directory", nargs="?", default=".", help="Directory to undo (default: current)")
    args = parser.parse_args()

    undoer = SmartUndo(args.directory)
    undoer.undo()

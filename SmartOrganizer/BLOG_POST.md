# Lazy Automation: How I Built a Smart File Organizer with Python

## The Problem: Digital Clutter
We've all been there. You open your Downloads folder, and it's a graveyard of `setup.exe`, `invoice.pdf`, `IMG_2024.jpg`, and `archive.zip`. Finding anything takes forever, and manually sorting it is the definition of "boring."

As part of the **Lazy Automation** week, I decided to solve this problem once and for all.

## The Solution: Smart File Organizer
I built a Python script that acts as a digital housekeeper. It scans a target directory, identifies file types, and moves them into appropriate folders (Images, Documents, etc.).

### How It Works
The core logic is simple but effective. It uses a `config.json` file to map file extensions to categories.

```json
{
    "Images": [".jpg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"]
}
```

The Python script then iterates through the files:

```python
def organize(self):
    for filename in os.listdir(self.target_dir):
        # ... check extension ...
        category = self.get_category(extension)
        # ... move file ...
```

### Key Features
1.  **Configurable**: I can easily add new file types.
2.  **Conflict Handling**: If a file already exists, it renames the new one with a timestamp instead of overwriting it.
3.  **Instant**: It cleans up hundreds of files in seconds.

## How Kiro Accelerated Development
Using Kiro (my AI pair programmer) made this process incredibly fast.
1.  **Planning**: Kiro helped me outline the project structure and requirements.
2.  **Boilerplate**: It generated the initial `config.json` with common extensions so I didn't have to type them all out.
3.  **Error Handling**: Kiro suggested adding the duplicate file handling logic, which saved me from potential data loss.

## Conclusion
Now, whenever my Desktop gets messy, I just run `python organizer.py`, and everything is tidy again. Automation for the win!

[Link to GitHub Repository]

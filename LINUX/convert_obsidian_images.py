import os
import re

# Change this to your vault path
vault_path = "D:\OSCP NOTES\OSCP\OSCP-FUNDAMENTALS\LINUX"

# Loop through all .md files in the vault
for root, dirs, files in os.walk(vault_path):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(root, file)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Replace Obsidian ![[...]] links with GitHub Markdown
            def replace_link(match):
                path = match.group(1)
                filename = os.path.basename(path)
                filename_encoded = filename.replace(" ", "%20")
                # Return standard Markdown format
                return f"![{filename}]({path.replace(filename, filename_encoded)})"

            new_content = re.sub(r'!\[\[([^\]]+)\]\]', replace_link, content)

            # Overwrite file with converted content
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)

print("✅ All Obsidian image links have been converted to GitHub Markdown format!")

import os
import re
import shutil

# Paths
posts_dir = r"C:\Users\Petra\Desktop\Code Institute\undercoverunicorn\content\posts"
attachments_dir = r"C:\Users\Petra\Documents\Zettelkasten\My Zettelkasten\6 - Attachments"
static_images_dir = r"C:\Users\Petra\Desktop\Code Institute\undercoverunicorn\static\images"

# Process each markdown file in the posts directory
for filename in os.listdir(posts_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(posts_dir, filename)

        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()

        # Find Obsidian-style image links
        images = re.findall(r'!\[\]\(([^)]+\.png)\)', content)
        print(f"Images found in {filename}: {images}")  # Debugging

        # Process each image
        for image in images:
            image_source = os.path.join(attachments_dir, image)
            image_dest = os.path.join(static_images_dir, os.path.basename(image_source))

            # Replace the image link in Markdown
            markdown_image = f'<img src="/undercoverunicorn/images/{image.replace(' ', '%20')}" alt="{image}">'
            content = content.replace(f"![]({image})", markdown_image)

            # Copy image if it exists
            if os.path.exists(image_source):
                print(f"Copying: {image_source} -> {image_dest}")
                shutil.copy(image_source, image_dest)
            else:
                print(f"Image not found (double-check name and path): {image_source}")

        # Write updated content back
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)

print("Markdown files processed and images copied successfully.")

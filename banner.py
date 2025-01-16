from PIL import Image, ImageDraw, ImageFont
import os

# Create a new image with a dark background
width = 1280
height = 640
background_color = (15, 23, 42)  # Dark blue background
image = Image.new('RGB', (width, height), background_color)
draw = ImageDraw.Draw(image)

# Add a network/security pattern in the background
for i in range(0, width, 30):
    for j in range(0, height, 30):
        draw.rectangle([i, j, i+2, j+2], fill=(30, 41, 59))

# Add title text
title = "Fortigate CVE-2022-40684"
subtitle = "Vulnerability Tracker"

# You'll need to adjust font paths based on your system
try:
    title_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 72)
    subtitle_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 48)
except:
    title_font = ImageFont.load_default()
    subtitle_font = ImageFont.load_default()

# Center the text
title_bbox = draw.textbbox((0, 0), title, font=title_font)
subtitle_bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)

title_x = (width - (title_bbox[2] - title_bbox[0])) // 2
title_y = (height - (title_bbox[3] - title_bbox[1])) // 2 - 40

subtitle_x = (width - (subtitle_bbox[2] - subtitle_bbox[0])) // 2
subtitle_y = title_y + 100

# Add text with a subtle glow effect
draw.text((title_x+2, title_y+2), title, font=title_font, fill=(255, 99, 71, 128))  # Shadow
draw.text((title_x, title_y), title, font=title_font, fill=(255, 99, 71))  # Main text in red

draw.text((subtitle_x+2, subtitle_y+2), subtitle, font=subtitle_font, fill=(200, 200, 200, 128))  # Shadow
draw.text((subtitle_x, subtitle_y), subtitle, font=subtitle_font, fill=(200, 200, 200))  # White text

# Save the image
image.save('banner.png')

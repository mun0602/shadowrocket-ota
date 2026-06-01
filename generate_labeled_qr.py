import urllib.request
import urllib.parse
import os
from PIL import Image, ImageDraw, ImageFont

# Define link and api url
link = "itms-services://?action=download-manifest&url=https://raw.githubusercontent.com/mun0602/shadowrocket-ota/main/manifest.plist"
encoded_link = urllib.parse.quote_plus(link)
api_url = f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={encoded_link}"

dir_path = os.path.dirname(__file__)
temp_qr_path = os.path.join(dir_path, "temp_qr.png")
output_path = os.path.join(dir_path, "qrcode_labeled.png")

try:
    # 1. Download the raw QR code
    print("Downloading QR code...")
    urllib.request.urlretrieve(api_url, temp_qr_path)
    
    # 2. Open QR code image (300x300)
    qr_img = Image.open(temp_qr_path)
    
    # 3. Create a larger white canvas (300x360)
    canvas = Image.new("RGB", (300, 360), "white")
    canvas.paste(qr_img, (0, 0))
    
    # 4. Draw text "Shadowrocket 3utool" centered
    draw = ImageDraw.Draw(canvas)
    text = "Shadowrocket 3utool"
    
    # Try to load a clean Windows font, fallback if not found
    try:
        font = ImageFont.truetype("arial.ttf", 18)
    except IOError:
        font = ImageFont.load_default()
        
    # Get text dimensions to center it
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (300 - text_width) // 2
    y = 300 + (60 - text_height) // 2 - 5  # center vertically in the bottom 60px area
    
    # Draw text with crisp black color
    draw.text((x, y), text, fill="black", font=font)
    
    # 5. Save the labeled image
    canvas.save(output_path)
    print(f"Labeled QR code generated successfully at: {output_path}")
    
    # Clean up temp file
    if os.path.exists(temp_qr_path):
        os.remove(temp_qr_path)
        
except Exception as e:
    print(f"Error: {e}")

import urllib.request
import urllib.parse
import os

link = "itms-services://?action=download-manifest&url=https://raw.githubusercontent.com/mun0602/shadowrocket-ota/main/manifest.plist"
encoded_link = urllib.parse.quote_plus(link)
api_url = f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={encoded_link}"

output_path = os.path.join(os.path.dirname(__file__), "qrcode.png")

try:
    print(f"Downloading QR code from: {api_url}")
    urllib.request.urlretrieve(api_url, output_path)
    print(f"Successfully generated QR code and saved to {output_path}")
except Exception as e:
    print(f"Error generating QR code: {e}")

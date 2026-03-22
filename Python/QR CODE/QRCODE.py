# animated_qrcode_local.py
import segno

# Create a QR code that links to the YouTube video
slts_qrcode = segno.make_qr("https://www.youtube.com/watch?v=hTWKbfoikeg")

# Use the downloaded GIF as the background
slts_qrcode.to_artistic(
    background="nirvana.gif",  # <-- This line is changed to use the local file
    target="animated_qrcode.gif",
    scale=5,
)

print("Animated QR code has been created successfully as animated_qrcode.gif!")
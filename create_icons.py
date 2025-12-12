import os
from PIL import Image, ImageDraw, ImageFont

# Tạo icon với text "P.bò"
def create_icon(size, output_path, bg_color, text_color):
    """
    Tạo icon với text P.bò
    size: kích thước icon (width, height)
    output_path: đường dẫn lưu file
    bg_color: màu nền (R, G, B)
    text_color: màu chữ (R, G, B)
    """
    # Tạo image với nền màu
    img = Image.new('RGB', size, color=bg_color)
    draw = ImageDraw.Draw(img)
    
    # Vẽ hình tròn bo góc (rounded rectangle)
    # Tạo mask cho bo góc
    mask = Image.new('L', size, 0)
    mask_draw = ImageDraw.Draw(mask)
    
    # Vẽ hình chữ nhật bo góc
    corner_radius = size[0] // 6
    mask_draw.rounded_rectangle([(0, 0), size], corner_radius, fill=255)
    
    # Apply mask
    img.putalpha(mask)
    
    # Vẽ text "P.bò"
    text = "P.bò"
    
    # Tính font size phù hợp
    font_size = int(size[0] * 0.25)
    
    try:
        # Thử dùng font Arial hoặc font hệ thống
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        try:
            font = ImageFont.truetype("Arial.ttf", font_size)
        except:
            # Fallback sang font mặc định
            font = ImageFont.load_default()
    
    # Lấy kích thước text
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    # Vẽ text ở giữa
    position = ((size[0] - text_width) // 2, (size[1] - text_height) // 2 - font_size // 10)
    
    # Vẽ shadow (bóng chữ)
    shadow_offset = size[0] // 50
    draw.text((position[0] + shadow_offset, position[1] + shadow_offset), 
              text, font=font, fill=(0, 0, 0, 100))
    
    # Vẽ text chính
    draw.text(position, text, font=font, fill=text_color)
    
    # Lưu file
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, 'PNG')
    print(f"Created: {output_path}")

# Định nghĩa màu cho từng flavor
flavors = {
    'blue': ((24, 119, 242), (255, 255, 255)),    # Facebook blue + white text
    'green': ((49, 162, 76), (255, 255, 255)),    # Grab green + white text
    'red': ((245, 83, 61), (255, 255, 255)),      # Red + white text
    'purple': ((142, 68, 173), (255, 255, 255)),  # Purple + white text
    'orange': ((243, 156, 18), (255, 255, 255)),  # Orange + white text
}

# Định nghĩa sizes cho Android
sizes = {
    'mdpi': 48,
    'hdpi': 72,
    'xhdpi': 96,
    'xxhdpi': 144,
    'xxxhdpi': 192,
}

# Base path
base_path = os.path.dirname(os.path.abspath(__file__))
res_path = os.path.join(base_path, 'android', 'app', 'src')

# Tạo icon cho từng flavor
for flavor_name, (bg_color, text_color) in flavors.items():
    flavor_path = os.path.join(res_path, flavor_name, 'res')
    
    for density, size in sizes.items():
        mipmap_path = os.path.join(flavor_path, f'mipmap-{density}')
        
        # Tạo ic_launcher.png
        icon_path = os.path.join(mipmap_path, 'ic_launcher.png')
        create_icon((size, size), icon_path, bg_color, text_color)
        
        # Tạo ic_launcher_round.png (giống nhau cho đơn giản)
        round_path = os.path.join(mipmap_path, 'ic_launcher_round.png')
        create_icon((size, size), round_path, bg_color, text_color)

print("\n✅ Tất cả icon đã được tạo!")
print("\nCác icon có màu:")
print("- Blue (Xanh dương Facebook)")
print("- Green (Xanh lá Grab)")
print("- Red (Đỏ)")
print("- Purple (Tím)")
print("- Orange (Cam)")
print("\nMỗi flavor có icon riêng để dễ phân biệt!")

# Hướng dẫn tạo Icon cho P.bò

## Cách 1: Chạy script Python (Tự động - Khuyến nghị)

### Bước 1: Cài đặt Python và Pillow
```bash
# Cài Python từ: https://www.python.org/downloads/
# Sau đó cài Pillow:
pip install Pillow
```

### Bước 2: Chạy script
```bash
cd C:\Users\Conchuot\SocialLiteApp
python create_icons.py
```

Script sẽ tự động tạo icon "P.bò" với màu khác nhau cho mỗi flavor!

## Cách 2: Sử dụng hình ảnh bạn đã gửi

### Online Tool (Dễ nhất):

1. **Truy cập:** https://icon.kitchen/

2. **Upload ảnh** người trên xe Yamaha

3. **Chọn:**
   - Platform: Android
   - Shape: Circle hoặc Square
   - Background: Tùy chọn

4. **Download** file ZIP

5. **Giải nén** và copy vào:
   ```
   android/app/src/main/res/
   ```

### Cho từng phiên bản khác nhau:

Nếu muốn mỗi flavor có icon khác màu:

```
android/app/src/
├── blue/res/
│   ├── mipmap-mdpi/ic_launcher.png
│   ├── mipmap-hdpi/ic_launcher.png
│   ├── mipmap-xhdpi/ic_launcher.png
│   ├── mipmap-xxhdpi/ic_launcher.png
│   └── mipmap-xxxhdpi/ic_launcher.png
├── green/res/
│   └── ... (icon màu xanh lá)
├── red/res/
│   └── ... (icon màu đỏ)
├── purple/res/
│   └── ... (icon màu tím)
└── orange/res/
    └── ... (icon màu cam)
```

## Cách 3: Icon mặc định đơn giản

Script Python đã tạo sẵn icon text "P.bò" với:
- Nền màu theo từng flavor
- Chữ trắng, font to
- Bo góc mềm mại
- Có bóng đổ (shadow)

## Sau khi có icon:

### 1. Build lại app:
```bash
cd android
gradlew clean
gradlew assembleRelease
```

### 2. Icon sẽ khác nhau:
- **P.bò Blue**: Nền xanh Facebook
- **P.bò Green**: Nền xanh Grab
- **P.bò Red**: Nền đỏ
- **P.bò Purple**: Nền tím
- **P.bò Orange**: Nền cam

## Tùy chỉnh màu trong script:

Mở file `create_icons.py` và sửa dòng:

```python
flavors = {
    'blue': ((24, 119, 242), (255, 255, 255)),    # (R,G,B nền), (R,G,B chữ)
    'green': ((49, 162, 76), (255, 255, 255)),
    # ... thêm màu mới
}
```

Màu RGB:
- Đỏ: (255, 0, 0)
- Xanh lá: (0, 255, 0)
- Xanh dương: (0, 0, 255)
- Vàng: (255, 255, 0)
- Tím: (128, 0, 128)
- Cam: (255, 165, 0)

## Nếu không muốn chạy Python:

Tôi khuyên dùng online tool:
1. https://icon.kitchen/ (Tốt nhất)
2. https://appicon.co/
3. https://romannurik.github.io/AndroidAssetStudio/

Upload hình và download ngay!

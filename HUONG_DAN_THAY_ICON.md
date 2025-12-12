# Hướng dẫn thay Icon cho ứng dụng P.bò

## Cách 1: Sử dụng Online Tool (Dễ nhất)

### Bước 1: Chuẩn bị ảnh icon
- Sử dụng hình ảnh bạn đã gửi (người trên xe Yamaha)
- Hoặc bất kỳ ảnh nào bạn muốn làm icon
- Kích thước khuyến nghị: 1024x1024 pixels

### Bước 2: Tạo icon sizes
Truy cập: https://icon.kitchen/ hoặc https://appicon.co/

1. Upload hình ảnh của bạn
2. Chọn "Android" platform
3. Download file ZIP chứa tất cả kích thước icon

### Bước 3: Thay thế icon
Giải nén file ZIP, bạn sẽ có các thư mục:
```
mipmap-mdpi/
mipmap-hdpi/
mipmap-xhdpi/
mipmap-xxhdpi/
mipmap-xxxhdpi/
```

Copy các thư mục này vào:
```
SocialLiteApp/android/app/src/main/res/
```

Các file icon cần có:
- `ic_launcher.png` - Icon thông thường
- `ic_launcher_round.png` - Icon tròn (Android 7.1+)

## Cách 2: Thủ công (Chi tiết)

### Bước 1: Chuẩn bị các kích thước icon

Bạn cần tạo icon với các kích thước sau:

| Thư mục | Kích thước | DPI |
|---------|-----------|-----|
| mipmap-mdpi | 48x48 | 160 |
| mipmap-hdpi | 72x72 | 240 |
| mipmap-xhdpi | 96x96 | 320 |
| mipmap-xxhdpi | 144x144 | 480 |
| mipmap-xxxhdpi | 192x192 | 640 |

### Bước 2: Đặt file vào đúng thư mục

```
android/app/src/main/res/
├── mipmap-mdpi/
│   ├── ic_launcher.png (48x48)
│   └── ic_launcher_round.png (48x48)
├── mipmap-hdpi/
│   ├── ic_launcher.png (72x72)
│   └── ic_launcher_round.png (72x72)
├── mipmap-xhdpi/
│   ├── ic_launcher.png (96x96)
│   └── ic_launcher_round.png (96x96)
├── mipmap-xxhdpi/
│   ├── ic_launcher.png (144x144)
│   └── ic_launcher_round.png (144x144)
└── mipmap-xxxhdpi/
    ├── ic_launcher.png (192x192)
    └── ic_launcher_round.png (192x192)
```

## Cách 3: Icon khác nhau cho mỗi phiên bản

Nếu bạn muốn mỗi phiên bản (Blue, Green, Red, Purple, Orange) có icon khác nhau:

### Tạo thư mục riêng cho mỗi flavor:

```
android/app/src/
├── blue/res/mipmap-xxxhdpi/
│   └── ic_launcher.png (icon xanh dương)
├── green/res/mipmap-xxxhdpi/
│   └── ic_launcher.png (icon xanh lá)
├── red/res/mipmap-xxxhdpi/
│   └── ic_launcher.png (icon đỏ)
├── purple/res/mipmap-xxxhdpi/
│   └── ic_launcher.png (icon tím)
└── orange/res/mipmap-xxxhdpi/
    └── ic_launcher.png (icon cam)
```

## Tool hỗ trợ tạo icon

### Online Tools (Miễn phí):
1. **Icon Kitchen**: https://icon.kitchen/
2. **AppIcon**: https://appicon.co/
3. **Android Asset Studio**: https://romannurik.github.io/AndroidAssetStudio/icons-launcher.html

### Phần mềm:
1. **GIMP** (Free) - https://www.gimp.org/
2. **Photoshop** (Paid)
3. **Figma** (Free)

## Sử dụng hình ảnh bạn gửi làm icon

Hình ảnh bạn gửi (người trên xe Yamaha) có thể làm icon theo cách này:

### Option 1: Crop hình vuông
1. Mở ảnh bằng tool chỉnh sửa
2. Crop thành hình vuông (1:1 ratio)
3. Resize xuống 1024x1024
4. Upload lên icon.kitchen để tạo tất cả sizes

### Option 2: Tạo icon với nền
1. Tạo canvas 1024x1024 với nền màu (xanh lá, đỏ, tím, cam...)
2. Đặt hình ảnh vào giữa
3. Thêm text "P.bò" nếu muốn
4. Export và upload lên icon.kitchen

### Option 3: Icon đơn giản
Tạo icon chữ "P.bò" với:
- Font chữ đẹp
- Nền màu gradient
- Viền bo tròn

## Sau khi thay icon

### 1. Clean project
```bash
cd android
gradlew clean
```

### 2. Build lại APK
```bash
gradlew assembleRelease
```

### 3. Kiểm tra
- Cài APK lên điện thoại
- Icon mới sẽ xuất hiện trên màn hình chính

## Lưu ý

⚠️ **Quan trọng:**
- Icon nên có nền trong suốt (PNG) hoặc nền màu
- Tránh dùng ảnh có nhiều chi tiết nhỏ (khó nhìn khi thu nhỏ)
- Icon tròn (`ic_launcher_round.png`) sẽ hiển thị trên Android 7.1+
- Nên test icon trên nhiều thiết bị khác nhau

## Ví dụ icon đơn giản cho P.bò

Nếu bạn muốn icon đơn giản, tôi đề xuất:

**Design 1: Chữ P.bò trên nền màu**
```
┌─────────────┐
│             │
│    P.bò     │  <- Chữ to, font đẹp
│             │
└─────────────┘
   (Nền xanh lá giống Grab)
```

**Design 2: Xe máy stylized**
```
┌─────────────┐
│   🏍️        │  <- Icon xe máy vector
│    P.bò     │  <- Text bên dưới
└─────────────┘
```

**Design 3: Mix cả hai**
```
┌─────────────┐
│   🏍️ P.bò   │  <- Icon + Text
└─────────────┘
```

## Cần giúp đỡ?

Nếu bạn cần tôi tạo icon cụ thể, hãy cho tôi biết:
1. Màu sắc chủ đạo
2. Style (đơn giản, phức tạp, hiện đại...)
3. Có muốn dùng ảnh gốc hay làm mới?

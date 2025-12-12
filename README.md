# Hướng dẫn Build Ứng dụng P.bò

## Giới thiệu
Ứng dụng mạng xã hội nhẹ **P.bò** được tối ưu cho thiết bị Android 32-bit.

## Tính năng
- ✅ News Feed (Bảng tin)
- ✅ Đăng bài viết với ảnh
- ✅ Thích, bình luận, chia sẻ
- ✅ Tin nhắn (Chat)
- ✅ Thông báo
- ✅ Trang cá nhân
- ✅ Tối ưu cho thiết bị 32-bit

## Yêu cầu hệ thống
- Node.js >= 16
- JDK 11 hoặc cao hơn
- Android SDK
- React Native CLI

## Cài đặt

### 1. Cài đặt dependencies
```bash
cd SocialLiteApp
npm install
```

### 2. Cài đặt Android SDK
Đảm bảo bạn đã cài đặt:
- Android SDK Platform 33
- Android SDK Build-Tools 33.0.0
- Android Emulator hoặc thiết bị thật

## Build APK cho nhiều phiên bản

Ứng dụng được cấu hình để build 5 phiên bản khác nhau:

### 1. P.bò Blue (Xanh dương)
```bash
cd android
gradlew assembleBlueRelease
```
APK: `android/app/build/outputs/apk/blue/release/app-blue-release.apk`

### 2. P.bò Green (Xanh lá - giống Grab)
```bash
cd android
gradlew assembleGreenRelease
```
APK: `android/app/build/outputs/apk/green/release/app-green-release.apk`

### 3. P.bò Red (Đỏ)
```bash
cd android
gradlew assembleRedRelease
```
APK: `android/app/build/outputs/apk/red/release/app-red-release.apk`

### 4. P.bò Purple (Tím)
```bash
cd android
gradlew assemblePurpleRelease
```
APK: `android/app/build/outputs/apk/purple/release/app-purple-release.apk`

### 5. P.bò Orange (Cam)
```bash
cd android
gradlew assembleOrangeRelease
```
APK: `android/app/build/outputs/apk/orange/release/app-orange-release.apk`

## Build tất cả phiên bản cùng lúc
```bash
cd android
gradlew assembleRelease
```

## Chạy ở chế độ Development

### Android
```bash
npm run android
```

## Đặc điểm kỹ thuật

### Tối ưu cho 32-bit
- Chỉ build cho kiến trúc `armeabi-v7a` (32-bit)
- Giảm kích thước APK
- Tương thích với thiết bị Android cũ

### Kích thước nhỏ gọn
- Sử dụng Hermes Engine
- Tối ưu code
- Không thư viện thừa

### Nhiều phiên bản
Mỗi phiên bản có:
- Package name riêng: `com.pbo.blue`, `com.pbo.green`, etc.
- Tên ứng dụng riêng: "P.bò Blue", "P.bò Green", etc.
- Màu chủ đạo riêng
- Có thể cài cùng lúc trên một thiết bị

## Tùy chỉnh thêm phiên bản

Mở file `android/app/build.gradle` và thêm flavor mới:

```gradle
productFlavors {
    // ... các flavor hiện tại
    
    yellow {
        dimension "version"
        applicationId "com.pbo.yellow"
        resValue "string", "app_name", "P.bò Yellow"
        buildConfigField "String", "THEME_COLOR", '"#f1c40f"'
    }
}
```

## Cấu trúc dự án

```
SocialLiteApp/
├── src/
│   ├── App.js              # Main app component
│   └── screens/
│       ├── HomeScreen.js        # Trang chủ / News Feed
│       ├── PostDetailScreen.js  # Chi tiết bài viết
│       ├── CreatePostScreen.js  # Tạo bài viết
│       ├── ProfileScreen.js     # Trang cá nhân
│       ├── ChatScreen.js        # Tin nhắn
│       ├── NotificationScreen.js # Thông báo
│       └── LoginScreen.js       # Đăng nhập
├── android/                # Android native code
├── package.json
└── README.md
```

## Ghi chú quan trọng

⚠️ **Về APK Release:**
- APK hiện tại dùng debug keystore
- Để publish lên Play Store, cần tạo release keystore riêng
- Thay đổi signing config trong `android/app/build.gradle`

⚠️ **Về Backend:**
- Hiện tại dùng dữ liệu mẫu (mock data)
- Cần kết nối với API backend thật để hoạt động đầy đủ
- Có thể dùng Firebase, Node.js + Express, hoặc bất kỳ backend nào

## Tích hợp Backend

Để kết nối với backend, sửa các file screen và thêm API calls:

```javascript
// Ví dụ trong HomeScreen.js
import axios from 'axios';

const loadPosts = async () => {
  try {
    const response = await axios.get('https://your-api.com/posts');
    setPosts(response.data);
  } catch (error) {
    console.error(error);
  }
};
```

## Hỗ trợ

Nếu gặp lỗi khi build:
1. Xóa thư mục `node_modules` và chạy lại `npm install`
2. Xóa thư mục `android/build` và `android/app/build`
3. Chạy `cd android && gradlew clean`
4. Build lại

## Package Names

Các package name cho từng phiên bản:
- **P.bò Blue**: `com.pbo.blue`
- **P.bò Green**: `com.pbo.green`
- **P.bò Red**: `com.pbo.red`
- **P.bò Purple**: `com.pbo.purple`
- **P.bò Orange**: `com.pbo.orange`

Tất cả đều có thể cài đồng thời trên một thiết bị!

## Thay đổi Icon

Xem hướng dẫn chi tiết trong file: **HUONG_DAN_THAY_ICON.md**

Tóm tắt:
1. Tạo icon 1024x1024 từ hình ảnh bạn muốn
2. Truy cập https://icon.kitchen/
3. Upload ảnh và download icon pack
4. Copy vào `android/app/src/main/res/`

## License
MIT

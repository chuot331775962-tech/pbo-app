# 🔧 HƯỚNG DẪN CÀI ĐẶT ĐỂ BUILD APK

## ⚠️ YÊU CẦU:

Để build APK cho P.bò, bạn cần cài đặt:

### 1. **Node.js** ✅ (Đã có)
- Bạn đã có Node.js và npm

### 2. **JDK (Java Development Kit)** ❓
- Cần JDK 11 hoặc 17
- Download: https://adoptium.net/

### 3. **Android Studio** ❓ (QUAN TRỌNG)
- Bao gồm Android SDK, Gradle, Build Tools
- Download: https://developer.android.com/studio

---

## 📥 CÁCH CÀI ĐẶT:

### OPTION 1: Android Studio (Khuyến nghị)

#### Bước 1: Download Android Studio
- Truy cập: https://developer.android.com/studio
- Download bản Windows
- Cài đặt (chọn Standard Install)

#### Bước 2: Cài SDK và Build Tools
Mở Android Studio → Settings (Ctrl+Alt+S) → Appearance & Behavior → System Settings → Android SDK

Chọn tab **SDK Platforms**, tích:
- ☑️ Android 13 (Tiramisu) - API Level 33
- ☑️ Android 12 (S) - API Level 31
- ☑️ Android 11 (R) - API Level 30

Chọn tab **SDK Tools**, tích:
- ☑️ Android SDK Build-Tools 33.0.0
- ☑️ Android SDK Platform-Tools
- ☑️ Android SDK Tools
- ☑️ NDK (Side by side) - Version 23.1.7779620
- ☑️ CMake

Click **Apply** → **OK**

#### Bước 3: Thiết lập biến môi trường
Thêm vào Environment Variables:

**ANDROID_HOME:**
```
C:\Users\Conchuot\AppData\Local\Android\Sdk
```

**Path (thêm vào):**
```
%ANDROID_HOME%\platform-tools
%ANDROID_HOME%\tools
%ANDROID_HOME%\tools\bin
```

#### Bước 4: Verify
```powershell
adb version
```

---

### OPTION 2: Chỉ cài Gradle (Nhanh hơn)

#### Bước 1: Download Gradle
- Truy cập: https://gradle.org/releases/
- Download **Gradle 8.0.1** (Binary-only)
- Giải nén vào: `C:\Gradle\gradle-8.0.1`

#### Bước 2: Thêm vào Path
Thêm vào Environment Variables → Path:
```
C:\Gradle\gradle-8.0.1\bin
```

#### Bước 3: Verify
```powershell
gradle -v
```

#### Bước 4: Tạo Gradle Wrapper
```powershell
cd C:\Users\Conchuot\SocialLiteApp\android
gradle wrapper --gradle-version=8.0.1
```

---

## 🚀 SAU KHI CÀI XONG:

### 1. Tạo Gradle Wrapper (nếu chưa có)
```powershell
cd C:\Users\Conchuot\SocialLiteApp\android
gradle wrapper
```

### 2. Build APK
```powershell
# Build P.bò Blue
.\gradlew assembleBlueRelease

# Build P.bò Green
.\gradlew assembleGreenRelease

# Build tất cả
.\gradlew assembleRelease
```

### 3. Lấy APK
File APK sẽ ở:
```
android\app\build\outputs\apk\blue\release\app-blue-release.apk
android\app\build\outputs\apk\green\release\app-green-release.apk
...
```

---

## 🎯 CÁCH NHANH NHẤT:

### Nếu có Android Studio rồi:

1. Mở Android Studio
2. File → Open → Chọn thư mục `SocialLiteApp\android`
3. Chờ Gradle sync xong
4. Build → Generate Signed Bundle / APK
5. Chọn APK → Chọn flavor (blue/green/red/purple/orange)
6. Build

---

## ❓ KIỂM TRA ĐÃ CÀI CHƯA:

```powershell
# Kiểm tra Java
java -version

# Kiểm tra Android SDK
echo %ANDROID_HOME%
adb version

# Kiểm tra Gradle
gradle -v
```

---

## 🔍 NẾU GẶP LỖI:

### "ANDROID_HOME not set"
→ Thiết lập biến môi trường ANDROID_HOME

### "SDK location not found"
→ Tạo file `android/local.properties`:
```properties
sdk.dir=C:\\Users\\Conchuot\\AppData\\Local\\Android\\Sdk
```

### "gradlew not found"
→ Chạy: `gradle wrapper` trong thư mục android

### "JDK not found"
→ Cài JDK 11 hoặc 17

---

## 💡 GIẢI PHÁP THAY THẾ:

### Nếu không muốn cài nhiều thứ:

#### 1. Dùng Expo (Đơn giản hơn)
- Không cần Android Studio
- Build online qua Expo servers
- Nhưng cần chuyển sang Expo

#### 2. Dùng dịch vụ build online
- EAS Build (Expo)
- Bitrise
- AppCenter

#### 3. Thuê người build
- Fiverr, Upwork
- Các dev React Native

---

## 📋 CHECKLIST:

Trước khi build, đảm bảo có:
- ☑️ Node.js & npm
- ☑️ JDK 11+
- ☑️ Android Studio / Android SDK
- ☑️ Gradle
- ☑️ Biến môi trường ANDROID_HOME
- ☑️ Đã chạy `npm install` trong project

---

## 🎬 BƯỚC TIẾP THEO:

1. **Cài Android Studio** (Cách dễ nhất)
   - Link: https://developer.android.com/studio
   - Chọn Standard Install
   - Chờ download SDK

2. **Thiết lập biến môi trường**
   - ANDROID_HOME
   - Path

3. **Quay lại build**
   ```powershell
   cd C:\Users\Conchuot\SocialLiteApp\android
   gradle wrapper
   .\gradlew assembleRelease
   ```

---

**Link download:**
- Android Studio: https://developer.android.com/studio
- JDK: https://adoptium.net/
- Gradle: https://gradle.org/releases/

Bạn muốn tôi hướng dẫn chi tiết phần nào? 🤔

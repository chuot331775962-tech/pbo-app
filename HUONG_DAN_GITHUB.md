# 📱 CÁCH ĐƠN GIẢN NHẤT - BUILD APK QUA GITHUB

## 🎯 Không cần cài Android Studio!

GitHub sẽ build APK cho bạn **MIỄN PHÍ** và **TỰ ĐỘNG**.

---

## 📋 CÁC BƯỚC:

### 1️⃣ Tạo tài khoản GitHub (2 phút)
- Vào: https://github.com
- Click "Sign up"
- Điền email, password
- Verify email

### 2️⃣ Tạo repository mới (1 phút)
- Click nút "+" góc trên → "New repository"
- Tên repo: `pbo-app`
- Chọn "Public"
- Click "Create repository"

### 3️⃣ Upload code (5 phút)

**Cách A: Qua GitHub Web (Dễ nhất)**
1. Vào repo vừa tạo
2. Click "uploading an existing file"
3. Drag & drop toàn bộ thư mục `SocialLiteApp`
4. Kéo thả hoặc chọn tất cả files
5. Click "Commit changes"

**Cách B: Qua Git Command (Nếu biết dùng)**
```powershell
cd C:\Users\Conchuot\SocialLiteApp
git init
git add .
git commit -m "Add P.bo app"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/pbo-app.git
git push -u origin main
```

### 4️⃣ Chạy build (1 click)
1. Vào repo trên GitHub
2. Click tab "Actions"
3. Click "Build Android APK" (bên trái)
4. Click nút "Run workflow" (bên phải)
5. Click "Run workflow" màu xanh

### 5️⃣ Đợi build xong (10-15 phút)
- GitHub sẽ tự động:
  - Cài Android SDK
  - Cài Gradle
  - Build 5 APK files
- Xem tiến trình trên màn hình

### 6️⃣ Download APK
1. Build xong sẽ có dấu ✅ xanh
2. Click vào build
3. Kéo xuống "Artifacts"
4. Download:
   - `app-blue-release.apk`
   - `app-green-release.apk`
   - `app-red-release.apk`
   - `app-purple-release.apk`
   - `app-orange-release.apk`

---

## ✅ XONG!

Bạn có 5 file APK không cần cài gì cả!

---

## 🔄 LẦN SAU:

Khi sửa code, chỉ cần:
1. Upload file mới lên GitHub
2. GitHub tự động build lại
3. Download APK mới

---

## 📸 HƯỚNG DẪN CÓ HÌNH:

### Bước 1: GitHub Sign up
```
github.com → Sign up → Điền thông tin → Verify email
```

### Bước 2: Create Repository
```
Click "+" → New repository → Đặt tên "pbo-app" → Public → Create
```

### Bước 3: Upload Files
```
Click "uploading an existing file" → Kéo thả files → Commit
```

### Bước 4: Actions
```
Tab "Actions" → "Build Android APK" → "Run workflow" → Đợi
```

### Bước 5: Download
```
Build xong → Click vào → Kéo xuống "Artifacts" → Download APK
```

---

## ⚠️ LƯU Ý:

- **Miễn phí**: GitHub cho build free 2000 phút/tháng
- **Thời gian**: Mỗi lần build mất ~10-15 phút
- **Giới hạn**: Có thể build nhiều lần
- **Public repo**: Code sẽ public (mọi người thấy được)
- **Private repo**: Nếu muốn giấu code thì upgrade ($4/tháng)

---

## 💡 MẸO:

- Nếu không muốn public code, tạo private repo
- Build sẽ tự động mỗi khi push code mới
- Có thể share link APK cho người khác
- Không giới hạn số lần download

---

## 🆘 NẾU GẶP LỖI:

### "Build failed"
- Kiểm tra log màu đỏ
- Thường do thiếu file
- Đảm bảo đã upload đầy đủ thư mục

### "Workflow not found"
- File `.github/workflows/build-apk.yml` phải đúng vị trí
- Upload lại đúng cấu trúc thư mục

### "No artifacts"
- Build có thể đang chạy
- Đợi đến khi có dấu ✅ xanh

---

## 🎉 KẾT QUẢ:

Sau 20 phút (kể từ tạo tài khoản đến có APK):
- ✅ 5 file APK P.bò
- ✅ Cài được lên điện thoại
- ✅ Không cần cài Android Studio
- ✅ Hoàn toàn miễn phí

---

**Bạn chỉ cần làm theo từng bước là có APK! 🚀**

Tôi có thể hướng dẫn chi tiết từng bước nếu bạn cần!

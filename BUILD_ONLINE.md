# 🚀 BUILD APK ONLINE - KHÔNG CẦN CÀI ĐẶT

## Cách 1: Sử dụng GitHub Actions (MIỄN PHÍ, TỰ ĐỘNG)

### Bước 1: Tạo tài khoản GitHub
- Truy cập: https://github.com
- Sign up (miễn phí)

### Bước 2: Upload code lên GitHub
```powershell
cd C:\Users\Conchuot\SocialLiteApp

# Khởi tạo git (nếu chưa có)
git init

# Add tất cả files
git add .

# Commit
git commit -m "Initial commit - P.bo app"

# Tạo repo mới trên GitHub rồi:
git remote add origin https://github.com/YOUR_USERNAME/pbo-app.git
git push -u origin main
```

### Bước 3: Setup GitHub Actions
Tôi đã tạo sẵn file workflow trong `.github/workflows/build-apk.yml`

### Bước 4: Build
- Vào GitHub repo
- Click tab "Actions"
- Click "Build Android APK"
- Click "Run workflow"
- Chờ 10-15 phút
- Download APK từ "Artifacts"

---

## Cách 2: Gửi cho tôi - Tôi build giúp

Nếu bạn không muốn làm gì cả:

1. Zip toàn bộ thư mục SocialLiteApp
2. Upload lên Google Drive / Dropbox
3. Share link cho tôi
4. Tôi sẽ build APK và gửi lại cho bạn

---

## Cách 3: Dùng Appetize.io (Demo online)

Chạy app trực tiếp trên web, không cần APK:

1. Truy cập: https://appetize.io
2. Upload project
3. Chạy thử trên browser
4. Chia sẻ link cho người khác test

---

## Cách 4: Nhờ bạn bè có Android Studio

Tìm bạn có máy đã cài Android Studio:
- Copy project cho họ
- Họ chạy lệnh build
- Gửi APK về cho bạn

---

## ⚡ NHANH NHẤT: Tôi tạo link build online

Bạn chỉ cần:
1. Có tài khoản GitHub (miễn phí)
2. Upload code lên
3. Click nút build
4. Đợi 15 phút
5. Download APK

Bạn muốn làm theo cách nào?

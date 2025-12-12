@echo off
echo ============================================
echo Build P.bo - Tat ca phien ban
echo ============================================
echo.

cd android

echo [1/5] Building P.bo Blue...
call gradlew assembleBlueRelease
echo.

echo [2/5] Building P.bo Green...
call gradlew assembleGreenRelease
echo.

echo [3/5] Building P.bo Red...
call gradlew assembleRedRelease
echo.

echo [4/5] Building P.bo Purple...
call gradlew assemblePurpleRelease
echo.

echo [5/5] Building P.bo Orange...
call gradlew assembleOrangeRelease
echo.

echo ============================================
echo BUILD HOAN THANH!
echo ============================================
echo.
echo Cac file APK da duoc tao tai:
echo - android/app/build/outputs/apk/blue/release/app-blue-release.apk
echo - android/app/build/outputs/apk/green/release/app-green-release.apk
echo - android/app/build/outputs/apk/red/release/app-red-release.apk
echo - android/app/build/outputs/apk/purple/release/app-purple-release.apk
echo - android/app/build/outputs/apk/orange/release/app-orange-release.apk
echo.

pause

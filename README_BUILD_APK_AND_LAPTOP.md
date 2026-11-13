# OmniFile V4 Pro — Mobile APK & Laptop Deployment Guide

## 1. How to Get the Installable Android `.apk` From Your Phone (Zero Laptop Needed)
1. Create a free repository on GitHub from your mobile browser.
2. Upload the files from this zip (`www/index.html`, `package.json`, `capacitor.config.json`, and `.github/workflows/build-android-apk.yml`).
3. Tap the **Actions** tab in your GitHub repository -> Run **Build Android APK**.
4. In ~2 minutes, download `OmniFile-Radial-Android-APK.zip` right from the GitHub Actions page and install `app-debug.apk` on your phone!

## 2. How Laptop Users Access It
* **Option A (Instant Local Folder Mount):** Open `www/index.html` in Chrome/Edge on any laptop and click **Mount Real Folder** (uses the native File System Access API to read/write local laptop folders directly) or drag-and-drop files onto the floating `QUICK` bubble.
* **Option B (Windows Explorer Right-Click Integration):** Run `desktop_windows_context_menu.py` alongside `app.py` to add **Open in OmniFile Radial Wheel** directly inside Windows File Explorer.

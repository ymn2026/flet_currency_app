[app]

# (str) Title of your application
title = Your App Name

# (str) Package name
package.name = yourapp

# (str) Package domain (MUST BE UNIQUE - change this!)
package.domain = org.yourdomain

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (glob patterns)
source.include_exts = py,png,jpg,kv,atlas,ttf

# (list) Application requirements
# CRITICAL: Use Python 3.11 (NOT 3.13!)
requirements = python3==3.11.9,kivy==2.3.0,kivymd==2.0.0

# (str) Supported orientation (landscape, portrait or all)
orientation = portrait

# (list) Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# (str) Android API level (33 = Android 13)
android.api = 33

# (int) Android NDK version
android.ndk = 25c

# (str) Android SDK version
android.sdk = 33

# (bool) Enable/disable debugging
android.debug = 1

# (bool) Enable/disable logging
android.logs = 1

# (str) Android architecture
android.arch = arm64-v8a

# (list) Android add-ons (for Google Play Services, etc.)
android.add_src =

# (list) Gradle dependencies
android.gradle_dependencies =

# (list) Proguard rules
android.proguard_rules =

# (str) Android app theme
android.manifest.theme = @android:style/Theme.NoTitleBar

# (str) Android app icon (512x512 PNG)
# android.icon = icon.png

# (str) Android app splash screen
# android.splash = splash.png

# (bool) Enable/disable the App Shortcut feature
android.enable_app_shortcut = False

# ============================================================
# BUILDOZER CONFIGURATION
# ============================================================

[buildozer]

# (str) Path to build output
build_dir = .buildozer

# (str) Path to bin directory
bin_dir = bin

# (str) Log level (debug, info, warning, error, critical)
log_level = 2

# (bool) Warnings are fatal
warn_on_root = 1
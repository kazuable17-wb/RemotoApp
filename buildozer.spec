[app]

title = Meu Remoto
package.name = meu_remoto
package.domain = org.remoto

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0.0
requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.api = 36
android.ndk = 28c
android.debug_artifact = apk

p4a.branch = master

[buildozer]

log_level = 2
warn_on_root = 0

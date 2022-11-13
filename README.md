# shb_py_gui_keyboard_sound - Aplikasi yang Bisa Mengeluarkan Suara saat Keyboard Ditekan

## Link-Link Penting

- Website Utama Saya: https://bit.ly/shb-main
- Akun GitHub Saya: https://bit.ly/shb-github
- Channel YouTube Saya: https://bit.ly/shb-channel
- Berikan Saya Uang Gratis (Traktir Saya): https://bit.ly/shb-traktir

## Software Apakah Ini?

Software ini adalah aplikasi untuk memainkan suara saat keyboard ditekan.

Kita bisa mendaftarkan satu atau lebih file .wav di dalam aplikasi ini untuk dimainkan.

## Screenshot

![ScreenShot](.readme-assets/shb_py_gui_keyboard_sound-1.png?raw=true)

## Cara Mencoba Kode Ini

Untuk menjalankan aplikasi ini, install Python3, masuk ke dalam foldernya via command line, lalu:

Buat virtual environment:

```
python -m venv venv
```

Untuk di windows agar venv bisa diaktifkan:

```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Aktifkan venv:

```
venv/Scripts/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Untuk menjalankannya dalam mode development:

```
python App.py
```

Untuk membuild exe:

```
pyinstaller --onefile App.py
```

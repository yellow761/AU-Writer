Вот исправленное описание проекта на английском языке, с удаленной структурой проекта:

---

# AU Writer - Arch USB Writer

**AU Writer** is a simple and convenient tool for writing ISO images to USB drives. Specially optimized for Arch Linux.

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Arch_Linux-1793D1?style=for-the-badge&logo=arch-linux" alt="Arch Linux">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/GTK-3.0-7C4AFF?style=for-the-badge&logo=gtk" alt="GTK">
  <img src="https://img.shields.io/badge/License-GPLv3-red?style=for-the-badge&logo=gnu" alt="License">
</p>

## ✨ Features

- 🚀 Simple and clean interface like Rufus
- 🌐 Dual language support: English / Русский
- 💾 Write any ISO images (Linux, Windows, etc.)
- 🔧 Auto-formatting before writing (optional)
- 📊 Real-time progress display
- 🛑 Stop writing at any time
- 🐙 Open source on GitHub

## 📦 Requirements

- **OS**: Arch Linux (also works on Debian/Ubuntu)
- **Python**: 3.x
- **GTK**: 3.0
- **Additional**: sudo, parted, dd, lsblk, udevadm

## 🔧 Installation

### Quick Install (Arch Linux)

```bash
# Clone the repository
git clone https://github.com/yellow761/AU-Writer.git
cd AU-Writer

# Install dependencies
sudo pacman -S python-gobject python-gobject-cairo gtk3 dosfstools ntfs-3g exfatprogs e2fsprogs parted systemd util-linux wget

# Make executable
chmod +x au_writer.py

# Run
sudo -E python3 au_writer.py
```

### Install on Debian/Ubuntu

```bash
# Clone the repository
git clone https://github.com/yellow761/AU-Writer.git
cd AU-Writer

# Install dependencies
sudo apt update
sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0 dosfstools ntfs-3g exfatprogs e2fsprogs parted udev util-linux wget

# Make executable
chmod +x au_writer.py

# Run
sudo -E python3 au_writer.py
```

### Install on Fedora

```bash
# Clone the repository
git clone https://github.com/yellow761/AU-Writer.git
cd AU-Writer

# Install dependencies
sudo dnf install python3-gobject python3-gobject-cairo gtk3 dosfstools ntfs-3g exfatprogs e2fsprogs parted systemd-udev util-linux wget

# Make executable
chmod +x au_writer.py

# Run
sudo -E python3 au_writer.py
```

## 🚀 Usage

### Run the Program

```bash
cd AU-Writer
sudo -E python3 au_writer.py
```

### Step-by-Step Guide

1. **Select ISO**: Click "Select ISO" and choose your ISO file
2. **Select USB**: Choose your USB drive from the dropdown
3. **Options**:
   - ✅ Format before writing - Recommended for clean installation
   - 🌐 Language - Switch between English/Русский
4. **Write**: Click "Write" and confirm
5. **Wait**: Progress bar shows writing status
6. **Done**: USB is ready to use!

### Important Notes

- ⚠️ **ALL DATA** on the USB drive will be DESTROYED!
- 🔒 Requires sudo privileges (shown in terminal)

## 🖥️ Create Desktop Shortcut

```bash
cat > ~/.local/share/applications/au-writer.desktop << 'EOF'
[Desktop Entry]
Name=AU Writer
Name[ru]=AU Writer
Comment=Arch USB Writer - Write ISO images to USB drives
Comment[ru]=Arch USB Writer - Запись ISO-образов на USB
Exec=sudo -E python3 /home/$(whoami)/AU-Writer/au_writer.py
Icon=drive-removable-media-usb
Terminal=true
Type=Application
Categories=System;Utility;
StartupNotify=true
EOF
```

## 🔧 Troubleshooting

### "cannot open display" Error

```bash
# Fix display issues
export DISPLAY=:0
sudo -E python3 au_writer.py
```

### "Authorization required" Error

```bash
# Allow root access to display
xhost +SI:localuser:root
sudo python3 au_writer.py
```

### Firefox/GitHub Button Not Working

The program automatically tries multiple methods:
1. GTK show_uri
2. sudo -u user xdg-open
3. Direct browser launch
4. Dialog with URL

### USB Device Not Detected

```bash
# Check USB devices
lsblk -o NAME,SIZE,TYPE,MOUNTPOINT

# Refresh USB list in the program
# Click the "Refresh" button
```

## 🛠️ Development

### Run in Debug Mode

```bash
# Show all log messages
python3 -d au_writer.py
```

### Add New Language

1. Add new language dictionary in `LANGUAGES` variable
2. Update `detect_language()` method for language detection
3. Add language name to `lang_combo` dropdown

### Package as AUR

```bash
# Build PKGBUILD for Arch Linux
makepkg -si
```

## 📝 License

AU Writer is released under the GPLv3 License.

```
Copyright (C) 2024 AU Writer Contributors

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
```

## 🌟 Acknowledgments

- Inspired by Rufus (Windows)
- Built with Python and GTK
- Optimized for Arch Linux community

## 📬 Contact

- **GitHub**: [yellow761/AU-Writer](https://github.com/yellow761/AU-Writer)
- **Issues**: [Report a bug](https://github.com/yellow761/AU-Writer/issues)
- **Discussions**: [Join the conversation](https://github.com/yellow761/AU-Writer/discussions)

## ⭐ Star the Project

If you find AU Writer useful, please consider giving it a ⭐ on GitHub!

<p align="center">
  <a href="https://github.com/yellow761/AU-Writer">
    <img src="https://img.shields.io/github/stars/yellow761/AU-Writer?style=social" alt="GitHub stars">
  </a>
  <a href="https://github.com/yellow761/AU-Writer/network/members">
    <img src="https://img.shields.io/github/forks/yellow761/AU-Writer?style=social" alt="GitHub forks">
  </a>
  <a href="https://github.com/yellow761/AU-Writer/watchers">
    <img src="https://img.shields.io/github/watchers/yellow761/AU-Writer?style=social" alt="GitHub watchers">
  </a>
</p>

---

**Happy writing! 🚀**

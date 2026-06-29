# AU Writer - Arch USB Writer

A simple and convenient tool for writing ISO images to USB drives. Specially optimized for Arch Linux.

<p align="center"> <img src="https://img.shields.io/badge/Platform-Arch_Linux-1793D1?style=for-the-badge&logo=arch-linux" alt="Arch Linux"> <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python" alt="Python"> <img src="https://img.shields.io/badge/GTK-3.0-7C4AFF?style=for-the-badge&logo=gtk" alt="GTK"> <img src="https://img.shields.io/badge/License-GPLv3-red?style=for-the-badge&logo=gnu" alt="License"> <img src="https://img.shields.io/badge/Platform-Linux-FCC624?style=for-the-badge&logo=linux" alt="Linux"> </p>

<p align="center"> <img src="screenshot.png" alt="AU Writer Screenshot" width="650"> </p>

## ✨ Features
🚀 Simple and clean interface like Rufus | 🌐 Dual language support: English / Русский | 💾 Write any ISO images (Linux, Windows, etc.) | 🔧 Format options: Partition scheme (MBR/GPT) and File system (FAT32/NTFS) | 📊 Real-time progress display | 🛑 Stop writing at any time | 🐙 Open source on GitHub

## 📦 Requirements
OS: Arch Linux / Debian / Ubuntu / Fedora | Python: 3.x | GTK: 3.0 | Utilities: sudo, parted, dd, lsblk, udevadm, ntfs-3g, dosfstools

## 🔧 Installation

**Arch Linux:** git clone https://github.com/yellow761/AU-Writer.git && cd AU-Writer && sudo pacman -S python python-gobject gtk3 cairo python-cairo parted dosfstools ntfs-3g e2fsprogs util-linux systemd coreutils && chmod +x au_writer.py && sudo -E python3 au_writer.py

**Ubuntu/Debian:** git clone https://github.com/yellow761/AU-Writer.git && cd AU-Writer && sudo apt update && sudo apt install python3 python3-gi python3-gi-cairo gir1.2-gtk-3.0 parted dosfstools ntfs-3g e2fsprogs util-linux udev coreutils wget && chmod +x au_writer.py && sudo -E python3 au_writer.py

**Fedora:** git clone https://github.com/yellow761/AU-Writer.git && cd AU-Writer && sudo dnf install python3 python3-gobject python3-gobject-cairo gtk3 parted dosfstools ntfs-3g e2fsprogs util-linux systemd-udev coreutils wget && chmod +x au_writer.py && sudo -E python3 au_writer.py

## 🚀 Usage
1. Select ISO – Click "Select ISO" and choose your ISO file | 2. Select USB – Choose your USB drive from the dropdown | 3. Configure options – Format before writing (recommended), Partition scheme (MBR/GPT), File system (FAT32/NTFS), Language (English/Русский) | 4. Write – Click "Write" and confirm | 5. Wait – Progress bar shows writing status | 6. Done – USB is ready to use

## 📋 Recommended Settings
Linux ISO: MBR + FAT32 | Windows 10/11: GPT + NTFS | Windows (legacy): MBR + NTFS | Windows To Go: GPT + NTFS

## 🖥️ Desktop Shortcut
cat > ~/.local/share/applications/au-writer.desktop << 'EOF' && echo "[Desktop Entry]" >> ~/.local/share/applications/au-writer.desktop && echo "Name=AU Writer" >> ~/.local/share/applications/au-writer.desktop && echo "Name[ru]=AU Writer" >> ~/.local/share/applications/au-writer.desktop && echo "Comment=Arch USB Writer - Write ISO images to USB drives" >> ~/.local/share/applications/au-writer.desktop && echo "Comment[ru]=Arch USB Writer - Запись ISO-образов на USB" >> ~/.local/share/applications/au-writer.desktop && echo "Exec=sudo -E python3 /home/$(whoami)/AU-Writer/au_writer.py" >> ~/.local/share/applications/au-writer.desktop && echo "Icon=drive-removable-media-usb" >> ~/.local/share/applications/au-writer.desktop && echo "Terminal=true" >> ~/.local/share/applications/au-writer.desktop && echo "Type=Application" >> ~/.local/share/applications/au-writer.desktop && echo "Categories=System;Utility;" >> ~/.local/share/applications/au-writer.desktop && echo "StartupNotify=true" >> ~/.local/share/applications/au-writer.desktop && EOF

## 🔧 Troubleshooting
**Cannot open display:** export DISPLAY=:0 && sudo -E python3 au_writer.py | **Authorization required:** xhost +SI:localuser:root && sudo python3 au_writer.py | **USB not detected:** lsblk -o NAME,SIZE,TYPE,MOUNTPOINT or dmesg | tail -20 | **Missing dependencies:** Arch: sudo pacman -S ntfs-3g dosfstools parted | Ubuntu: sudo apt install ntfs-3g dosfstools parted | Fedora: sudo dnf install ntfs-3g dosfstools parted

## 🛠️ Development
**Debug mode:** python3 -d au_writer.py | **Add language:** Add dictionary to LANGUAGES, update detect_language(), add to lang_combo | **AUR package:** makepkg -si

## 📝 License
GPLv3 - Copyright (C) 2024 AU Writer Contributors. This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

## 🌟 Acknowledgments
Inspired by Rufus (Windows) | Built with Python and GTK | Optimized for Arch Linux community

## 📬 Contact
GitHub: yellow761/AU-Writer | Issues: Report a bug | Discussions: Join the conversation

## ⭐ Star the Project
If you find AU Writer useful, please consider giving it a ⭐ on GitHub!

<p align="center"> <a href="https://github.com/yellow761/AU-Writer"> <img src="https://img.shields.io/github/stars/yellow761/AU-Writer?style=social" alt="GitHub stars"> </a> <a href="https://github.com/yellow761/AU-Writer/network/members"> <img src="https://img.shields.io/github/forks/yellow761/AU-Writer?style=social" alt="GitHub forks"> </a> <a href="https://github.com/yellow761/AU-Writer/watchers"> <img src="https://img.shields.io/github/watchers/yellow761/AU-Writer?style=social" alt="GitHub watchers"> </a> </p>

Happy writing! 🚀

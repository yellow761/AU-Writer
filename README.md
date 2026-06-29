# AU Writer - Arch USB Writer

AU Writer is a simple and convenient tool for writing ISO images to USB drives. Specially optimized for Arch Linux.

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
- 🔧 Format options: Partition scheme (MBR/GPT) and File system (FAT32/NTFS)
- 📊 Real-time progress display
- 🛑 Stop writing at any time
- 🐙 Open source on GitHub

## 📦 Installation

**Arch Linux:**
```bash
sudo pacman -S python python-gobject gtk3 cairo python-cairo parted dosfstools ntfs-3g e2fsprogs util-linux systemd coreutils
git clone https://github.com/yellow761/AU-Writer.git
cd AU-Writer
chmod +x au_writer.py
sudo -E python3 au_writer.py

Debian/Ubuntu:
bash

sudo apt install python3 python3-gi python3-gi-cairo gir1.2-gtk-3.0 parted dosfstools ntfs-3g e2fsprogs util-linux udev coreutils
git clone https://github.com/yellow761/AU-Writer.git
cd AU-Writer
chmod +x au_writer.py
sudo -E python3 au_writer.py

Fedora:
bash

sudo dnf install python3 python3-gobject python3-gobject-cairo gtk3 parted dosfstools ntfs-3g e2fsprogs util-linux systemd-udev coreutils
git clone https://github.com/yellow761/AU-Writer.git
cd AU-Writer
chmod +x au_writer.py
sudo -E python3 au_writer.py

🚀 Usage

    Select ISO - Click "Select ISO" and choose your ISO file

    Select USB - Choose your USB drive from the dropdown

    Configure options - Format before writing (recommended), Partition scheme (MBR/GPT), File system (FAT32/NTFS), Language (English/Русский)

    Write - Click "Write" and confirm

    Wait - Progress bar shows writing status

    Done - USB is ready to use

📋 Recommended Settings
ISO Type	Partition	File System
Linux ISO	MBR	FAT32
Windows 10/11	GPT	NTFS
Windows (legacy)	MBR	NTFS
Windows To Go	GPT	NTFS
🖥️ Desktop Shortcut
bash

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

🔧 Troubleshooting

Missing dependencies:
bash

# Arch
sudo pacman -S ntfs-3g dosfstools parted
# Debian/Ubuntu
sudo apt install ntfs-3g dosfstools parted
# Fedora
sudo dnf install ntfs-3g dosfstools parted

Cannot open display:
bash

export DISPLAY=:0 && sudo -E python3 au_writer.py

Authorization required:
bash

xhost +SI:localuser:root && sudo python3 au_writer.py

USB not detected:
bash

lsblk -o NAME,SIZE,TYPE,MOUNTPOINT
dmesg | tail -20

📝 License

GPLv3 - Copyright (C) 2024 AU Writer Contributors
🔗 Links

    GitHub: https://github.com/yellow761/AU-Writer

    Issues: https://github.com/yellow761/AU-Writer/issues

    Discussions: https://github.com/yellow761/AU-Writer/discussions

<p align="center"> <a href="https://github.com/yellow761/AU-Writer"> <img src="https://img.shields.io/github/stars/yellow761/AU-Writer?style=social" alt="GitHub stars"> </a> <a href="https://github.com/yellow761/AU-Writer/network/members"> <img src="https://img.shields.io/github/forks/yellow761/AU-Writer?style=social" alt="GitHub forks"> </a> <a href="https://github.com/yellow761/AU-Writer/watchers"> <img src="https://img.shields.io/github/watchers/yellow761/AU-Writer?style=social" alt="GitHub watchers"> </a> </p>

Happy writing! 🚀

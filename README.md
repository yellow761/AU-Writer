# AU Writer - Arch USB Writer

A simple and convenient tool for writing ISO images to USB drives. Specially optimized for Arch Linux.

<p align="center"> <img src="https://img.shields.io/badge/Platform-Arch_Linux-1793D1?style=for-the-badge&logo=arch-linux" alt="Arch Linux"> <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python" alt="Python"> <img src="https://img.shields.io/badge/GTK-3.0-7C4AFF?style=for-the-badge&logo=gtk" alt="GTK"> <img src="https://img.shields.io/badge/License-GPLv3-red?style=for-the-badge&logo=gnu" alt="License"> <img src="https://img.shields.io/badge/Platform-Linux-FCC624?style=for-the-badge&logo=linux" alt="Linux"> <img src="https://img.shields.io/badge/Version-1.0-blue?style=for-the-badge" alt="Version"> </p>

<p align="center"> <img src="screenshot.png" alt="AU Writer Screenshot" width="650"> </p>

## Features
🚀 Simple and clean interface like Rufus | 🌐 Dual language support: English / Русский | 💾 Write any ISO images (Linux, Windows, etc.) | 🔧 Format options: Partition scheme (MBR/GPT) and File system (FAT32/NTFS) | 📊 Real-time progress display | 🛑 Stop writing at any time | 🐙 Open source on GitHub

## Requirements
OS: Arch Linux / Debian / Ubuntu / Fedora | Python: 3.x | GTK: 3.0 | Utilities: sudo, parted, dd, lsblk, udevadm, ntfs-3g, dosfstools

## Installation

**Arch Linux:**
```bash
# 1. Clone the repository
git clone https://github.com/yellow761/AU-Writer.git

# 2. Enter the directory
cd AU-Writer

# 3. Install dependencies
sudo pacman -S python python-gobject gtk3 cairo python-cairo parted dosfstools ntfs-3g e2fsprogs util-linux systemd coreutils

# 4. Make executable
chmod +x au_writer.py

# 5. Run
sudo -E python3 au_writer.py
**Ubuntu/Debian:**
# 1. Clone the repository
git clone https://github.com/yellow761/AU-Writer.git

# 2. Enter the directory
cd AU-Writer

# 3. Update package list
sudo apt update

# 4. Install dependencies
sudo apt install python3 python3-gi python3-gi-cairo gir1.2-gtk-3.0 parted dosfstools ntfs-3g e2fsprogs util-linux udev coreutils wget

# 5. Make executable
chmod +x au_writer.py

# 6. Run
sudo -E python3 au_writer.py

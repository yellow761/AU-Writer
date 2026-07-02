# AU Writer - Arch USB Writer

A simple and convenient tool for writing ISO images to USB drives. Specially optimized for Arch Linux.

<p align="center"> <img src="https://img.shields.io/badge/Platform-Arch_Linux-1793D1?style=for-the-badge&logo=arch-linux" alt="Arch Linux"> <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python" alt="Python"> <img src="https://img.shields.io/badge/GTK-3.0-7C4AFF?style=for-the-badge&logo=gtk" alt="GTK"> <img src="https://img.shields.io/badge/License-GPLv3-red?style=for-the-badge&logo=gnu" alt="License"> <img src="https://img.shields.io/badge/Platform-Linux-FCC624?style=for-the-badge&logo=linux" alt="Linux"> <img src="https://img.shields.io/badge/Version-1.0-blue?style=for-the-badge" alt="Version"> </p>

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
```

**Ubuntu/Debian:**
```bash
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
```
**Fedora:**
```bash
# 1. Clone the repository
git clone https://github.com/yellow761/AU-Writer.git
# 2. Enter the directory
cd AU-Writer
# 3. Install dependencies
sudo dnf install python3 python3-gobject python3-gobject-cairo gtk3 parted dosfstools ntfs-3g e2fsprogs util-linux systemd-udev coreutils wget
# 4. Make executable
chmod +x au_writer.py
# 5. Run
sudo -E python3 au_writer.py
```
**Usage**
1.Select ISO – Click "Select ISO" and choose your ISO file 
2. Select USB – Choose your USB drive from the dropdown 
3. Configure options – Format before writing (recommended), Partition scheme (MBR/GPT), File system (FAT32/NTFS), Language (English/Русский) 
4. Write – Click "Write" and confirm 
5. Wait – Progress bar shows writing status 
6. Done – USB is ready to use

**Desktop Shortcut**
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
**Troubleshooting**
1. **Cannot open display:**
```bash
export DISPLAY=:0 && sudo -E python3 au_writer.py
```
2. **Authorization required**
```bash
xhost +SI:localuser:root && sudo python3 au_writer.py
```
3. **USB not detected**
```bash
lsblk -o NAME,SIZE,TYPE,MOUNTPOINT or dmesg | tail -20
```
4. **Missing dependencies:**
- **Arch:**
```bash
sudo pacman -S ntfs-3g dosfstools parted
```
- **Ubuntu:** 
```bash
sudo apt install ntfs-3g dosfstools parted
```
- **Fedora:**
```bash
sudo dnf install ntfs-3g dosfstools parted
```
## Development

- **Debug mode:** `python3 -d au_writer.py` - run with debug output
- **Add language:** Add dictionary to `LANGUAGES`, update `detect_language()`, add to `lang_combo`
- **AUR package:** `makepkg -si` - build Arch Linux package\

## License
This project is licensed under the **GPLv3 License** - see the [LICENSE](LICENSE) file for details.

## Links
- **GitHub:** https://github.com/yellow761/AU-Writer
- **Issues:** https://github.com/yellow761/AU-Writer/issues

<p align="center"> <a href="https://github.com/yellow761/AU-Writer"> <img src="https://img.shields.io/github/stars/yellow761/AU-Writer?style=social" alt="GitHub stars"> </a> <a href="https://github.com/yellow761/AU-Writer/network/members"> <img src="https://img.shields.io/github/forks/yellow761/AU-Writer?style=social" alt="GitHub forks"> </a> <a href="https://github.com/yellow761/AU-Writer/watchers"> <img src="https://img.shields.io/github/watchers/yellow761/AU-Writer?style=social" alt="GitHub watchers"> </a> </p>

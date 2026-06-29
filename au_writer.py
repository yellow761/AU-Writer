#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# AU Writer - Arch USB Writer
# Copyright (C) 2024 yellow761
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GLib', '2.0')
from gi.repository import Gtk, GLib
import os
import subprocess
import threading
import time
import re
import shutil
import sys
import warnings
import pwd

warnings.filterwarnings("ignore")

os.environ['NO_AT_BRIDGE'] = '1'
os.environ['GTK_USE_PORTAL'] = '0'
os.environ['GSETTINGS_BACKEND'] = 'memory'
os.environ['GTK_MODULES'] = ''
os.environ['GDK_PIXBUF_MODULE_FILE'] = ''

LANGUAGES = {
    'en': {
        'window_title': 'AU Writer - Arch USB Writer',
        'select_iso': 'Select ISO',
        'select_iso_title': 'Select ISO image',
        'cancel': 'Cancel',
        'ok': 'OK',
        'yes': 'Yes',
        'no': 'No',
        'no_file': 'No file selected',
        'iso_files': 'ISO files',
        'all_files': 'All files',
        'usb_device': 'USB drive',
        'refresh': 'Refresh',
        'select_usb': 'Select USB drive',
        'no_usb': 'No USB devices',
        'format_before': 'Format before writing',
        'partition_scheme': 'Partition scheme:',
        'file_system': 'File system:',
        'write': 'Write',
        'stop': 'Stop',
        'version': 'AU Writer v1.0',
        'checking_mount': 'Checking mount...',
        'unmounting': 'Unmounting {}',
        'unmounted': 'Unmounting complete',
        'formatting': 'Formatting USB ({})...',
        'format_complete': 'Formatting complete',
        'format_error': 'Formatting error: {}',
        'writing': 'Writing {} to {}',
        'write_progress': 'Writing: {:.1f}%',
        'write_complete': 'Write completed successfully!',
        'write_success_msg': 'ISO image successfully written to USB drive.',
        'write_error': 'Write error (code {})',
        'write_error_msg': 'An error occurred while writing the ISO image.',
        'sync': 'Synchronizing...',
        'error': 'Error: {}',
        'stopped': 'Stopped',
        'stop_confirm': 'Stop writing?',
        'stop_confirm_text': 'This may damage the USB drive!',
        'warning': 'WARNING!',
        'confirm_write': 'You are about to write:\nISO: {}\nDevice: {}\nPartition: {}\nFS: {}\n\nALL DATA ON USB DRIVE WILL BE DESTROYED!\nContinue?',
        'selected_iso': 'Selected ISO: {}',
        'selected_usb': 'Selected: {}',
        'no_usb_available': 'No USB devices available',
        'language': 'Language:',
        'github': 'GitHub'
    },
    'ru': {
        'window_title': 'AU Writer - Arch USB Writer',
        'select_iso': 'Выбрать ISO',
        'select_iso_title': 'Выберите ISO-образ',
        'cancel': 'Отмена',
        'ok': 'ОК',
        'yes': 'Да',
        'no': 'Нет',
        'no_file': 'Файл не выбран',
        'iso_files': 'ISO файлы',
        'all_files': 'Все файлы',
        'usb_device': 'USB-накопитель',
        'refresh': 'Обновить',
        'select_usb': 'Выберите USB-накопитель',
        'no_usb': 'Нет USB-устройств',
        'format_before': 'Форматировать перед записью',
        'partition_scheme': 'Схема разделов:',
        'file_system': 'Файловая система:',
        'write': 'Записать',
        'stop': 'Остановить',
        'version': 'AU Writer v1.0',
        'checking_mount': 'Проверка монтирования...',
        'unmounting': 'Размонтирование {}',
        'unmounted': 'Размонтирование выполнено',
        'formatting': 'Форматирование USB ({})...',
        'format_complete': 'Форматирование завершено',
        'format_error': 'Ошибка форматирования: {}',
        'writing': 'Запись {} на {}',
        'write_progress': 'Запись: {:.1f}%',
        'write_complete': 'Запись успешно завершена!',
        'write_success_msg': 'ISO-образ успешно записан на USB-накопитель.',
        'write_error': 'Ошибка записи (код {})',
        'write_error_msg': 'Произошла ошибка при записи ISO-образа.',
        'sync': 'Синхронизация...',
        'error': 'Ошибка: {}',
        'stopped': 'Остановлено',
        'stop_confirm': 'Остановить запись?',
        'stop_confirm_text': 'Это может привести к повреждению USB-накопителя!',
        'warning': 'ВНИМАНИЕ!',
        'confirm_write': 'Вы собираетесь записать:\nISO: {}\nУстройство: {}\nРазметка: {}\nФС: {}\n\nВСЕ ДАННЫЕ НА USB-НАКОПИТЕЛЕ БУДУТ УНИЧТОЖЕНЫ!\nПродолжить?',
        'selected_iso': 'Выбран ISO: {}',
        'selected_usb': 'Выбран: {}',
        'no_usb_available': 'Нет доступных USB-устройств',
        'language': 'Язык:',
        'github': 'GitHub'
    }
}

class AUWriterWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_default_size(650, 500)
        self.set_border_width(10)
        self.set_position(Gtk.WindowPosition.CENTER)
        
        self.current_lang = self.detect_language()
        self.iso_path = None
        self.usb_device = None
        self.process = None
        self.is_running = False
        
        # Default settings
        self.partition_scheme = 'msdos'  # msdos or gpt
        self.file_system = 'fat32'       # fat32 or ntfs
        
        self.create_ui()
        self.update_ui_texts()
    
    def _(self, key):
        return LANGUAGES[self.current_lang].get(key, key)
    
    def detect_language(self):
        lang = os.environ.get('LANG', 'en')
        if lang.startswith('ru'):
            return 'ru'
        return 'en'
    
    def get_original_user(self):
        """Get the original user who ran sudo"""
        try:
            if 'SUDO_USER' in os.environ:
                return os.environ['SUDO_USER']
            
            if os.geteuid() == 0:
                try:
                    result = subprocess.run(['who', 'am', 'i'], 
                                          capture_output=True, text=True)
                    if result.stdout:
                        return result.stdout.split()[0]
                except:
                    pass
                
                try:
                    with open('/etc/passwd', 'r') as f:
                        for line in f:
                            parts = line.split(':')
                            if len(parts) >= 3:
                                try:
                                    uid = int(parts[2])
                                    if uid >= 1000 and uid < 65534:
                                        return parts[0]
                                except:
                                    pass
                except:
                    pass
            
            return os.environ.get('USER', '')
        except:
            return os.environ.get('USER', '')
    
    def open_url_as_user(self, url):
        """Open URL as the original user (not root)"""
        user = self.get_original_user()
        
        if not user or user == 'root':
            user = os.environ.get('USER', '')
        
        open_commands = [
            ['sudo', '-u', user, 'xdg-open', url],
            ['sudo', '-u', user, 'firefox', url],
            ['sudo', '-u', user, 'google-chrome', url],
            ['sudo', '-u', user, 'chromium', url],
            ['sudo', '-u', user, 'brave-browser', url],
            ['sudo', '-u', user, 'opera', url],
            ['sudo', '-u', user, 'dbus-launch', '--exit-with-session', 'xdg-open', url],
            ['xdg-open', url],
        ]
        
        env = {
            'DISPLAY': os.environ.get('DISPLAY', ':0'),
            'XAUTHORITY': os.environ.get('XAUTHORITY', ''),
            'DBUS_SESSION_BUS_ADDRESS': os.environ.get('DBUS_SESSION_BUS_ADDRESS', ''),
            'WAYLAND_DISPLAY': os.environ.get('WAYLAND_DISPLAY', ''),
        }
        
        for cmd in open_commands:
            try:
                if cmd[0] == 'sudo' and '-u' in cmd:
                    subprocess.Popen(cmd, 
                                   env={**os.environ, **env},
                                   stdout=subprocess.DEVNULL,
                                   stderr=subprocess.DEVNULL)
                    return True
                else:
                    subprocess.Popen(cmd,
                                   stdout=subprocess.DEVNULL,
                                   stderr=subprocess.DEVNULL)
                    return True
            except:
                continue
        
        return False
    
    def create_ui(self):
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(main_box)
        
        # Top bar with title and language
        top_bar = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        main_box.pack_start(top_bar, False, False, 0)
        
        header = Gtk.Label()
        header.set_markup("<big><b>⚡ AU Writer</b></big>")
        header.set_halign(Gtk.Align.START)
        top_bar.pack_start(header, True, True, 0)
        
        lang_label = Gtk.Label(label=self._('language'))
        top_bar.pack_start(lang_label, False, False, 0)
        
        self.lang_combo = Gtk.ComboBoxText()
        self.lang_combo.append_text("English")
        self.lang_combo.append_text("Русский")
        self.lang_combo.set_active(0 if self.current_lang == 'en' else 1)
        self.lang_combo.connect("changed", self.on_language_changed)
        top_bar.pack_start(self.lang_combo, False, False, 0)
        
        self.github_button = Gtk.Button(label="🐙 " + self._('github'))
        self.github_button.connect("clicked", self.on_github)
        top_bar.pack_start(self.github_button, False, False, 0)
        
        # ISO selection
        self.iso_frame = Gtk.Frame(label=self._('select_iso'))
        self.iso_frame.set_margin_top(10)
        self.iso_frame.set_margin_bottom(10)
        main_box.pack_start(self.iso_frame, False, False, 0)
        
        iso_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        iso_box.set_margin_start(10)
        iso_box.set_margin_end(10)
        iso_box.set_margin_top(10)
        iso_box.set_margin_bottom(10)
        self.iso_frame.add(iso_box)
        
        self.iso_label = Gtk.Label(label=self._('no_file'))
        self.iso_label.set_halign(Gtk.Align.START)
        iso_box.pack_start(self.iso_label, True, True, 0)
        
        self.iso_button = Gtk.Button(label=self._('select_iso'))
        self.iso_button.connect("clicked", self.on_select_iso)
        iso_box.pack_start(self.iso_button, False, False, 0)
        
        # USB selection
        self.usb_frame = Gtk.Frame(label=self._('usb_device'))
        self.usb_frame.set_margin_top(10)
        self.usb_frame.set_margin_bottom(10)
        main_box.pack_start(self.usb_frame, False, False, 0)
        
        usb_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        usb_box.set_margin_start(10)
        usb_box.set_margin_end(10)
        usb_box.set_margin_top(10)
        usb_box.set_margin_bottom(10)
        self.usb_frame.add(usb_box)
        
        self.usb_combo = Gtk.ComboBoxText()
        self.usb_combo.set_hexpand(True)
        self.refresh_usb_list()
        usb_box.pack_start(self.usb_combo, True, True, 0)
        
        self.refresh_button = Gtk.Button(label=self._('refresh'))
        self.refresh_button.connect("clicked", self.on_refresh_usb)
        usb_box.pack_start(self.refresh_button, False, False, 0)
        
        self.usb_info_label = Gtk.Label(label="")
        self.usb_info_label.set_markup("<span size='small' color='gray'>" + self._('select_usb') + "</span>")
        self.usb_info_label.set_halign(Gtk.Align.START)
        main_box.pack_start(self.usb_info_label, False, False, 0)
        
        # Format options
        format_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        format_box.set_margin_top(5)
        format_box.set_margin_bottom(5)
        main_box.pack_start(format_box, False, False, 0)
        
        self.format_check = Gtk.CheckButton(label=self._('format_before'))
        self.format_check.set_active(True)
        format_box.pack_start(self.format_check, False, False, 0)
        
        # Partition scheme
        part_label = Gtk.Label(label=self._('partition_scheme'))
        format_box.pack_start(part_label, False, False, 0)
        
        self.partition_combo = Gtk.ComboBoxText()
        self.partition_combo.append_text("MBR")
        self.partition_combo.append_text("GPT")
        self.partition_combo.set_active(0)
        self.partition_combo.connect("changed", self.on_partition_changed)
        format_box.pack_start(self.partition_combo, False, False, 0)
        
        # File system
        fs_label = Gtk.Label(label=self._('file_system'))
        format_box.pack_start(fs_label, False, False, 0)
        
        self.fs_combo = Gtk.ComboBoxText()
        self.fs_combo.append_text("FAT32")
        self.fs_combo.append_text("NTFS")
        self.fs_combo.set_active(0)
        self.fs_combo.connect("changed", self.on_fs_changed)
        format_box.pack_start(self.fs_combo, False, False, 0)
        
        # Progress bar
        self.progress_bar = Gtk.ProgressBar()
        self.progress_bar.set_show_text(True)
        main_box.pack_start(self.progress_bar, False, False, 0)
        
        # Log area
        scroll_window = Gtk.ScrolledWindow()
        scroll_window.set_vexpand(True)
        scroll_window.set_min_content_height(100)
        main_box.pack_start(scroll_window, True, True, 0)
        
        self.log_textview = Gtk.TextView()
        self.log_textview.set_editable(False)
        self.log_textview.set_wrap_mode(Gtk.WrapMode.WORD)
        scroll_window.add(self.log_textview)
        
        # Buttons
        button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        button_box.set_margin_top(10)
        main_box.pack_start(button_box, False, False, 0)
        
        self.write_button = Gtk.Button(label=self._('write'))
        self.write_button.connect("clicked", self.on_write)
        self.write_button.set_sensitive(False)
        self.write_button.set_size_request(100, 35)
        button_box.pack_start(self.write_button, False, False, 0)
        
        self.stop_button = Gtk.Button(label=self._('stop'))
        self.stop_button.connect("clicked", self.on_stop)
        self.stop_button.set_sensitive(False)
        self.stop_button.set_size_request(100, 35)
        button_box.pack_start(self.stop_button, False, False, 0)
        
        version_label = Gtk.Label()
        version_label.set_markup("<span size='small' color='gray'>" + self._('version') + "</span>")
        version_label.set_halign(Gtk.Align.END)
        main_box.pack_start(version_label, False, False, 0)
        
        self.show_all()
    
    def on_partition_changed(self, widget):
        active = self.partition_combo.get_active()
        self.partition_scheme = 'gpt' if active == 1 else 'msdos'
    
    def on_fs_changed(self, widget):
        active = self.fs_combo.get_active()
        self.file_system = 'ntfs' if active == 1 else 'fat32'
    
    def on_github(self, widget):
        url = "https://github.com/yellow761/AU-Writer"
        
        try:
            Gtk.show_uri(None, url, Gtk.get_current_event_time())
            return
        except:
            pass
        
        if self.open_url_as_user(url):
            self.log_message("Opened GitHub in browser")
            return
        
        dialog = Gtk.MessageDialog(
            parent=self,
            flags=Gtk.DialogFlags.MODAL,
            type=Gtk.MessageType.INFO,
            buttons=Gtk.ButtonsType.OK,
            message_format="🐙 GitHub"
        )
        dialog.format_secondary_text(
            f"Open this URL in your browser:\n\n"
            f"<b>{url}</b>\n\n"
            f"Or click the link in your terminal."
        )
        dialog.run()
        dialog.destroy()
        
        print(f"\n🔗 GitHub: {url}\n")
    
    def on_language_changed(self, widget):
        active = self.lang_combo.get_active()
        self.current_lang = 'ru' if active == 1 else 'en'
        self.update_ui_texts()
    
    def update_ui_texts(self):
        self.set_title(self._('window_title'))
        
        self.iso_frame.set_label(self._('select_iso'))
        self.usb_frame.set_label(self._('usb_device'))
        
        self.iso_button.set_label(self._('select_iso'))
        self.refresh_button.set_label(self._('refresh'))
        self.write_button.set_label(self._('write'))
        self.stop_button.set_label(self._('stop'))
        self.format_check.set_label(self._('format_before'))
        self.github_button.set_label("🐙 " + self._('github'))
        
        if not self.iso_path:
            self.iso_label.set_text(self._('no_file'))
        else:
            self.iso_label.set_text(os.path.basename(self.iso_path))
        
        self.usb_info_label.set_markup("<span size='small' color='gray'>" + self._('select_usb') + "</span>")
        
        self.update_usb_info()
        self.update_write_button()
    
    def refresh_usb_list(self):
        self.usb_combo.remove_all()
        devices = self.get_usb_devices()
        
        if not devices:
            self.usb_combo.append_text(self._('no_usb'))
            self.usb_combo.set_active(0)
            self.usb_combo.set_sensitive(False)
            return
        
        self.usb_combo.set_sensitive(True)
        for dev in devices:
            label = f"{dev['device']} ({dev['size']})"
            self.usb_combo.append_text(label)
        
        self.usb_combo.set_active(0)
    
    def get_usb_devices(self):
        devices = []
        try:
            result = subprocess.run(
                ['lsblk', '-o', 'NAME,SIZE,TYPE,MOUNTPOINT', '-l', '-n'],
                capture_output=True,
                text=True,
                check=True
            )
            
            for line in result.stdout.strip().split('\n'):
                parts = line.split()
                if len(parts) >= 3:
                    name = parts[0]
                    size = parts[1]
                    dev_type = parts[2]
                    
                    if dev_type == 'disk' and name.startswith(('sd', 'hd')):
                        if self.is_usb_device(name):
                            mount = parts[3] if len(parts) > 3 else ''
                            devices.append({
                                'device': f'/dev/{name}',
                                'size': size,
                                'mount': mount
                            })
        except Exception as e:
            self.log_message(f"Error: {e}")
        
        return devices
    
    def is_usb_device(self, device_name):
        try:
            result = subprocess.run(
                ['udevadm', 'info', '--query=property', f'--name=/dev/{device_name}'],
                capture_output=True,
                text=True,
                check=True
            )
            return 'ID_BUS=usb' in result.stdout
        except:
            return False
    
    def on_select_iso(self, widget):
        dialog = Gtk.FileChooserDialog(
            title=self._('select_iso_title'),
            parent=self,
            action=Gtk.FileChooserAction.OPEN
        )
        dialog.add_buttons(
            self._('cancel'), Gtk.ResponseType.CANCEL,
            self._('ok'), Gtk.ResponseType.OK
        )
        
        filter_iso = Gtk.FileFilter()
        filter_iso.set_name(self._('iso_files'))
        filter_iso.add_pattern("*.iso")
        filter_iso.add_pattern("*.ISO")
        dialog.add_filter(filter_iso)
        
        filter_all = Gtk.FileFilter()
        filter_all.set_name(self._('all_files'))
        filter_all.add_pattern("*")
        dialog.add_filter(filter_all)
        
        response = dialog.run()
        
        if response == Gtk.ResponseType.OK:
            self.iso_path = dialog.get_filename()
            self.iso_label.set_text(os.path.basename(self.iso_path))
            self.log_message(self._('selected_iso').format(self.iso_path))
            self.update_write_button()
        
        dialog.destroy()
    
    def on_refresh_usb(self, widget):
        self.refresh_usb_list()
        self.update_usb_info()
        self.update_write_button()
    
    def update_usb_info(self):
        active = self.usb_combo.get_active()
        if active >= 0:
            text = self.usb_combo.get_active_text()
            if text and text != self._('no_usb'):
                self.usb_info_label.set_text(self._('selected_usb').format(text))
                self.usb_device = text.split(' ')[0]
            else:
                self.usb_info_label.set_text(self._('no_usb_available'))
                self.usb_device = None
    
    def update_write_button(self):
        if self.iso_path and self.usb_device and not self.is_running:
            self.write_button.set_sensitive(True)
        else:
            self.write_button.set_sensitive(False)
    
    def log_message(self, message):
        buffer = self.log_textview.get_buffer()
        end_iter = buffer.get_end_iter()
        buffer.insert(end_iter, f"{time.strftime('%H:%M:%S')} - {message}\n")
        self.log_textview.scroll_to_iter(end_iter, 0.0, False, 0.0, 0.0)
    
    def on_write(self, widget):
        if not self.iso_path or not self.usb_device:
            return
        
        # Get current settings
        partition_label = "MBR" if self.partition_scheme == 'msdos' else "GPT"
        fs_label = "FAT32" if self.file_system == 'fat32' else "NTFS"
        
        dialog = Gtk.MessageDialog(
            parent=self,
            flags=Gtk.DialogFlags.MODAL,
            type=Gtk.MessageType.WARNING,
            buttons=Gtk.ButtonsType.YES_NO,
            message_format=self._('warning')
        )
        dialog.format_secondary_text(
            self._('confirm_write').format(
                os.path.basename(self.iso_path),
                self.usb_device,
                partition_label,
                fs_label
            )
        )
        
        response = dialog.run()
        dialog.destroy()
        
        if response == Gtk.ResponseType.YES:
            self.start_write_process()
    
    def start_write_process(self):
        self.is_running = True
        self.write_button.set_sensitive(False)
        self.stop_button.set_sensitive(True)
        self.progress_bar.set_fraction(0.0)
        self.progress_bar.set_text(self._('checking_mount'))
        
        thread = threading.Thread(target=self.write_thread, daemon=True)
        thread.start()
    
    def format_usb(self, dev):
        """Format USB drive with selected partition scheme and file system"""
        fs_label = "FAT32" if self.file_system == 'fat32' else "NTFS"
        self.log_message(self._('formatting').format(fs_label))
        GLib.idle_add(self.update_progress, 0.2, self._('formatting').format(fs_label))
        
        # Create partition table
        if self.partition_scheme == 'msdos':
            subprocess.run(['sudo', 'parted', '-s', dev, 'mklabel', 'msdos'], check=True, timeout=10)
        else:
            subprocess.run(['sudo', 'parted', '-s', dev, 'mklabel', 'gpt'], check=True, timeout=10)
        
        # Create partition
        subprocess.run(['sudo', 'parted', '-s', dev, 'mkpart', 'primary', '1MiB', '100%'], check=True, timeout=10)
        
        # Format with selected file system
        if self.file_system == 'fat32':
            subprocess.run(['sudo', 'mkfs.vfat', '-F32', f'{dev}1'], check=True, timeout=30)
        else:  # NTFS
            subprocess.run(['sudo', 'mkfs.ntfs', '-Q', f'{dev}1'], check=True, timeout=30)
        
        self.log_message(self._('format_complete'))
    
    def write_thread(self):
        try:
            dev = self.usb_device
            iso_path = self.iso_path
            
            self.log_message(self._('checking_mount'))
            GLib.idle_add(self.update_progress, 0.1, self._('checking_mount'))
            
            # Unmount if mounted
            try:
                result = subprocess.run(['mount'], capture_output=True, text=True, check=True)
                for line in result.stdout.split('\n'):
                    if dev in line and 'type' in line:
                        mount_point = line.split('on')[1].split('type')[0].strip()
                        self.log_message(self._('unmounting').format(mount_point))
                        subprocess.run(['sudo', 'umount', mount_point], check=True)
                        self.log_message(self._('unmounted'))
            except Exception as e:
                self.log_message(self._('format_error').format(e))
            
            # Format if enabled
            if self.format_check.get_active():
                self.format_usb(dev)
                target_dev = f'{dev}1'
            else:
                target_dev = dev
            
            # Write ISO
            self.log_message(self._('writing').format(os.path.basename(iso_path), dev))
            GLib.idle_add(self.update_progress, 0.3, self._('writing'))
            
            cmd = ['sudo', 'dd', f'if={iso_path}', f'of={target_dev}', 'bs=4M', 'status=progress']
            
            self.process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1
            )
            
            iso_size = os.path.getsize(iso_path)
            
            while True:
                line = self.process.stderr.readline()
                if not line and self.process.poll() is not None:
                    break
                if line and 'bytes' in line:
                    try:
                        numbers = re.findall(r'[\d.]+', line.replace(',', ''))
                        if numbers and iso_size > 0:
                            size = float(numbers[0])
                            if 'MiB' in line or 'Mi' in line:
                                size = size * 1024 * 1024
                            elif 'GiB' in line or 'Gi' in line:
                                size = size * 1024 * 1024 * 1024
                            elif 'KB' in line or 'KiB' in line:
                                size = size * 1024
                            
                            progress = min(size / iso_size, 1.0)
                            GLib.idle_add(self.update_progress, progress, 
                                        self._('write_progress').format(progress * 100))
                    except:
                        pass
            
            if self.process.returncode == 0:
                self.log_message(self._('write_complete'))
                GLib.idle_add(self.update_progress, 1.0, self._('write_complete'))
                GLib.idle_add(self.show_completion_message, True)
            else:
                self.log_message(self._('write_error').format(self.process.returncode))
                GLib.idle_add(self.update_progress, 0.0, self._('write_error').format(self.process.returncode))
                GLib.idle_add(self.show_completion_message, False)
            
            self.log_message(self._('sync'))
            subprocess.run(['sync'], check=True)
            
        except Exception as e:
            self.log_message(self._('error').format(e))
            GLib.idle_add(self.update_progress, 0.0, self._('error').format(e))
        finally:
            self.is_running = False
            GLib.idle_add(self.cleanup_ui)
    
    def update_progress(self, fraction, text):
        self.progress_bar.set_fraction(fraction)
        self.progress_bar.set_text(text)
        return False
    
    def cleanup_ui(self):
        self.write_button.set_sensitive(True)
        self.stop_button.set_sensitive(False)
        self.is_running = False
        self.process = None
        self.update_write_button()
        return False
    
    def show_completion_message(self, success):
        if success:
            dialog = Gtk.MessageDialog(
                parent=self,
                flags=Gtk.DialogFlags.MODAL,
                type=Gtk.MessageType.INFO,
                buttons=Gtk.ButtonsType.OK,
                message_format=self._('write_complete')
            )
            dialog.format_secondary_text(self._('write_success_msg'))
        else:
            dialog = Gtk.MessageDialog(
                parent=self,
                flags=Gtk.DialogFlags.MODAL,
                type=Gtk.MessageType.ERROR,
                buttons=Gtk.ButtonsType.OK,
                message_format=self._('write_error').format('')
            )
            dialog.format_secondary_text(self._('write_error_msg'))
        
        dialog.run()
        dialog.destroy()
        return False
    
    def on_stop(self, widget):
        if self.process and self.is_running:
            dialog = Gtk.MessageDialog(
                parent=self,
                flags=Gtk.DialogFlags.MODAL,
                type=Gtk.MessageType.WARNING,
                buttons=Gtk.ButtonsType.YES_NO,
                message_format=self._('stop_confirm')
            )
            dialog.format_secondary_text(self._('stop_confirm_text'))
            
            response = dialog.run()
            dialog.destroy()
            
            if response == Gtk.ResponseType.YES:
                self.log_message(self._('stopped'))
                self.process.terminate()
                self.is_running = False
                self.stop_button.set_sensitive(False)
                self.progress_bar.set_text(self._('stopped'))

class AUWriterApp:
    def __init__(self):
        try:
            Gtk.init([])
        except:
            pass
        
        self.window = AUWriterWindow()
        self.window.connect("destroy", Gtk.main_quit)
        self.window.show_all()

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("⚠️ This program requires sudo privileges!")
        print("Run: sudo python3 au_writer.py")
        sys.exit(1)
    
    try:
        app = AUWriterApp()
        Gtk.main()
    except Exception as e:
        error_str = str(e).lower()
        if "cannot open display" in error_str:
            print("❌ Error: Cannot open display")
            print("\nSolutions:")
            print("1. Run: export DISPLAY=:0 && sudo -E python3 au_writer.py")
            print("2. Run: xhost +SI:localuser:root")
            print("3. Run from local terminal (not SSH)")
        else:
            print(f"Error: {e}")

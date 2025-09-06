# Mosaic
A Python script that combines images into a mosaic and uploads them to an FTP server on a regular schedule.  
Useful for weather cams, security feeds, or any regularly updated images.

---

## ✨ Features

- ✅ Combine 4 images (2x2 grid) into a single mosaic (PNG or JPEG).
- ✅ Automatic FTP upload with clean reconnects every cycle.
- ✅ Configurable schedule (default: every 5 minutes).
- ✅ Logging with timestamps for easy monitoring.
- ✅ Handles errors gracefully without stopping.

---

## ⚡ Requirements

- Python 3.8+
- [Pillow](https://pypi.org/project/Pillow/)  
- [schedule](https://pypi.org/project/schedule/)  

Install dependencies:
`pip install pillow schedule`

---

## 👷 Usage

Clone the repo:

git clone https://github.com/YOUR_USERNAME/ftp-mosaic-generator.git
cd ftp-mosaic-generator

Edit the script to:
  Define your image sets
  Set FTP credentials and target directory

Run the script:
  `python mosaic_scheduler.py`

The script will create mosaics and upload them every 5 minutes (or an interval you configure).

## ⚙️ Configuration

Adjust mosaic_sets to define multiple mosaics.

Change schedule.every(5).minutes.do(job) for timing.

Modify output format (.png or .jpg).

## 🤝 Contributing
 
 Issues and pull requests are welcome.
 
<img width="594" height="564" alt="Screenshot 2025-09-04 at 8 11 41 PM" src="https://github.com/user-attachments/assets/2c796e9d-2099-41ff-8c45-7f4d640d0c56" />

 

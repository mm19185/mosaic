from PIL import Image
from ftplib import FTP, error_perm
import schedule
import time
import os
import logging

# Configure logging with timestamps
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Define sets of source images (all must be 960x480 each)
mosaic_sets = [
    {
        "images": ["image1.png", "image2.png", "image3.png", "image4.png"],
        "output": "mosaic1.png"
    },
    {
        "images": ["image5.png", "image6.png", "image7.png", "image8.png"],
        "output": "mosaic2.png"
    }
]

# FTP details
FTP_HOST = "ftp.yourserver.com"
FTP_USER = "your_username"
FTP_PASS = "your_password"
FTP_TARGET_DIR = "/path/on/server/"

def create_mosaic(image_paths, output_path):
    try:
        logging.info(f"Creating mosaic {output_path}...")

        # Open images
        images = [Image.open(p) for p in image_paths]

        # Layout: 2x2 grid
        width, height = images[0].size
        mosaic = Image.new("RGB", (width * 2, height * 2))

        # Paste images
        mosaic.paste(images[0], (0, 0))
        mosaic.paste(images[1], (width, 0))
        mosaic.paste(images[2], (0, height))
        mosaic.paste(images[3], (width, height))

        # Save output
        mosaic.save(output_path, "PNG")
        logging.info(f"Saved mosaic as {output_path}")

        # Upload via FTP
        upload_via_ftp(output_path)

    except Exception as e:
        logging.error(f"Failed to create/upload {output_path}: {e}")

def upload_via_ftp(filename):
    try:
        logging.info(f"Connecting to FTP {FTP_HOST}...")
        with FTP(FTP_HOST, timeout=30) as ftp:
            ftp.login(FTP_USER, FTP_PASS)
            logging.info("FTP login successful")

            ftp.cwd(FTP_TARGET_DIR)
            logging.info(f"Changed directory to {FTP_TARGET_DIR}")

            with open(filename, "rb") as f:
                ftp.storbinary(f"STOR {os.path.basename(filename)}", f)

            logging.info(f"Uploaded {filename} to FTP server")

    except error_perm as e:
        logging.error(f"FTP permission error: {e}")
    except Exception as e:
        logging.error(f"FTP upload failed: {e}")

def job():
    logging.info("Starting new cycle...")
    for m in mosaic_sets:
        create_mosaic(m["images"], m["output"])
    logging.info("Cycle complete")

# Run every 5 minutes
schedule.every(5).minutes.do(job)

logging.info("Scheduler started... (Ctrl+C to stop)")
while True:
    schedule.run_pending()
    time.sleep(1)

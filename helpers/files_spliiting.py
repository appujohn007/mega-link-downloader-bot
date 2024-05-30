import logging
import os
import subprocess

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

from translation import Translation

def split_files(download_directory, splitting_size, splitted_files_directory):
    try:
        # Ensure the output directory exists
        os.makedirs(splitted_files_directory, exist_ok=True)

        # Construct the split command
        command = [
            'split', '-b', str(splitting_size), download_directory,
            os.path.join(splitted_files_directory, 'part_')
        ]

        # Run the command
        subprocess.run(command, check=True)
        logger.info("File split successfully.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to split files: {e}")
    except Exception as e:
        logger.error(f"An error occurred: {e}")

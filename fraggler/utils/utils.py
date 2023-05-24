from pathlib import Path
import logging
from datetime import datetime


def get_files(in_path: str) -> list[Path]:
    # If in_path is a directory, get a list of all .fsa files in it
    if Path(in_path).is_dir():
        files = [x for x in Path(in_path).iterdir() if x.suffix == ".fsa"]
    else:
        files = [Path(in_path)]
    return files


def setup_logging(outdir: str) -> None:
    """
    Set up the logging object and saves the log file to the same dir as the results files.
    """
    NOW = datetime.now().strftime("%Y-%m-%d_%H:%M")

    if not (outdir := Path(outdir)).exists():
        outdir.mkdir(parents=True)

    LOG_FILE = f"{outdir}/fraggler_{NOW}.log"

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] \n%(message)s",
        datefmt="%Y-%m-%d %I:%M:%S",
        handlers=[logging.FileHandler(LOG_FILE), logging.StreamHandler()],
    )

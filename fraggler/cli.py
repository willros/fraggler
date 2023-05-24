import fire
import pandas as pd
from pathlib import Path
import sys
import logging

import fraggler


def analyze(
    in_path: str,
    out_folder: str,
    ladder: str = "LIZ",
    peak_model: str = "gauss",
    min_ratio: float = 0.2,
    min_height: int = 30,
    cutoff: int = 175,
    trace_channel: str = "DATA1",
    peak_height: int = 500,
    custom_peaks: str = None,
    excel: bool = True,
) -> None:

    # Logging
    fraggler.setup_logging(out_folder)
    INFO = f"""
    Runned command:
    {' '.join(sys.argv)}

    Running fraggler with following parameters:
        In path: {in_path}
        Out folder: {out_folder}
        Ladder: {ladder}
        Peak model: {peak_model}
        Min ratio: {min_ratio}
        Min height: {min_height}
        Cutoff: {cutoff}
        Trace channel: {trace_channel}
        Peak Height: {peak_height}
        Custom Peaks: {custom_peaks}
        Excel: {excel}
    """
    logging.info(INFO)

    # Files
    files = fraggler.get_files(in_path)

    # Generate a peak area report for each file
    failed_files = []
    no_peaks = []
    peak_dfs = []
    for file in files:
        logging.info(f"Processing file: {file}")
        fraggler_object = fraggler.make_fraggler_object(
            file=file,
            ladder=ladder,
            min_height=min_height,
            min_ratio=min_ratio,
            trace_channel=trace_channel,
            cutoff=cutoff,
            peak_height=peak_height,
            custom_peaks=custom_peaks,
        )

        # If make_fraggler_object failed
        if isinstance(fraggler_object, str):
            failed_files.append(fraggler_object)
            continue

        if not fraggler_object.peak_areas.found_peaks:
            no_peaks.append(file.stem)

        # generate report and peak table
        if fraggler_object.peak_areas.found_peaks:
            peak_dfs.append(fraggler_object.peak_areas.assays_dataframe(peak_model))
            
        fraggler.peak_area_report(fraggler_object, out_folder, peak_model)

    # Save dataframe
    if peak_dfs:
        df = pd.concat(peak_dfs).reset_index(drop=True)
        out_name = f"{out_folder}/peaktable_{Path(in_path).parts[-1]}"
        if excel:
            df.to_excel(f"{out_name}.xlsx", index=False)
        else:
            df.to_csv(f"{out_name}.csv", index=False)

    # log failed files
    logging.info(f"""
    Fraggler done for files in {in_path}!
    Following files were not analyzed:""")
    if failed_files:
        failed_files = "\n".join(failed_files)
        logging.warning(f"Failed: {failed_files}")
    if no_peaks:
        no_peaks = "\n".join(no_peaks)
        logging.warning(f"No peaks: {no_peaks}")


def run():
    """
    Run the command-line interface using Fire.
    """
    fire.Fire(
        {
            "analyze": analyze,
        }
    )

import pandas as pd
from pathlib import Path
import fraggler


# TODO just take Fraggler object
def generate_peak_table(
    in_files: str | list,
) -> pd.DataFrame:
    if isinstance(in_files, str):
        in_files = [x for x in Path(in_files).iterdir() if x.suffix == ".fsa"]

    peak_dfs = []
    for x in in_files:
        try:
            fsa = fraggler.FsaFile(
                x, ladder, min_height=min_height, trace_channel=trace_channel
            )
            pla = fraggler.PeakLadderAssigner(fsa)
            model = fraggler.FitLadderModel(pla)
            pam = fraggler.PeakAreaDeMultiplex(
                model,
                cutoff=cutoff,
                min_ratio=min_ratio,
                custom_peaks=custom_peaks,
            )
            peak_dfs.append(pam.assays_dataframe(peak_model))
        except:
            print(f"FAILED: {fsa.file_name}")

    return pd.concat(peak_dfs).reset_index(drop=True)

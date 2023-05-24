from dataclasses import dataclass
import logging
from pathlib import Path

import fraggler
from ..applications.peak_area_multiplex import PeakAreaDeMultiplex


@dataclass
class Fraggler:
    fsa: fraggler.FsaFile
    ladder_assigner: fraggler.PeakLadderAssigner
    model: fraggler.FitLadderModel
    peak_areas: PeakAreaDeMultiplex


def make_fraggler_object(
    file: Path,
    ladder: str,
    min_height: int,
    min_ratio: float,
    trace_channel: str,
    cutoff: float,
    peak_height: int,
    custom_peaks: str,
) -> Fraggler | str:
    try:
        fsa = fraggler.FsaFile(
            file,
            ladder,
            min_height=min_height,
            trace_channel=trace_channel,
        )
        ladder_assigner = fraggler.PeakLadderAssigner(fsa)
        model = fraggler.FitLadderModel(ladder_assigner)
        peak_areas = fraggler.PeakAreaDeMultiplex(
            model,
            cutoff=cutoff,
            min_ratio=min_ratio,
            peak_height=peak_height,
            custom_peaks=custom_peaks,
        )

        return Fraggler(
            fsa=fsa,
            ladder_assigner=ladder_assigner,
            model=model,
            peak_areas=peak_areas,
        )

    except Exception as e:
        logging.error(f"""Following file did not work: {file.stem}
        Reason: {e}
        """)

        return file.stem

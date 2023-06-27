from dataclasses import dataclass
import logging
from pathlib import Path

from ..applications.peak_area_multiplex import PeakAreaDeMultiplex
from ..utils.peak_finder import PeakFinder
from ..utils.fsa_file import FsaFile
from ..ladder_fitting.peak_ladder_assigner import PeakLadderAssigner
from ..ladder_fitting.fit_ladder_model import FitLadderModel


@dataclass
class FragglerPeak:
    fsa: FsaFile
    ladder_assigner: PeakLadderAssigner
    model: FitLadderModel
    peaks: PeakFinder


@dataclass
class FragglerArea:
    fsa: FsaFile
    ladder_assigner: PeakLadderAssigner
    model: FitLadderModel
    peaks: PeakFinder
    areas: PeakAreaDeMultiplex


def make_fraggler_peak(
    file: Path,
    ladder: str,
    min_height: int,
    min_ratio: float,
    trace_channel: str,
    peak_height: int,
    custom_peaks: str | None,
    size_standard_channel: str | None,
    distance_between_assays: int,
) -> FragglerPeak | str:
    file = Path(file)
    try:
        fsa = FsaFile(
            file,
            ladder,
            min_height=min_height,
            trace_channel=trace_channel,
            size_standard_channel=size_standard_channel,
        )
        ladder_assigner = PeakLadderAssigner(fsa)
        model = FitLadderModel(ladder_assigner)
        peaks = PeakFinder(
            model,
            min_ratio=min_ratio,
            peak_height=peak_height,
            custom_peaks=custom_peaks,
            distance_between_assays=distance_between_assays,
        )

        return FragglerPeak(
            fsa=fsa,
            ladder_assigner=ladder_assigner,
            model=model,
            peaks=peaks,
        )

    except Exception as e:
        logging.error(
            f"""Following file did not work: {file.stem}
        Reason: {e}
        """
        )

        return file.stem


def make_fraggler_area(
    file: Path,
    ladder: str,
    min_height: int,
    min_ratio: float,
    trace_channel: str,
    peak_height: int,
    custom_peaks: str | None,
    size_standard_channel: str | None,
    distance_between_assays: int,
    cutoff: int,
) -> FragglerArea | str:
    file = Path(file)
    try:
        fsa = FsaFile(
            file,
            ladder,
            min_height=min_height,
            trace_channel=trace_channel,
            size_standard_channel=size_standard_channel,
        )
        ladder_assigner = PeakLadderAssigner(fsa)
        model = FitLadderModel(ladder_assigner)
        peaks = PeakFinder(
            model,
            min_ratio=min_ratio,
            peak_height=peak_height,
            custom_peaks=custom_peaks,
            distance_between_assays=distance_between_assays,
        )
        areas = PeakAreaDeMultiplex(
            peaks,
            cutoff,
        )

        return FragglerArea(
            fsa=fsa,
            ladder_assigner=ladder_assigner,
            model=model,
            peaks=peaks,
            areas=areas,
        )

    except Exception as e:
        logging.error(
            f"""Following file did not work: {file.stem}
        Reason: {e}
        """
        )

        return file.stem

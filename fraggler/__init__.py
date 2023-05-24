"""
fraggler.
Easy Fragment Analyzing in python!
"""

__author__ = "William Rosenbaum and Pär Larsson"

from .ladder_fitting.fit_ladder_model import FitLadderModel
from .ladder_fitting.peak_ladder_assigner import PeakLadderAssigner
from .ladders.ladders import LADDERS
from .plotting.plot_ladder import PlotLadder
from .utils.baseline_removal import baseline_arPLS
from .utils.fsa_file import FsaFile
from .utils.utils import get_files, setup_logging
from .utils.fraggler_object import Fraggler, make_fraggler_object
from .applications.peak_area_multiplex import PeakAreaDeMultiplex
from .plotting.plot_peak_area import PlotPeakArea
from .plotting.plot_raw_data import PlotRawData
from .reports.peak_area_report import peak_area_report
from .functions.generate_peak_table import generate_peak_table


__all__ = [
    "FitLadderModel",
    "PeakLadderAssigner",
    "LADDERS",
    "PlotLadder",
    "baseline_arPLS",
    "FsaFile",
    "PeakArea",
    "PeakAreaDeMultiplex",
    "PlotPeakArea",
    "PlotRawData",
    "generate_peak_table",
    "peak_area_report",
    "Fraggler",
    "make_fraggler_object",
    "get_files",
    "setup_logging",
]

from ..utils.peak_finder import PeakFinder
import matplotlib.pyplot as plt
import numpy as np


class PlotPeaks:
    def __init__(self, peaks: PeakFinder):
        self.peaks = peaks

    @property
    def plot_peaks(self):
        fig_peaks = plt.figure(figsize=(20, 10))

        df = self.peaks.peaks_dataframe.loc[
            lambda x: x.basepairs > self.peaks.peak_information.basepairs.min() - 10
        ].loc[lambda x: x.basepairs < self.peaks.peak_information.basepairs.max() + 10]

        plt.plot(df.basepairs, df.peaks)
        plt.plot(
            self.peaks.peak_information.basepairs,
            self.peaks.peak_information.peaks,
            "o",
        )
        for x, y in zip(
            self.peaks.peak_information.basepairs,
            self.peaks.peak_information.peaks,
        ):
            plt.text(x, y, f"{round(x, 1)} bp")

        channel = self.peaks.model.fsa_file.trace_channel
        plt.title(f"Channel: {channel}")
        plt.xticks(np.arange(df.basepairs.min(), df.basepairs.max(), 10), rotation=90)
        plt.ylabel("intensity")
        plt.xlabel("basepairs")
        plt.grid()
        plt.close()

        return fig_peaks

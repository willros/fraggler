from fraggler.applications.peak_area_multiplex import PeakAreaDeMultiplex
import matplotlib.pyplot as plt
import numpy as np


class PlotPeakArea:
    def __init__(self, peak_area: PeakAreaDeMultiplex):
        self.peak_area = peak_area

    def plot_peaks(self):
        fig_peaks = plt.figure(figsize=(20, 10))

        df = self.peak_area.peaks_dataframe.loc[
            lambda x: x.basepairs > self.peak_area.peak_information.basepairs.min() - 10
        ].loc[
            lambda x: x.basepairs < self.peak_area.peak_information.basepairs.max() + 10
        ]

        plt.plot(df.basepairs, df.peaks)
        plt.plot(
            self.peak_area.peak_information.basepairs,
            self.peak_area.peak_information.peaks,
            "o",
        )
        for x, y in zip(
            self.peak_area.peak_information.basepairs,
            self.peak_area.peak_information.peaks,
        ):
            plt.text(x, y, f"{round(x, 1)} bp")

        plt.xticks(np.arange(df.basepairs.min(), df.basepairs.max(), 10), rotation=90)
        plt.ylabel("intensity")
        plt.xlabel("basepairs")
        plt.grid()
        plt.close()

        return fig_peaks

    def plot_areas(self, peak_finding_model: str,assay_number: int):
        
        self.peak_area.fit_assay_peaks(peak_finding_model, assay_number)

        fig_areas, axs = plt.subplots(
            1, len(self.peak_area.fit_df), sharey=True, figsize=(20, 10)
        )

        # if there is only one peak
        if len(self.peak_area.fit_df) == 1:
            axs.plot(
                self.peak_area.fit_df[0].basepairs, self.peak_area.fit_df[0].peaks, "o"
            )
            axs.plot(
                self.peak_area.fit_df[0].basepairs, self.peak_area.fit_df[0].fitted
            )
            axs.set_title(
                f"Peak 1 area: {self.peak_area.fit_params[0]['amplitude']: .1f}"
            )
            axs.grid()
        # if more than one peak
        else:
            for i, ax in enumerate(axs):
                ax.plot(
                    self.peak_area.fit_df[i].basepairs,
                    self.peak_area.fit_df[i].peaks,
                    "o",
                )
                ax.plot(
                    self.peak_area.fit_df[i].basepairs, self.peak_area.fit_df[i].fitted
                )
                ax.set_title(
                    f"Peak {i + 1} area: {self.peak_area.fit_params[i]['amplitude']: .1f}"
                )
                ax.grid()

        fig_areas.suptitle(f"Quotient: {self.peak_area.quotient: .2f}")
        fig_areas.legend(["Raw data", "Model"])
        fig_areas.supxlabel("basepairs")
        fig_areas.supylabel("intensity")
        plt.close()

        return fig_areas
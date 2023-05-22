import matplotlib.pyplot as plt
import fraggler


class PlotRawData:
    def __init__(self, fsa: fraggler.FsaFile):
        self.fsa = fsa

    @property
    def plot_raw_data(self):
        fig = plt.figure(figsize=(20, 10))

        plt.plot(self.fsa.trace)
        plt.xlabel("Time")
        plt.ylabel("Intensity")

        plt.close()
        return fig

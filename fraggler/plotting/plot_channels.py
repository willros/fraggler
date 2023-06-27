import pandas as pd
import altair as alt


def make_fsa_data_df(fsa, ladder: bool = False) -> pd.DataFrame:
    data = ["DATA1", "DATA2", "DATA3", "DATA4"]
    if ladder:
        data.append("DATA205")
    dfs = []
    for d in data:
        df = (
            pd.DataFrame()
            .assign(data=fsa.fsa[d])
            .assign(channel=d)
            .assign(time=lambda x: range(x.shape[0]))
        )
        dfs.append(df)
    return pd.concat(dfs)


def plot_fsa_data(fsa: str, ladder: bool = False) -> list:
    alt.data_transformers.disable_max_rows()
    df = make_fsa_data_df(fsa, ladder)

    plots = []
    for channel in df.channel.unique():
        plot = (
            alt.Chart(df.loc[lambda x: x.channel == channel])
            .mark_line()
            .encode(
                alt.X("time:Q", title="Time"),
                alt.Y("data:Q", title="Intensity"),
                alt.Color("channel:N"),
            )
            .properties(
                width=800,
                height=500,
            )  # .interactive()
        )
        plots.append((plot, channel))

    all_data = (
        alt.Chart(df)
        .mark_line()
        .encode(
            alt.X("time:Q", title="Time"),
            alt.Y("data:Q", title="Intensity"),
            alt.Color("channel:N"),
        )
        .properties(
            width=800,
            height=500,
        )  # .interactive()
    )
    plots.append((all_data, "All channels"))
    return plots

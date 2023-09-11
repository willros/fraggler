# Fraggler
![logo](examples/logo.png)

## Description
Fraggler is for fragment analysis in Python!
Fraggler is a Python package that provides functionality for analyzing and generating reports for fsa files. It offers both a Python API and a command-line tool for ease of use.

----------------

### Features
`Peak Area Report Generation`: Fraggler allows you to generate peak area reports for all input files. The package calculates peak areas based on specified parameters and generates a report summarizing the results.

`Combined Peak Table Generation`: Fraggler provides a command-line tool to generate a combined dataframe of peaks for all input files. This allows you to easily analyze and compare peaks across multiple files.

`Customization Options`: Fraggler offers various customization options to tailor the analysis to your specific needs. You can specify parameters such as ladder type, peak model, minimum ratio, minimum height, cutoff value, trace channel, peak height, and even provide a custom peaks file for specific assays and intervals.

## Install

Via pip:
```bash
pip install fraggler
```

## Usage

To get an overview how the library can be used in a python environment, please look at `tutorial.ipynb`.


## CLI Tool
### `fraggler area` and `fraggler peak`

#### Usage
To generate peak area reports and a peak table for all input files, use the `fraggler area` or `fraggler peak` command followed by the required positional arguments and any optional flags.

- If not specified, fraggler finds peaks agnostic in the `fsa file`. To specifiy custom assays with certain peaks and intervals, the user can add a .csv file to the `--custom_peaks` argument. The csv file MUST have the following shape:

| name | start | stop | amount | min_ratio |
|---|---|---|---|
| prt1 | 140 | 150 | 2 | 0.2

If `amount` or `min_ratio` are left emtpy, `fraggler` will take all peaks inside the interval. If amount is not empty, fraggler will include the top `N` peaks in the interval, based on height. If `min_ratio` is set, only peaks with the a ratio of the `min_ratio` of the highest peak is included, *e.g.* if `min_ratio == .02`, only peaks with a height of 20 is included, if the highest peak is 100 units.

```console
fraggler peak IN_PATH OUT_FOLDER --ladder LIZ <flags>
```

#### Positional Arguments
The following positional arguments are required:

- `IN_PATH`: Type `str`. Specifies the input path.
- `OUT_FOLDER`: Type `str`. Specifies the output folder.
- `LADDER`: Type `str`. Specifies the ladder used in the experiment.

#### Flags
The following flags can be used with the `fraggler peak` or `fraggler area` command:

- `-l, --ladder=LADDER`: Type `str`. Specifies the ladder. Default value: 'LIZ'.
- `--peak_model=PEAK_MODEL`: Type `str`. Specifies the peak model. Default value: 'gauss'.
- `--min_ratio=MIN_RATIO`: Type `float`. Specifies the minimum ratio. Default value: 0.3.
- `--min_height=MIN_HEIGHT`: Type `int`. Specifies the minimum height. Default value: 100.
- `--cutoff=CUTOFF`: Type `int`. Specifies the cutoff value. Default value: 175.
- `-t, --trace_channel=TRACE_CHANNEL`: Type `str`. Specifies the trace channel. Default value: 'DATA9'.
- `--peak_height=PEAK_HEIGHT`: Type `int`. Specifies the peak height. Default value: 200.
- `--custom_peaks=CUSTOM_PEAKS`: Type `Optional[str]`. Specifies custom peaks. Default value: None.
- `-e, --excel=EXCEL`: Type: `bool`, Default: True

#### Typical usage
```console
fraggler peak IN_FOLDER OUT_FOLDER ORANGE --min_ratio=0.2 
```









import matplotlib.lines as mlines
import matplotlib.pyplot as plt
import numpy as np
from _utils import get_mbit_str, get_pretty_codec_name
from _bitrate_analyzer import analyze_bitrate


def plot_results(resultsBBB, resultsTOS, resultsSintel):
    secondsBBB, bitratesBBB, _, _ = resultsBBB
    secondsTOS, bitratesTOS, _, _ = resultsTOS
    secondsSintel, bitratesSintel, _, _ = resultsSintel



    # init the plot
    plt.figure(figsize=(19.20, 10.80))

    plt.xlabel('Seconds')
    plt.ylabel('Video Bitrate (Mbps)')
    plt.grid(True)

    # actually plot the data
    bitrate_lineBBB, = plt.plot(secondsBBB, bitratesBBB)
    bitrate_lineTOS, = plt.plot(secondsTOS, bitratesTOS)
    bitrate_lineSintel, = plt.plot(secondsSintel, bitratesSintel)
    # plot vertical lines for keyframes






    # save the plot
    plt.savefig(f'bitrate.png')

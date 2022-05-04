import matplotlib.lines as mlines
import matplotlib.pyplot as plt
import numpy as np
from _utils import get_mbit_str, get_pretty_codec_name
from _bitrate_analyzer import analyze_bitrate
from matplotlib.pyplot import MultipleLocator

def plot_results(resultsBBB, resultsTOS, resultsSintel):
    secondsBBB, bitratesBBB, _, _ = resultsBBB
    secondsTOS, bitratesTOS, _, _ = resultsTOS
    secondsSintel, bitratesSintel, _, _ = resultsSintel
    plt.rc('font', family='Times New Roman', size=12, weight='bold')
    plt.xticks(fontsize=20, rotation=90)
    plt.yticks(fontsize=20)

    # init the plot
    plt.figure(figsize=(25.20, 10.80))

    plt.xlabel('Seconds')
    plt.ylabel('Video Bitrate (Mbps)')
    plt.grid(True)

    # actually plot the data
    bitrate_lineBBB, = plt.plot(secondsBBB, bitratesBBB,linewidth=4)
    bitrate_lineTOS, = plt.plot(secondsTOS, bitratesTOS,linestyle=':',linewidth=4)
    bitrate_lineSintel, = plt.plot(secondsSintel, bitratesSintel,linestyle='-.',linewidth=4)
    # plot vertical lines for keyframes

    x_major_locator = MultipleLocator(10)
    ax = plt.gca()
    # ax为两条坐标轴的实例
    ax.xaxis.set_major_locator(x_major_locator)


    # save the plot
    plt.savefig(f'bitrate.png')

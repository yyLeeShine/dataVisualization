import os
from pathlib import Path
import sys
from _bitrate_analyzer import analyze_bitrate
from _plotter import plot_results
from _file_parser import FileParser

BBB = "out.json"
TOS = "out2.json"
Sintel = "out3.json"


if not os.path.exists(BBB):
		print('File specified for -i could not be found. Exiting.')
		sys.exit()
parser = FileParser()

resultsBBB = parser.run(BBB, 'json', 30)
resultsTOS = parser.run(TOS, 'json', 30)
resultsSintel = parser.run(Sintel, 'json', 30)




plot_results(resultsBBB,resultsTOS,resultsSintel)

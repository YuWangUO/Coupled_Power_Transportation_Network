# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 10:36:37 2020

@author: wany105
"""
"""Power Data Input: Power Network Structure
"""

Padjl = [
    ("1", ["2", "21"]), ("2", ["3"]), ("3", ["4", "14"]),
    ("4", ["5"]), ("5", ["6"]), ("6", ["7"]),
    ("7", ["8", "11"]), ("8", ["9"]), ("9", ["10"]),
    ("10", ["11"]), ("11", ["12"]), ("12", ["60"]),
    ("13", ["20"]), ("14", ["15"]), ("15", ["18", "16"]),
    ("16", ["17"]), ("17", ["19"]), ("18", ["22", "19"]),
    ("19", ["23", "13"]), ("20", ["24"]), ("21", ["26"]),
    ("22", ["25", "23"]),  ("23", ["24"]), ("24", ["32"]),
    ("25", ["27"]), ("26", ["28"]), ("27", ["30"]),
    ("28", ["34", "29"]), ("29", ["30"]), ("30", ["35", "31"]),
    ("31", ["38"]), ("31", ["33"]), ("32", ["33"]),
    ("33", ["36"]), ("34", ["35"]), ("35", ["37"]),
    ("36", ["56"]), ("37", ["39", "38"]), ("38", ["45"]),
    ("39", ["40", "43"]), ("40", ["41"]), ("41", ["42"]),
    ("42", ["46"]), ("43", ["41", "44", "48"]), ("44", ["54"]),
    ("45", ["47"]), ("46", ["45"]), ("47", ["50"]),
    ("48", ["53"]), ("49", []), ("50", ["49"]),
    ("51", ["52"]), ("52", []), ("53", ["57", "55"]),
    ("54", ["53", "58"]), ("55", ["51"]), ("56", []),
    ("57", []), ("58", ["57", "59"]), ("59", []),
    ("60", ["13"])
]

color, name = 'red', 'TX-power'
lat, lon = [29.286, 29.313], [-94.8, -94.777]
nodenum, edgenum = 60, 72

nodefile, edgefile, Type = 'PN.csv', 'PL.csv', 'local'

up_bound, low_bound = 1.5, 0.3
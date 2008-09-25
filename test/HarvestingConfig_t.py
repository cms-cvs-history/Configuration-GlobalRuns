#!/usr/bin/env python

import sys
import getopt

valid = ['run=', 'dataset=', 'global-tag=', 'files=' ]

usage = "Usage: HarvestingConfig_t.py --run=<Run Number to harvest>/n"
usage += "    --dataset=<dataset name>\n"
usage += "    --global-tag=<Global Tag>\n"
usage += "    --files=<comma separated list of LFNs>\n"

runNumber = None
dataset = None
globalTag = None
files = []

try:
    opts, args = getopt.getopt(sys.argv[1:], "", valid)
except getopt.GetoptError, ex:
    print usage
    print str(ex)
    sys.exit(1)

for opt, arg in opts:
    if opt == "--run":
        runNumber = arg

    if opt == "--dataset":
        dataset = arg

    if opt == "--global-tag":
        globalTag = arg

    if opt == "--files":
        files = [ x for x in arg.split(",") if x.strip() != "" ]

if runNumber == None:
    msg = "--run option not provided"
    raise RuntimeError, msg
if dataset == None:
    msg = "--dataset option not provided"
    raise RuntimeError, msg
if globalTag == None:
    msg = "--global-tag option not provided"
    raise RuntimeError, msg
if files == []:
    msg = "--files option not provided"
    raise RuntimeError, msg

from Configuration.GlobalRuns.HarvestingConfig import makeDQMHarvestingConfig

process = makeDQMHarvestingConfig(dataset, runNumber, globalTag, *files)
print process.dumpPython()


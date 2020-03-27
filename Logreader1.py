#!/bin/python
import linecache
import sys
import glob
import os

logfiles = sorted(glob.glob('./*.log'))
print ("absolute path:", os.getcwd())
print ("Filename  ElecEnergy ElecZPE Enthalpy GibbsFreeEnergy LowestFreq")

for logs in logfiles:
    linenum  = sum(1 for line in open(logs))

    Firstfreq        = 0
    Secondfreq       = 0
    ElecEnergy       = 0
    ElecZPE          = 0
    Enthalpy         = 0
    GibbsFreeEnergy  = 0

    FreqChk = 1

    try:
        for line in range(linenum):
            Linedata = linecache.getline(logs,line).split()
            try:
                if Linedata[0] == "Frequencies" and Linedata[1] == "--" and FreqChk == 1:
                    Firstfreq  = Linedata[2]
                    Secondfreq = Linedata[3]
                    FreqChk   = 0

                if Linedata[4] == "zero-point" and Linedata[5] == "Energies=":
                    ElecZPE  = Linedata[6]
                if Linedata[4] == "thermal" and Linedata[5] == "Enthalpies=":
                    Enthalpy  = Linedata[6]
                if Linedata[4] == "thermal" and Linedata[5] == "Free":
                    GibbsFreeEnergy =  Linedata[7]
                if Linedata[0] == "SCF" and Linedata[1] == "Done:":
                    ElecEnergy = Linedata[4]
            except:
                pass

        print (logs,ElecEnergy,ElecZPE,Enthalpy,GibbsFreeEnergy,Firstfreq)

    except:
        pass

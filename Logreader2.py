#!/bin/python
import linecache
import sys

#read commandline
param = sys.argv

#setup parameters
number_atom  = {'1':'H','2':'He','3':'Li','4':'Be','5':'B','6':'C','7':'N','8':'O','9':'F','10':'Ne',
                '11':'Na','12':'Mg','13':'Al','14':'Si','15':'P','16':'S','17':'Cl','18':'Ar','19':'K','20':'Ca',
                '21':'Sc','22':'Ti','23':'V','24':'Cr','25':'Mn','26':'Fe','27':'Co','28':'Ni','29':'Cu','30':'Zn',
                '31':'Ga','32':'Ge','33':'As','34':'Se','35':'Br','36':'Kr','37':'Rb','38':'Sr','39':'Y','40':'Zr',
                '41':'Nb','42':'Mo','43':'Tc','44':'Ru','45':'Rh','46':'Pd','47':'Ag','48':'Cd','49':'In','50':'Sn',
                '51':'Sb','52':'Te','53':'I','54':'Xe','55':'Cs','56':'Ba'}

linenum  = sum(1 for line in open(param[1]))
#tempfile = open('templog','w')

Maximum_Force        = "Null"
RMS_Force            = "Null"
Maximum_Displacement = "Null"
RMS_Displacement     = "Null"
Firstfreq            = "Null"
Secondfreq           = "Null"
OptChk  = 1
FreqChk = 1
OptFlag      = 0
PrintFlag    = 0
PrintedFlag  = 0
ChargeFlag   = 1

try:
    if param[2] == "SI":
        print("-------------paste below in SI--------------")
        for line in range(linenum):
            Linedata = linecache.getline(param[1],line).split()
            try:
                if Linedata[0] == "Frequencies" and Linedata[1] == "--" and FreqChk == 1:
                    Firstfreq  = Linedata[2]
                    Secondfreq = Linedata[3]
                    if float(Firstfreq) > 0:
                        print (" Number of imaginary frequency = 0")
                    elif float(Firstfreq) < 0 and float(Secondfreq) > 0:
                        print (" Number of imaginary frequency = 1")
                    else:
                        print (" Number of imaginary frequency >= 2")
                if Linedata[0] == "Zero-point" and Linedata[1] == "correction=":
                    PrintFlag = 1
                if PrintFlag == 1:
                    Line = linecache.getline(param[1],line)
                    print (Line,)
                if Linedata[4] == "thermal" and Linedata[5] == "Free":
                    PrintFlag = 0
            except:
                pass

        EE = 0
        for line in range(linenum):
            Linedata = linecache.getline(param[1],line).split()
            try:
                if Linedata[0] == "SCF" and Linedata[1] == "Done:":
                    EE = Linedata[4]
            except:
                pass
            if line == linenum-1:
                print (" Electronic Energy =", EE)
                print ("")
        for line in range(linenum):
            Linedata = linecache.getline(param[1],line).split()
            try:
                if Linedata[1] == "Optimized" and Linedata[2] == "Parameters":
                    OptFlag = 1
                    if OptChk == 1:
                        OptChk = 0
                if Linedata[0] == "Standard" and Linedata[1] ==  "orientation:":
                    PrintFlag = OptFlag
                if Linedata[0] == "Rotational":
                    if PrintFlag == 1:
                        PrintedFlag = 1
                    PrintFlag = 0
                if PrintFlag == 1 and Linedata[0].isdigit() == True and PrintedFlag == 0:
                    print(number_atom[Linedata[1]]+" "+ Linedata[3]+" "+ Linedata[4]+" "+Linedata[5])
            except:
                pass

except:
        for line in range(linenum):
            Linedata = linecache.getline(param[1],line).split()
            try:
                if Linedata[0] == "Maximum" and Linedata[1] == "Force":
                    if Linedata[4] == 'YES':
                        Maximum_Force        = "YES"

                if Linedata[0] == "RMS" and Linedata[1] == "Force":
                    if Linedata[4] == 'YES':
                        RMS_Force            = "YES"

                if Linedata[0] == "Maximum" and Linedata[1] == "Displacement":
                    if Linedata[4] == 'YES':
                        Maximum_Displacement = "YES"
                if Linedata[0] == "RMS" and Linedata[1] == "Displacement":
                    if Linedata[4] == 'YES':
                        RMS_Displacement     = "YES"
                if Linedata[0] == "Input" and Linedata[1] ==  "orientation:":
                    Maximum_Force        = "NO"
                    RMS_Force            = "NO"
                    Maximum_Displacement = "NO"
                    RMS_Displacement     = "NO"
                if Linedata[0] == "Frequencies" and Linedata[1] == "--" and FreqChk == 1:
                    Firstfreq  = Linedata[2]
                    Secondfreq = Linedata[3]
                    print ("")
                    if float(Firstfreq) > 0:
                        print ("Number of imerginary frequency = 0")
                    elif float(Firstfreq) < 0 and float(Secondfreq) > 0:
                        print ("Number of imerginary frequency = 1")
                    else:
                        print ("Number of imerginary frequency >= 2")
                    FreqChk   = 0
                if Linedata[1] == "Optimized" and Linedata[2] == "Parameters":
                    OptFlag = 1
                    if OptChk == 1:
                        print ("Maximum_Force       ", Maximum_Force)
                        print ("RMS_Force           ", RMS_Force)
                        print ("Maximum_Displacement", Maximum_Displacement)
                        print ("RMS_Displacement    ", RMS_Displacement)
                        print ("")
                        print ("---Optimized Geometry---")
                        OptChk = 0
                if Linedata[0] == "Standard" and Linedata[1] ==  "orientation:":
                    PrintFlag = OptFlag
                if Linedata[0] == "Rotational":
                    if PrintFlag == 1:
                        PrintedFlag = 1
                    PrintFlag = 0
                if PrintFlag == 1 and Linedata[0].isdigit() == True and PrintedFlag == 0:
                    print (number_atom[Linedata[1]]," ", Linedata[3]," ", Linedata[4]," ", Linedata[5])
            except:
                pass

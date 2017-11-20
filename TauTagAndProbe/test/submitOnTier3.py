import os
import argparse

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i+n]

def splitInBlocks (l, n):
    """split the list l in n blocks of equal size"""
    k = len(l) / n
    r = len(l) % n

    i = 0
    blocks = []
    while i < len(l):
        if len(blocks)<r:
            blocks.append(l[i:i+k+1])
            i += k+1
        else:
            blocks.append(l[i:i+k])
            i += k

    return blocks

###########

parser = argparse.ArgumentParser(description='Command line parser of plotting options')
parser.add_argument('--filelist', dest='filelist', help='filelist', default=None)
parser.add_argument('--folder', dest='folder', help='folder', default=None)
parser.add_argument('--njobs', dest='njobs', help='njobs', type=int, default=None)
parser.add_argument('--isMC', dest='isMC', help='is MC', action='store_true', default=False)
args = parser.parse_args()

njobs = 50
# filelist = open("Data_SingleMu_2016RunB_PromptRecov2_1Luglio.txt")
flistName = "Data_SingleMu_2016RunB_PromptRecov2_1Luglio.txt"
folder = "testSubmitT3TAndP2Luglio"
JSONfile = "Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt"

if args.njobs:
    njobs = args.njobs
if args.filelist:
    flistName = args.filelist
if args.folder:
    folder = args.folder

print "njobs    : " , njobs
print "filelist : " , flistName
print "folder   : " , folder

filelist = open(flistName)

###########

os.system ('source /opt/exp_soft/cms/t3/t3setup')

os.system('mkdir ' + folder)
files = [f.strip() for f in filelist]
print "Input has" , len(files) , "files" 
if njobs > len(files) : njobs = len(files)
filelist.close()

fileblocks = splitInBlocks (files, njobs)

for idx, block in enumerate(fileblocks):
    outRootName = folder + '/Ntuple_' + str(idx) + '.root'
    outJobName  = folder + '/job_' + str(idx) + '.sh'
    outListName = folder + "/filelist_" + str(idx) + ".txt"
    outLogName  = os.getcwd() + "/" + folder + "/log_" + str(idx) + ".txt"

    jobfilelist = open(outListName, 'w')
    for f in block: jobfilelist.write(f+"\n")
    jobfilelist.close()

    if not args.isMC: cmsRun = "cmsRun test.py maxEvents=-1 inputFiles_load="+outListName + " outputFile="+outRootName + " JSONfile="+JSONfile + " >& " + outLogName
    else:             cmsRun = "cmsRun test.py maxEvents=-1 inputFiles_load="+outListName + " outputFile="+outRootName + " >& " + outLogName
    skimjob = open (outJobName, 'w')
    skimjob.write ('#!/bin/bash\n')
    skimjob.write ('export X509_USER_PROXY=~/.t3/proxy.cert\n')
    skimjob.write ('source /cvmfs/cms.cern.ch/cmsset_default.sh\n')
    skimjob.write ('cd %s\n' % os.getcwd())
    skimjob.write ('export SCRAM_ARCH=slc6_amd64_gcc472\n')
    skimjob.write ('eval `scram r -sh`\n')
    skimjob.write ('cd %s\n'%os.getcwd())
    skimjob.write (cmsRun+'\n')
    skimjob.close ()

    os.system ('chmod u+rwx ' + outJobName)
    command = ('/opt/exp_soft/cms/t3/t3submit -long \'' + outJobName +"\'")
    # print command
    os.system (command)

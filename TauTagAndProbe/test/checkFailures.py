import argparse
import os
import sys
import fnmatch

def containsFailure(fname, failureMsg="End Fatal Exception"):
    failed = False
    ff = open(fname)
    for l in ff:
        if failureMsg in l:
            failed = True
            break
    return failed

parser = argparse.ArgumentParser(description='Command line parser of plotting options')
parser.add_argument('--dir', dest='dir', help='dir', default=None)
parser.add_argument('--resubCmd', dest='resubCmd', help='print resubmit cms to copy/paste', action='store_true', default=False)
parser.add_argument('--issueCmd', dest='issueCmd', help='issue the resubmit cmd', action='store_true', default=False)
args = parser.parse_args()

if not args.dir:
    print "please provide a directory : --dir <path>"
    sys.exit()

failedList = []
unfinishedList = []
finishedList = []

for filename in os.listdir(args.dir):
    if fnmatch.fnmatch(filename, 'log_*.txt'):
        # print filename
        if containsFailure(args.dir+'/'+filename):
            failedList.append(filename)
        elif not containsFailure(args.dir+'/'+filename, "MessageLogger Summary"):
            unfinishedList.append(filename)
        else:
            finishedList.append(filename)

print 'Successful jobs: '
print finishedList
print "\nTotal successful jobs: ", len(finishedList)

print '\n-------------------------\n'
print 'Failed jobs: '
print failedList
print "\nTotal failed jobs: ", len(failedList)

print '\n-------------------------\n'
print 'Unfinished jobs: '
print unfinishedList
print "\nTotal unfinished jobs: ", len(unfinishedList)

# python submitOnTier3.py --njobs 50 --folder SingleMuon_2016_B_res --filelist filelists/flist_SingleMuon_2016_B.txt

if args.resubCmd:
    print '\nCommands to issue for a resubmit:\n'
    for failed in failedList:
        # print "------ ", failed
        cmd = ('rm ' + args.dir + '/' + failed + ' ; ')

        ntupleName = failed.replace('log_', 'Ntuple_')
        ntupleName = ntupleName.replace('.txt', '.root')
        cmd += ('rm ' + args.dir + '/' + ntupleName + ' ; ')

        jobName = failed.replace('log_', 'job_')
        jobName = jobName.replace('.txt', '.sh')
        cmd += ('/opt/exp_soft/cms/t3/t3submit -long \'' + args.dir+'/'+jobName +"\'")
        print cmd
        if args.issueCmd:
            os.system(cmd)
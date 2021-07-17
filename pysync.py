import os
import sys

def help():
    print('Usage: pysync [DIR] [DIR]')

def parse(argv):
    if len(argv) != 3:
        help()
        exit()
    else:
        return [os.path.abspath(argv[1]), os.path.abspath(argv[2])]

def get_files(fromDir):
    for root, dirs, files in os.walk(fromDir):
        yield (root, dirs, files)

def gen_names(triples, fromDir, toDir):
    fromDirLen = len(fromDir)
    toDirLen = len(toDir)
    rFiles = []
    rDirs = []
    for root, dirs, files in triples:
        for f in files:
            relativePath = root[fromDirLen:] + '\\' + f
            rFiles.append(relativePath)
        for d in dirs:
            relativePath = root[fromDirLen:] + '\\' + d
            rDirs.append(relativePath)
    return rFiles, rDirs

def make_dirs(toDir, rDirs):
    for rDir in rDirs:
        dir = toDir + rDir
        if not os.path.exists(dir):
            os.makedirs(dir)

def label_files(fromDir, toDir, rFiles):
    notExistsFiles = []
    modifiedFiles = []
    for rFile in rFiles:
        fromFile = fromDir + rFile
        toFile = toDir + rFile
        if not os.path.exists(toFile):
            notExistsFiles.append(rFile)
            continue
        else:
            fmTime = os.path.getmtime(fromFile)
            tmTime = os.path.getmtime(toFile)
            if fmTime != tmTime:
                modifiedFiles.append(rFile)
            continue
    return notExistsFiles, modifiedFiles
        
def copy_files(fromDir, toDir, nFiles, mFiles):
    print('created files:', nFiles)
    print('modified files:', mFiles)
    for f in nFiles:
        os.system('copy ' + fromDir + f + ' ' + toDir + f)
    for f in mFiles:
        os.system('copy ' + fromDir + f + ' ' + toDir + f)

# parser
dirs = parse(sys.argv)
print(dirs)

# look through files
triples = get_files(dirs[0])

# generate complete file name
rFiles, rDirs = gen_names(triples, dirs[0], dirs[1])

# make directories
make_dirs(dirs[1], rDirs)

# label files
notExistsFiles, modifiedFiles = label_files(dirs[0], dirs[1], rFiles)

# copy files
copy_files(dirs[0], dirs[1], notExistsFiles, modifiedFiles)
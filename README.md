# pysync
A python script to synchronize files

All you can do now is to synchronize files from one folder to another. The script only copy the files which are modified or not existing to speed up transmission.

You can use pysync.py as follows:`python pysync.py fromDir toDir`. "start.bat" is a convenient batch script to copy directory that you often modify.

For now the script only support copy files on windows because I use system command to copy rather than shutil.
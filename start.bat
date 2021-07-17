call conda activate base
dir scriptLocation
python pysync.py fromDir toDir
call conda deactivate

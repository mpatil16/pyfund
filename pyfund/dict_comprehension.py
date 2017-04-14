import os
import glob

# finding size of the files present in same folder
def filesource():
    file_sizes = {os.path.realpath(p): os.stat(p).st_size
                  for p in glob.glob('*.py')}
    print(file_sizes)

if __name__ == '__main__':
	filesource()
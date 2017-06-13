import sys, os, hashlib


# Returns a map from directory -> [file1, file2, ...]
def get_file_dict(path):
    dirs = {}
    if path is not None:
        os.chdir(path)
    for d in os.walk(os.getcwd()):
        if d[2] != []:
            dirs[d[0]] = d[2]
    return dirs


# Creates a map from MD5 hash -> [path1/filename1, path2/filename2, ...]
def create_file_map(dirs):
    hash_to_file = {}
    for dir, files in dirs.items():
        for filename in files:
            filepath = dir+'/'+filename
            f = open(filepath)
            filehash = hashlib.md5(f.read()).hexdigest()
            if filehash in hash_to_file:
                hash_to_file[filehash].add(filepath)
            else:
                hash_to_file[filehash] = {filepath}
    return hash_to_file


def print_duplicates(hash_to_file):
    print "* Found the following duplicate files"
    for hash, files in hash_to_file.items():
        if len(files) > 1:
            file_list = list(files)
            print file_list[0].split('/')[-1]
            for file in file_list:
                print '\t' +  file

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "\nUsage: python find_dups.py _directory_\n\n" \
              "_directory_ points to the path, relative or absolute, you want \n" \
              "to start your search for duplicate files in. Example:\n\n" \
              "python find_dups.py .\n"
        exit(0)
    print "* Checking path", sys.argv[1]
    path = sys.argv[1]
    dirs = get_file_dict(path)
    file_map = create_file_map(dirs)
    print_duplicates(file_map)

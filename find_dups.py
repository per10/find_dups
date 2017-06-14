#!/usr/bin/python
import sys, os, hashlib


def get_file_dict(path):
    """
    Traverse the whole tree under the given path and create a dictionary
    mapping each full path to a list of the files contained in that directory.

    Example: {'/home/user/pics/': ['img1.jpg', img2,jpg]}

    :param path: root path to start the search from
    :return: a dictionary mapping each directory to a list of the files
    """
    dirs = {}
    if path is not None:
        os.chdir(path)
    for d in os.walk(os.getcwd()):
        if d[2] != []:
            dirs[d[0]] = d[2]
    return dirs


def create_file_map(directory_dict):
    """
    Create a dictionary that maps the hash value of each unique file to a list
    of the full paths of each copy of that file, even if those files have
    different names.

    :param directory_dict: dictionary mapping directory -> list of files
    :return: dictionary mapping hash value of file to occurences of that file
    """
    hash_to_files_dict = {}
    for directory, files in directory_dict.items():
        for filename in files:
            filepath = directory+'/'+filename
            f = open(filepath)
            filehash = hashlib.md5(f.read()).hexdigest()
            if filehash in hash_to_files_dict:
                hash_to_files_dict[filehash].add(filepath)
            else:
                hash_to_files_dict[filehash] = {filepath}
    return hash_to_files_dict


def print_duplicates(hash_to_files_dict):
    """
    Prints a list of all occurences of a file that occurs more than once in
    the directory tree.

    :param hash_to_files_dict: dictionary mapping hash value of file to occurences of that file
    :return: none
    """
    print "* Found the following duplicate files"
    for hash, files in hash_to_files_dict.items():
        if len(files) > 1:
            file_list = list(files)
            print file_list[0].split('/')[-1]
            for file in file_list:
                print '\t' +  file


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Usage: python find_dups.py _directory_\n\n" \
              "_directory_ points to the path, relative or absolute, in which\n" \
              "to start the search for duplicate files. Example:\n\n" \
              "python find_dups.py .\n"
        exit(0)
    if os.path.isdir(sys.argv[1]):
        print "* Checking path", sys.argv[1]
        dirs = get_file_dict(sys.argv[1])
        file_map = create_file_map(dirs)
        print_duplicates(file_map)
    else:
        print "Invalid path name:", sys.argv[1]

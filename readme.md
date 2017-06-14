find_dups.py
============

In our family we have a history of backing up photos from a range of different digital cameras, mobile phones and USB sticks with photos from friends to our computer. The process has not been very strict though and as you really don't want to overwrite anything we usually create new folders every time we do a new backup. Some are manually copied and some are copied through the software from the camera or phone supplier. It becomes even worse when we, from time to time, switch computers and copy the "repository" to a new computer. As nobody can remember the system (if there ever was one) different directories contain different subsets of pictures from different time periods and devices.

To once and for all try to find all the duplicates and do some cleaning I wrote this simple util in Python. It will traverse a directory structure and create a MD5 hash for each file. It will then list all occurrences of each file that exists in more than one place.

So far I have only tried this out on a Linux environment but I'll try to update it for Windows.
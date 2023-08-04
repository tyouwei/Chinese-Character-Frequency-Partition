# Chinese-Character-Frequency-Partition
A script I created to help sort a large database of chinese characters into separate files of high, medium and low frequency (in usage)

The word is mainly done by script.py which stores all characters as key and frequency rank as value in a hasmap
It then reads through each line in the user's folder one by one referencing to the hashmap and copying the lines onto a new folder as required (which in my case are 3 folders)

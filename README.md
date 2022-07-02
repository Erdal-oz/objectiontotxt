# objectiontotxt
Any update to this tool will be on https://codeberg.org/batu/objectiontotxt and not this github repo

A really really simple program to convert objection files from https://objection.lol/ to readable txt files.

I am not experienced with creating projects or programming stuff for public use so if there are any problems i would appreciate feedback.


## Usage

For giving filenames of the .objection files
```
$ objtotxt --filename file1 file2 file3...
```

For giving the directory where the .objection files are at
```
$ objtotxt -d directory1 directory2...
```

Help:
```
usage: objtotxt [-h] (-f file [file ...] | -d directory [directory ...])

Convert .objection files to txt

optional arguments:
  -h, --help            show this help message and exit
  -f file [file ...], --filename file [file ...]
                        Filename of the .objection file
  -d directory [directory ...], --directory directory [directory ...]
                        convert the .objection files in a directory to readable text file

```

Currently the git commit history is a bit confusing, but i'll try to fix it later on

=======
**Currently only works for courtroom recordings/ objection entries with nicknames**

pypi : https://pypi.org/project/objectionloltotxt/




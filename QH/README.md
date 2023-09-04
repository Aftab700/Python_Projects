## Files for OTX sample processing


### Copying folders from `Sample-Share` location

- put all the OTX Sample-Share path in file `input.txt`. example path: `\\192.168.21.11\Sample-Share\sample_search\20230830-131318`

- run the [copy_folders.bat](copy_folders.bat) file. It will copy all the folders path specified in [input.txt](input.txt) to `New Folder`.

### move all sample files from multiple folders to `sample` directory

- goto newly created `New Folder` where all the Sample-Share folders are copied
- run the [move_files_to_sample_folder.py](move_files_to_sample_folder.py) file.
- It will move all the samples from all subdirectory to new `sample` folder

### Check for apk or compressed files in `sample` folder

- run the [check_archive.py](check_archive.py) file.
- run this file in same direcdirectory as `sample`. not inside `sample` folder.
- It will create apk folder apk and `archive` folder compressed files

### unzip the files in archive folder and hashing





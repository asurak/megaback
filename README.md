megaback
========

Simple uploader for backing up files to Mega storage

How to use
---------
### Set credentials
```
# Configuration
mega_username = ""
mega_password = ""
```

### Upload file
```
python megaback.py upload filename
# returns the https link
```

### Delete file
```
python megaback.py delete link
```

### Cleanup the storage
```
python megaback.py cleanup
```

Requirements
------------
[Mega.py](https://github.com/richardasaurus/mega.py) library

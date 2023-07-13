# Installation
This tool has been uploaded to PyPI, so you can install it as follows:
```shell
pip install bccdl
```

# Usage
It can download the CC subtitles from Bilibili and convert to .ass simply:
```
Usage: bccdl [OPTIONS] IDENTITY

Options:
  General Options:
    -h, --help				Print this help text
    -o, --output			Path of subtitles download
  Boolen Options:
    -b, --bangumi			Bangumi support (must occur before -o/--output if specified

Identity:
  SSID if boolen option (-b/--bangumi) else (in general) BVID
```
Default download to current path

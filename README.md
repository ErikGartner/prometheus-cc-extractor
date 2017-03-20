# Prometheus Common Crawl Extractors
*This repository contains mapreduce extractors to preprocess and extract websites
from the common crawl corpus.*

You may use the `mrjob.conf` to configure running the jobs on AWS EMR.

## Installation
The original ccmrjob repo uses Python 2.7 however this has been upgraded to Python 3. That entails using a different library to read the warc files.

For Python 3:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements_python3.text
```

To do local testing the `get-data.sh` script downloads 100 WET files for testing purpose.
It uses [httpie](https://httpie.org/#installation) for downloading, so either install that or change the script to use cURL or wget.

```
./get-data.sh
```

## Extractors

### Obama Born Extractor
This simple extractors finds documents containing a regex specifing "obama born in".

Locally test using:
```
python obama_born_extractor.py --conf-path mrjob.conf --no-output --output-dir out input/test-1.wet
```

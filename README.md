# Licensing

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Tools

## findDefaultPages.py 

Python script that accepts a file as input which should contain one IP address or one URL per line

For each line in the provided file, this script will:

1. attempt to access http://[ip or url]/
2. pull down content found at http://[ip or url]/
3. check if content matches known default server web pages
4. if page not found or content matches, prints tab delimited output detailing findings 

To use the script:

usage: python findDefaultPages.py -h or python findDefaultPages.py -f [file]
     -h --help:     display help info
     -f --file:     path to file containing urls or ip addresses to query for default webserver pages


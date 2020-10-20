# Licensing

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Tools: findDefaultPages.py

findDefaultPages.py is a python script that accepts a file as input which should contain one IP address or one URL per line

For each line in the provided file, this script will:

1. try http://[ip or url]/
2. print tab delimited output for 404s or default webserver pages found

To use the script:

usage: python findDefaultPages.py -h or python findDefaultPages.py -f [file]
     -h --help:     display help info
     -f --file:     path to file containing urls or ip addresses to query for default webserver pages


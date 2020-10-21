# Licensing

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Tools

## findDefaultPages.py 

Python3 script that accepts a file as input which should contain one IP address or one URL per line

For each line in the provided file, this script will:

1. attempt to access http://[ip or url] and https://[ip or url]
2. pull down content found at http://[ip or url] and https://[ip or url]
3. check if content matches known default server web pages
4. if page not found or content matches, prints tab delimited output detailing findings 

To use the script:
```
usage: python findDefaultPages.py -h or python findDefaultPages.py -f [file]
     -h --help:     display help info
     -f --file:     path to file containing urls or ip addresses to query for default webserver pages
```
## createAttack.py

Python3 script that generates the beginning of an attack script against the url provided. The script uses attack.py.tmpl, replacing variables in the tmpl file with values provided in call to createAttack.py. Once script is created, user should open new script and complete the attack code as outlined in the new script. 

The benefit of using createAttack.py is import statements are written, url request code is written, among other things. User doesn't need to write from scratch.

```
usage: createAttack.py -h
       createAttack.py -u [url] -s [scriptname.py]

     -h --help:     display help info

     -s --script:   required name of script to create
     -u --url:      required url of target site or page ie www.somesite.com
     -p --protocol: protocol ie http, ftp, https
     -o --port:     port ie 80, 443, 8080
     -c --cookie:   cookie value ie PHPSESSID=XXX999XXX
     -a --auth:     value of Authorization header

Example usage creates a scipt called attack.py:

     createAttack.py -u 'www.someurl.com' \
                      -p 'http'  \
                      -a 'Basic bmSomeBasicAuthStringGoesHere9999XXXXXN0TlZrbXhkazM5Sg==' \
                      -s attack.py

     createAttack.py --url 'www.someurl.com' \
                      --protocol 'http'  \
                      --auth 'Basic bmSomeBasicAuthStringGoesHere9999XXXXXN0TlZrbXhkazM5Sg==' \
                      --script attack.py


```

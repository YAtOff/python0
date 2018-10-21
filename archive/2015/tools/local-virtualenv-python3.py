#!/usr/bin/env python
#
# Fetch virtualenv.py securely with dependencies and run
# it standalone.
#
# This stuff is placed into public domain by
#    anatoly techtonik <techtonik@gmail.com>

# --- bootstrap .locally --
#
# this creates .locally/ subdirectory in the script's dir
# and sets a few global variables for convenience:
#
#   ROOT  - absolute path to script dir
#   LOOT  - absolute path to the .locally/ subdir
#
# this provides some helpers:
#
#   wgetsecure(targetdir, filespec, quiet=False)
#                    - download file and check hash/size

filespec = [
  # files needed for standalone virtualenv operation
  dict(
    # filename to save download to (not autodetected for security purpose)
    filename='pip-8.0.2-py2.py3-none-any.whl',
    # md5 hash and size
    hashsize='2056f553d5b593d3a970296f229c1b79 1188805',
    url='https://pypi.python.org/packages/e7/a0/bd35f5f978a5e925953ce02fa0f078a232f0f10fcbe543d8cfc043f74fda/pip-8.0.2-py2.py3-none-any.whl#md5=2056f553d5b593d3a970296f229c1b79',
  ),

  dict(
    filename='setuptools-19.6.1-py2.py3-none-any.whl',
    hashsize='4b9a990c1ff59fd5aa79dde6a9f93cb7 472120',
    url='https://pypi.python.org/packages/ee/b5/595168f70a743d933bac6d4eb131dc9fc4a58fd38c59377a2c3903a7829d/setuptools-19.6.1-py2.py3-none-any.whl#md5=4b9a990c1ff59fd5aa79dde6a9f93cb7',
  ),

  dict(
    filename='virtualenv.py',
    hashsize='d75b65b59d239c32a3cf7b3b24f43dc0 99038',
    url='https://raw.githubusercontent.com/pypa/virtualenv/12.0.7/virtualenv.py',
  ),
]


# --- create .locally/ subdir ---
import os
import sys

ROOT = os.path.abspath(os.path.dirname(__file__))
LOOT = os.path.join(ROOT, '.locally/')
if not os.path.exists(LOOT):
  os.mkdir(LOOT)


# ---[ utilities ]---

import hashlib
from os.path import exists, getsize, join
import urllib.request
import os

def hashsize(path):
  '''
  Generate md5 hash + file size string for the given
  filename path. Used to check integrity of downloads.
  Resulting string is space separated 'hash size':

    >>> hashsize('locally.py')
    'fbb498a1d3a3a47c8c1ad5425deb46b635fac2eb 2006'
  '''
  size = getsize(path)
  h = hashlib.md5()
  with open(path, 'rb') as source:
    while True:
      c = source.read(64*1024)  # read in 64k blocks
      if not c:
        break
      h.update(c)
  return '%s %s' % (h.hexdigest(), size)

class HashSizeCheckFailed(Exception):
  '''Throw when downloaded file fails hash and size check.'''
  pass

def getsecure(targetdir, filespec, quiet=False):
  '''
  Using description in `filespec` list, download
  files from specified URL (if they don't exist)
  and check that their size and md5 hash matches.

  Files are downloaded into `targetdir`. `filespec`
  is a list of entries, each entry is a dictionary
  with obligatory keys: filename, hashsize and url.

    filespec = [ {
      'filename': 'wget.py',
      'hashsize': '4eb39538d9e9f360643a0a0b17579f6940196fe4 12262',
      'url': 'https://bitbucket.org/techtonik/python-wget/raw/2.0/wget.py'
    } ]

  Raises HashSizeCheckFailed if hash/size check
  fails. Set quiet to false to skip printing
  progress messages.
  '''
  # [-] no rollback
  def check(filepath, shize, quiet):
    if not quiet:
      print('Checking hash/size for %s' % filepath)
    if hashsize(filepath) != shize:
      raise HashSizeCheckFailed(
                'Hash/Size mismatch for %s\n  exp: %s\n  act: %s'
                % (filepath, shize, hashsize(filepath)))

  for entry in filespec:
    filepath = join(targetdir, entry['filename'])
    downloaded = False
    if exists(filepath):
      if not quiet:
        print("Downloading " + entry['filename'] + " skipped (already downloaded).")
    else:
      if not quiet:
        print("Downloading %s into %s" % (entry['filename'], targetdir))
      urllib.request.urlretrieve(entry['url'], filepath)
      downloaded = True

    if not entry['hashsize']:
      if not quiet:
        print("Hash/size is not set, check skipped..")
    else:
      try:
        check(filepath, entry['hashsize'], quiet)
      except HashSizeCheckFailed:
        if downloaded:
          # [x] remove file only if it was just downloaded
          os.remove(filepath)
        raise

# ---[ /utils ]---

#--[inline shellrun 2.0 import run]
import subprocess

class Result(object):
    def __init__(self, command=None, retcode=None, output=None):
        self.command = command or ''
        self.retcode = retcode
        self.output = output
        self.success = False
        if retcode == 0:
            self.success = True

def run(command):
    process = subprocess.Popen(command, shell=True)
    process.communicate()
    return Result(command=command, retcode=process.returncode)
#--[/inline]


# ---[ download dependencies ]---
print("Fetching stuff into .locally/")

getsecure(LOOT, filespec)

# ---[ run virtualenv.py ]---

python = sys.executable
cmd = '"%s" %s/virtualenv.py --extra-search-dir="%s" --always-copy' % (python, LOOT, LOOT)
cmd += ' ' + ' '.join(sys.argv[1:])
print("Executing: " + cmd)
run(cmd)
print("Done.")

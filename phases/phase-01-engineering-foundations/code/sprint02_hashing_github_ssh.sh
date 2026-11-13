#!/bin/sh
# Sprint 2 · the Try It commands printed on the image, in order.
# Run: sh sprint02_hashing_github_ssh.sh  (it works in a new folder, sprint02-run/)
set -e
mkdir sprint02-run                                             # setup (not on the image)
cd sprint02-run                                                # setup (not on the image)
echo -n "abc" | sha256sum
echo -n "abd" | sha256sum
echo "my notes" > notes.txt                                     # setup (not on the image)
git hash-object notes.txt
git init \
  --object-format=sha256
git hash-object notes.txt       # not on the image: the same file, now a 64-hex ID

#!/bin/sh
# Sprint 1 · the Essential Commands printed on the image, in order.
# Run: sh sprint01_environment_git_foundations.sh  (it works in a new folder, sprint01-run/)
set -e
mkdir sprint01-run                                             # setup (not on the image)
cd sprint01-run                                                # setup (not on the image)
export GIT_AUTHOR_NAME=me GIT_AUTHOR_EMAIL=me@example.com       # setup (not on the image)
export GIT_COMMITTER_NAME=me GIT_COMMITTER_EMAIL=me@example.com # setup (not on the image)
echo "# notes" > notes.md                                       # setup (not on the image)
git init
git status
git add notes.md
git commit -m "Add notes"
git log --oneline --graph
h=$(git hash-object notes.md)   # the blob's ID: the hash of its content
git cat-file -p "$h"            # <hash> on the image

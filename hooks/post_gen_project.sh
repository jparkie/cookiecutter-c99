#!/bin/bash

set -euo pipefail
IFS=$'\n\t'

#
# Functions:
#

function echo_info() {
	echo "[cookiecutter-c99] INFO post_gen_project.sh - $1" >&1
}


#
# Step 1:
#

echo_info "Initializing Git"
git init

#
# Step 2:
#

echo_info "Initializing Project"
make init

#
# Step 3:
#

echo_info "Committing"
git add .
git commit -n -m "Initial Commit"

#
# Done:
#

echo_info "Done!"
#!/usr/bin/env bash
# Debug build script for Render — prints working dir and contents
set -euo pipefail
echo "PWD: $(pwd)"
echo "Listing root dir:" 
ls -la
echo "Listing job1 dir (if present):"
ls -la job1 || true
echo "Python and pip info:" 
python --version || true
pip --version || true
echo "Installing requirements from job1/requirements.txt"
pip install -r job1/requirements.txt

echo "Done build script"

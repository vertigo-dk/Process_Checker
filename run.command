#!/bin/sh
cd "`dirname "$0"`"
source venv/bin/activate
python process_checker.py

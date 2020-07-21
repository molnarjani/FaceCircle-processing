#!/bin/bash
WORKDIR="$(dirname $0)/.."
cd "$WORKDIR"
/usr/local/opt/python@3.8/bin/python3 scripts/next_meetings.py $1

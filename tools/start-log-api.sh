#!/bin/bash 

PROJECT_NAME="cron-job"
PATH_PROJECT="/home/may-thin-kyi/$PROJECT_NAME"

if [ -d "$PATH_PROJECT" ]; then
    cd "$PATH_PROJECT"
    source .venv/bin/activate
    python3 scripts/log_api_request.py
    
else
    echo "Project path not found! $PATH_PROJECT"
fi

# */5 * * * * /home/may-thin-kyi/cron-job/tools/start-log-api.sh


#!/usr/bin/env bash
LOG="/opt/splunk_project/artifacts/triage_actions.log"
IP="$1"
HITS="$2"
TIME=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

echo "$TIME ACTION: Blocked IP $IP (Hits: $HITS)" >> "$LOG"

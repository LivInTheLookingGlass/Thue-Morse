#!/bin/bash
monitor_memory() {
  min_free_mem=999999999  # Arbitrarily large number to track the minimum
  handle_exit() {
    echo "Lowest free memory seen during the pytest run: $min_free_mem MB"
    exit 0  # Exit the script cleanly
  }
  trap handle_exit SIGTERM
  while true; do
    free_mem=$(free -m | awk '/^Mem:/ {print $4}')  # Get free memory in MB
    if [[ $free_mem -lt $min_free_mem ]]; then
      min_free_mem=$free_mem  # Update if we found a new minimum
    fi
    sleep 5  # Poll every 5 seconds
  done
}

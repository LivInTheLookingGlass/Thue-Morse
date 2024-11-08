#!/bin/bash
monitor_memory() {
  min_free_mem_swap=999999999  # Arbitrarily large number to track the minimum
  handle_exit() {
    echo "Lowest combined free memory + swap seen during the pytest run: $min_free_mem_swap MB"
    exit 0  # Exit the script cleanly
  }
  trap handle_exit SIGTERM
  while true; do
    free_mem=$(free -m | awk '/^Mem:/ {print $4}')  # Get free memory in MB
    free_swap=$(free -m | awk '/^Swap:/ {print $4}')  # Get free swap in MB

    total_free_mem_swap=$((free_mem + free_swap))  # Sum of free memory and swap

    if [[ $total_free_mem_swap -lt $min_free_mem_swap ]]; then
      min_free_mem_swap=$total_free_mem_swap  # Update if we found a new minimum combined value
    fi

    sleep 2
  done
}

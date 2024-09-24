#!/bin/bash

# Path to the Python script
PYTHON_SCRIPT_PATH="$HOME/Documents/rename_screenshot/rename_screenshot.py"

# Path to the virtual environment activation script
VENV_PATH="$HOME/Documents/rename_screenshot/venv/bin/activate"

# Directory for log file
LOG_DIR="$HOME/Documents/rename_screenshot"
LOG_FILE="$LOG_DIR/debug_log.txt"

# Create log directory if it doesn't exist
mkdir -p "$LOG_DIR"

# Activate the virtual environment
if [ -f "$VENV_PATH" ]; then
  source "$VENV_PATH"
  echo "$(date): Activated virtual environment at $VENV_PATH" >> "$LOG_FILE"
else
  echo "$(date): Virtual environment not found at $VENV_PATH" >> "$LOG_FILE"
  exit 1
fi

# Read the first (and only) line of input from stdin
if IFS= read -r file_path; then
  echo "$(date): Received file path: $file_path" >> "$LOG_FILE"
  # Call Python script with the file path and log output and errors
  echo "$(date): Starting Python script" >> "$LOG_FILE"
  python "$PYTHON_SCRIPT_PATH" "$file_path" 2>&1 | tee -a "$LOG_FILE"
  PYTHON_EXIT_CODE=${PIPESTATUS[0]}
  echo "$(date): Python script finished with exit code $PYTHON_EXIT_CODE" >> "$LOG_FILE"

  # Check if the script ran successfully
  if [ $PYTHON_EXIT_CODE -ne 0 ]; then
    echo "$(date): Error processing file: $file_path" >> "$LOG_FILE"
  else
    echo "$(date): Successfully processed file: $file_path" >> "$LOG_FILE"
  fi
else
  echo "$(date): No file path received." >> "$LOG_FILE"
fi
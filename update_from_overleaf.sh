#!/bin/bash

if [ "$#" -lt 2 ]; then
  echo "Usage: $0 <zip-file> <pdf-file> [commit-message]"
  exit 1
fi

ZIP_FILE="$1"
PDF_FILE="$2"
COMMIT_MSG="$3"
SRC_DIR="src"
RENDERED_PDF="rendered.pdf"

if [ ! -f "$ZIP_FILE" ]; then
  echo "Error: ZIP file ($ZIP_FILE) not found."
  exit 2
fi

if [ ! -f "$PDF_FILE" ]; then
  echo "Error: PDF file ($PDF_FILE) not found."
  exit 3
fi

echo "Cleaning up old content..."
rm -rf "$SRC_DIR" "$RENDERED_PDF"

echo "Unpacking ZIP file to $SRC_DIR..."
mkdir -p "$SRC_DIR"
unzip -q "$ZIP_FILE" -d "$SRC_DIR"
rm "$ZIP_FILE"

echo "Moving PDF to $RENDERED_PDF..."
mv "$PDF_FILE" "$RENDERED_PDF"

echo "Adding new files to git..."
git add "$SRC_DIR"/* "$RENDERED_PDF"

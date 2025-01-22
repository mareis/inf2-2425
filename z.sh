#!/bin/bash

# Gå gjennom alle PDF-filer i mappen
for file in *.pdf; do
    # Legg til "z" før filtypen .pdf
    new_name="${file%.pdf}z.pdf"
    
    # Gi nytt navn til filen
    mv "$file" "$new_name"
    
    echo "Endret navn på $file til $new_name"
done

echo "Alle PDF-filer har nå 'z' lagt til i slutten av filnavnene."
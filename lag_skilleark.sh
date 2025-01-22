#!/bin/bash
# Sjekker om Pandoc er installert
if ! command -v pandoc &> /dev/null
then
    echo "Pandoc er ikke installert. Vennligst installer det først."
    exit 1
fi

# Gå til mappen med filene
cd "$(dirname "$0")"

# Oppretter skilleark for hver fil i mappen
for file in *; do
    # Sjekker at det er en fil og ikke et skilleark
    if [[ -f "$file" && "$file" != *_skilleark.pdf ]]; then
        # Fjerner filtypen for å få bare filnavnet
        filename="${file%.*}"
        echo "Lager skilleark for $filename..."
        
        # Bruker Pandoc til å lage en enkel PDF med filnavnet som innhold
        echo "# $filename" | pandoc -o "${filename}_skilleark.pdf"
    fi
done

echo "Alle skilleark er generert."
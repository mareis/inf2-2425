# Fagdag
## Oppgave 1 – Aksjekurser

1.**Dataimport og visning:**  
   - Les inn `aksjekurser.csv` med pandas og vis de 5 første radene.

2. **Tidsserievisualisering:**  
   - Bruk matplotlib eller seaborn til å lage et linjediagram som viser den daglige kursutviklingen for alle fem selskapene over perioden.

3. **Beregning av "Mitt fond":**  
   - Lag en ny kolonne kalt «Mitt fond» der du kombinerer de fem aksjekursene med gitte vekter (f.eks. 20 % for hvert selskap) eller eksperimenter med alternative vektingsstrategier.
   - Diskutér hvordan endringer i vektingen påvirker fondets utvikling.

4. **Prosentvis utvikling:**  
   - Beregn den prosentvise endringen fra første til siste dag for de individuelle aksjene og for «Mitt fond».
   - Sammenlign og diskuter hvilken aksje og hvilket fond som har utviklet seg best.

5. **Avanserte analyser:**  
   - Beregn glidende gjennomsnitt (f.eks. 7-dagers og 14-dagers) for å identifisere trender.
   - Utforsk korrelasjonen mellom de ulike aksjene.

6. **Interaktiv visualisering:**  
   - Lag et interaktivt dashboard med ipywidgets og Voila der brukeren kan:  
     - Velge tidsintervall (via glidere eller dropdown).  
     - Velge hvilke aksjer som skal vises.  
     - Se både linjediagram og tabeller som oppdateres dynamisk etter brukerens valg.

---

## Oppgave 2 – Fotballspillere

1. **Dataimport og beskrivende statistikk:**  
   - Les inn `fotballspillere.csv` med pandas.  
   - Presenter grunnleggende statistikk: beregn gjennomsnitt, median, standardavvik og undersøk fordelingen av antall kamper, mål, assists osv.  
   - Visualiser fordelingen av spillere etter posisjon (f.eks. med et kakediagram eller stolpediagram).

2. **Gruppering og aggregasjon:**  
   - Gruppér spillerne etter klubb, posisjon og debutår.  
   - Beregn gjennomsnittlig antall mål, assists, taklinger og pasninger for hver gruppe.  
   - Diskutér hvordan statistikken varierer mellom for eksempel "Forward" og "Midfielder".

3. **Visualisering:**  
   - Lag søylediagram og boksplott for å sammenligne ytelsen på tvers av posisjoner eller klubber.  
   - Lag et scatterplot for å undersøke sammenhengen mellom antall pasninger og antall mål, eller mellom kamper og assists.

4. **Dynamisk filtrering og interaktiv visualisering:**  
   - Bygg et interaktivt dashboard med ipywidgets og Voila der brukeren kan filtrere ut spillere basert på:  
     - Debutår (f.eks. et slider-intervall)  
     - Posisjon (via dropdown)  
     - Klubb (flervalgsmulighet)  
   - Ved valg skal både tabeller og visualiseringer (f.eks. søylediagram, scatterplot) oppdateres automatisk.

5. **Pivot-tabeller og dashboard:**  
   - Opprett pivot-tabeller for å vise for eksempel gjennomsnittlig antall mål og assists per klubb og posisjon.  
   - Diskuter hvordan slike tabeller kan brukes for å identifisere lag med overlegen angreps- eller forsvarsevne.

---


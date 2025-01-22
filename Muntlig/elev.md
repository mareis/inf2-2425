
## Til Eleven

# Muntlig Eksamen: Dyrehageadministrasjonssystem i Python

## **Prosjektbeskrivelse: Dyrehageadministrasjonssystem**

**Beskrivelse:**
Du skal forklare hvordan du vil utvikle et enkelt system for å administrere dyr og ansatte i en dyrehage ved hjelp av objektorientert programmering i Python. Systemet skal håndtere informasjon om ulike dyr og ansatte, samt tildele dyr til ansatte for stell og omsorg.

## **Kravspesifikasjon**

### 1. **Klasser og Attributter:**
- **Dyr:**
  - `navn` (navn på dyret)
  - `art` (f.eks. løve, elefant)
  - `alder` (alder i år)
- **Ansatt:**
  - `navn` (navn på den ansatte)
  - `ansatt_id` (unik identifikator)
  - `dyr_ansvar` (liste over dyr den ansatte har ansvar for)

### 2. **Funksjonalitet:**
- **Registrere Nytt Dyr:** Administrator kan legge til nye dyr i systemet.
- **Registrere Ny Ansatt:** Administrator kan registrere nye ansatte.
- **Tildele Dyr til Ansatt:** Administrator kan tildele et dyr til en ansatt.
- **Vise Ansattens Dyr:** Vise hvilke dyr en bestemt ansatt har ansvar for.
- **Introduksjon til Arv:** Hvis tiden tillater det, kan du gruppere dyr i kategorier som **Fugler**, **Pattedyr**, og **Reptiler** med spesifikke egenskaper.

## **Eksamenstrinn og Spørsmål**

### **1. Introduksjon og Overordnet Design**

**Spørsmål:**
- Kan du gi en kort oversikt over hvordan du vil strukturere klassene for dette dyrehageadministrasjonssystemet? Hvilke hovedklasser vil du lage, og hva er deres ansvar?

---

### **2. Klasser og Objekter**

**Spørsmål:**
- Kan du beskrive forskjellen mellom en klasse og et objekt? Gi et eksempel relatert til dyrehageadministrasjonssystemet.

---

### **3. Konstruktører og Init-metoden**

**Spørsmål:**
- Hvordan definerer du en konstruktør i Python, og hvordan vil du implementere `__init__`-metoden for klassen `Dyr`?

---

### **4. Attributter og Metoder i Ansatt-klassen**

**Spørsmål:**
- Hvilke attributter og metoder vil du inkludere i `Ansatt`-klassen? Kan du beskrive en metode som tilordner et dyr til en ansatt?

---

### **5. Metoder for Registrering og Tildeling**

**Spørsmål:**
- Hvordan vil du implementere en metode for å registrere et nytt dyr og legge det til en liste over alle dyr i dyrehagen?

---

### **6. Feilhåndtering ved Tildeling av Dyr**

**Spørsmål:**
- Hvordan kan du håndtere situasjoner der en ansatt prøver å tilordne et dyr som allerede er tilordnet til en annen ansatt?

---

### **7. Praktisk Programmering**

**Spørsmål:**
- Kan du skrive et eksempel på hvordan du oppretter et `Dyr`-objekt og en `Ansatt`-objekt, og deretter tilordner dyret til den ansatte?

---

### **8. Testing og Validering**

**Spørsmål:**
- Hvordan kan du teste at `tilordne_dyr`-metoden fungerer korrekt når en ansatt tilordner et dyr?

---

### **9. Introduksjon til Arv**

**Spørsmål:**
- Hvis du ønsker å utvide systemet til å inkludere spesifikke dyretyper som fugler eller reptiler med egne egenskaper, hvordan kan arv være nyttig? Kan du gi et eksempel?

---

## **Eksempel på Implementering uten Arv**

### **Klasse Dyr**

```python
class Dyr:
    def __init__(self, navn, art, alder):
        self.navn = navn
        self.art = art
        self.alder = alder

    def vis_info(self):
        print(f"Dyr: {self.navn}, Art: {self.art}, Alder: {self.alder} år")

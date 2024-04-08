from decorators import print_and_update_score

class WordToNumericValueMixin:
    def __init__(self):
        self.MONOLEXEMISKA_TAL = {
        'noll': 0,
        'ett': 1,
        'två': 2,
        'tre': 3,
        'fyra': 4,
        'fem': 5,
        'sex': 6,
        'sju': 7,
        'åtta': 8,
        'nio': 9,
        'elva': 11,	
        'tolv': 12,
        'tretton': 13,
        'fjorton': 14,
        'femton': 15,
        'sexton': 16,
        'sjuton': 17,
        'arton': 18,
        'nitton': 19,
        'tjugo': 20,
        }

        self.BAS_TAL = {
            'tio': 10,
            'hundra': 100,
            'tusen': 1000,
            }

        self.PREFIX_TILL_BAS = {
            'tusen': {
                'ett': 1,
                'två': 2,
                'tre': 3,
                'fyra': 4,
                'fem': 5,
                'sex': 6,
                'sju': 7,
                'åtta': 8,
                'nio': 9,
                },
            
            'hundra': {
#                'ett': 1,
                'två': 2,
                'tre': 3,
                'fyra': 4,
                'fem': 5,
                'sex': 6,
                'sju': 7,
                'åtta': 8,
                'nio': 9,
                },
            
            'tio': {
                'tret': 3,
                'fyr': 4,
                'fem': 5,
                'sex': 6,
                'sju': 7,
                'åt': 8,
                'nit': 9,
                }
            }

    def word_to_numeric_values(self, input_sträng: str,) -> int:
        """Hanterar konvertering av ord till numeriskavärden/siffror från 0 upp till 9999, bas 10.
        
        Metoden bryter ner en sträng bakifrån genom att undersöka strängen bakifrån mot först fasta värden kopplade till nycklar (MONOLEXEMISKA_TAL), efter att rätt nyckel-värde identifieras skickas summan till en lista. Detta steg för att hantera specialtal som elva, tjugo eller enheter. Dessa raderas (pop()) sedan från strängen som använts för att sedan fortsätta loopen igen tills den inte finner någon nyckel till ordboken MONOLEXEMISKA_TAL. Därefter sker en nästlad loop som tar reda på basvärden som tio för att sedan söka om ett MONOLEXEMISKA_TAL kan hittas innas som sju och multipliceras sedan bas med MONOLEXEMISKA_TAL, om inget MONOLEXEMISKA_TAL hittas ges standard värde på 1 vilket då ger 10, 100 eller 1000. 
        
        OBS: TEKNISK-SKULD: För hantering av högre värden än 9999 eller som 'tolvhundra' behövs en omstrukturering av logiken. 
        Lösning: Skapa en rekursiv loop som delar upp strängen i flera delsträngar genom att söka efter bas tal och jämnföra det mot värdet till höger om det. ifall värdet är större till höger fortsätter sökandet tills den hittar ett bas ord som är större än det till höger och slicar av den delen av strängen till en ny del sträng från basen och allt till vänster om den sedan fortsätter sökandet efter nästa bas på samma vis till ingen mer bas hittas och då antingen bryter ut det som är kvar, om någonting är kvar, så som ett->nio. 
        
        MONOLEXEMISKA_TAL: Ordbok med nyckelord för värden som är bestämda (specialfall).
        BAS_TAL: Ordbok med värdena för bastal så som tio:10 och hundra:100 versionen av 
        PREFIX_TILL_BAS: Nästlad ordbok med värden kopplade till samlingar av bas10 ord så som tio, hundra och tusen upp till 10000.
        """
        MONOLEXEMISKA_TAL = self.MONOLEXEMISKA_TAL
        PREFIX_TILL_BAS = self.PREFIX_TILL_BAS
        BAS_TAL = self.BAS_TAL
        tal_delar = []
        #kan använda import re för att snygga till replace
        input_sträng = input_sträng.replace(' ', '').replace('minuter','').replace('min','').replace('sekunder','').replace('sek','')
        while input_sträng:
            """Loop för att plocka ut bastal för strängen för felhantering."""
            for ord_key in MONOLEXEMISKA_TAL.keys(): 
                ord_längd = len(ord_key)
                if input_sträng[-ord_längd:] == ord_key:
                    tal_delar.append(MONOLEXEMISKA_TAL[ord_key])
                    input_sträng = input_sträng[:-ord_längd]
                    
            """Loop för att hämta basvärde som tio i sju-tio."""
            for bas_key in self.PREFIX_TILL_BAS.keys():
                if bas_key in input_sträng:
                    index_of_base = input_sträng.index(bas_key)  # Hitta indexet för basordet
                    del_sträng = input_sträng[:index_of_base]  # Dela upp strängen före basordet
                    bas = self.BAS_TAL[bas_key]
                    # Sök multiplikatorn i delsträngen.
                    multiplikator = 1
                    for multi_key in self.PREFIX_TILL_BAS[bas_key].keys(): #multikey, value.. .items(): 
                        if multi_key in del_sträng:
                            # Hitta och extrahera multiplikatorn. Om man vill hantera högre värden med flera multiplikatorer som sjutiofemtusen så behövs en annan logik med en lista som lagrar värdena innan basen, skapar det korrekta värdet för sjutiofem för att sedan miltiplicera med basen, då skulle logiken i första loopen kunna användas för allt innan basen och sedan basen som sista multiplikator.
                            multiplikator = PREFIX_TILL_BAS[bas_key][multi_key] # value
                            continue

                    # Beräkna summan och uppdatera tal_delar.
                    summa = bas * multiplikator
                    tal_delar.append(summa)

                    # Uppdatera input_sträng för att ta bort bearbetad del.
                    input_sträng = input_sträng[index_of_base+len(bas_key):]
        
        """Adderar alla värden i listan och retunerar den totala summan när strängen är tom."""
        return(sum(tal_delar))


class GetInputMixin:
    def get_input(self, fråga: str, godkända_svar=None) -> str:
        """Metod för att ta emot validering från input.

        Mixin tillåter både svar kontrollerat mot en godkända_svar, om inte godkända_svar är definierat frågas användaren om korrekt stavningen för att sedan returnera svar (kan användas för att skapa nycklar ex).
        
        fråga: Sträng som frågar efter input.
        godkända_svar: Om det är definierat så kontrolleras input från svar mot listan, om inte så kommer en ytterligare fråga kontrollera att användaren är nöjd med sin input.
        """
        while True:
            try:
                if godkända_svar:
                    svar = input(f"\n{fråga} [{', '.join(godkända_svar)}]: ").lower().strip().replace('.', '')
                    if svar in godkända_svar:
                        return svar
                    else:
                        print("Felaktigt svar, kontrollera stavning och försök igen.")
                else:
                    svar = input(f"{fråga} ").lower().strip().replace('.', '')
                    säkerhetsfråga = input(f"Är detta korrekt: '{svar}'? ja/nej/avbryt ").lower().strip()
                    if säkerhetsfråga == 'ja' or säkerhetsfråga == 'avbryt':
                        return svar
                    elif säkerhetsfråga == 'nej':
                        continue
            except Exception as e:
                print(f"Ett oväntat fel uppstod: {e}. Försök igen.")


class GetUnitsInputMixin(GetInputMixin, WordToNumericValueMixin):
    def __init__(self):
        super().__init__()
        
    def get_units(self, fråga, prompt=None, kontroll_max=None, format=1) -> int:
        """Hämtar ett input som kräver en siffra antingen via bokstavering eller siffra.
        
        fråga: Fråga som används som prompt till hämta_input.
        kontroll_max: om det är definierat så finns ett tak för hur högt värde som är tillåtet.
        prompt_felsvar: Felsvarsmeddelande specifikt för om kontroll_max är definierat för att leda användaren att svara ett svar ifall ett tak eller logik finns för vilka värden som får anges.
        format: Standardvärde är 1 för att hantera bas 10 tal. Kan exempelvis vara 60 om det anges när mixinen används för att hantera HHMM/tid, bas 60 värden.
        """
        while True:
            enheter_sträng = self.get_input(fråga).replace(':', '')
            if enheter_sträng.lower() == 'avbryt':
                return None
            try:
                enheter = int(enheter_sträng)
                #kontroll för att inte kunna godkänna negativa värden
                if enheter < 0:
                    print(f"Du kan inte ange ett negativa nummer")
                    continue
                #om ett kontroll_max har angivits kontrolleras det mot det, om format också angivits så kontrolleras även det
                if kontroll_max:
                    if 0 <= enheter <= kontroll_max and (enheter % 100) < format:
                        return enheter
                    else:
                        print(prompt)
                        continue
                #om inget max (kontroll_max) angivits kontrolleras bara att det är en int
                elif not kontroll_max:
                    return enheter
            except ValueError:
                #försöker konvertera ord i strängen till nummer
                enheter = self.word_to_numeric_values(enheter_sträng)
                if enheter is not None:
                    if kontroll_max is None or 0 <= enheter <= kontroll_max:
                        return enheter
                print("Någonting gick fel, försök igen.")
                continue
            except Exception as e:
                print(f"Ett oväntat fel uppstod: {e}. Försök igen.")


class CalculateTriangleFunctionMixin:
    '''Mixin-klass för att beräkna användarens poäng baserade på en triangelformad funktion.
    
    Denna metod beräknar ett totalt poängvärde baserat på antalet enheter
    användaren har angivit. Poängen ökar linjärt upp till ett visst antal
    enheter (enheter_för_maxpoäng). Efter detta maxvärde minskar poängen
    linjärt, vilket reflekterar en avtagande värde för ökade enheter.
    
    Ex: Om enheter = 1 ger värde 1, enheter = 2 ger värde 2 osv till enheter = 10 ger 10 poäng därefter minskar det i samma takt. dvs enheter = 11 ger 9 poäng, enheter = 12 ger 8 osv. I detta scenario är:
    enheter = x
    lokalt_maximum = 10
    poäng_vid_lokalt_maxiumum = 10
    tröskel = 20
    
    Notera: 
        - 'enheter': Kordinat i funktionen (ges via input).
        - 'lokalt_maximum': Bestämmer vid vilken kordinat som ger användaren maximalt
           värde till poäng (värdet på y), den högsta punkten i y led - efter lokalt_maximum sker en linjär minskning.
        - 'poäng_vid_lokalt_maximum': Avser poäng för kordinaten lokalt_maximum.
        - 'tröskel': Definierar korsningspunkt där kordinsten nu ger negativt värde till poäng. 
        '''
    @print_and_update_score
    def calculate_with_triangle_function(self, enheter: int, lokalt_maximum: int, poäng_vid_lokalt_maximum: int, tröskel: int) -> float:
        if 0 <= enheter < lokalt_maximum:
            return poäng_vid_lokalt_maximum / lokalt_maximum * enheter
        else:
            enheter_över_max = max(enheter - lokalt_maximum, 0)
            return poäng_vid_lokalt_maximum - ((poäng_vid_lokalt_maximum) / (tröskel - lokalt_maximum) * enheter_över_max)


class CalculateDeclineMixin:
    '''Styckvis linjär funktion, Mixin-klass för att beräkna poäng baserade på varje antal av enheter.
    
    Värdet för varje antal av enheter ger samma poäng upp till en gräns och därefter minskar.
    Ex: Alla enheter upp till 10 ger 1 poäng därefter minskar värdet för varje extra enhet efter tröskel, dvs att om enheter = 20, ger de första 10 enheterna 10 poäng totalt därefter minskar antalet poäng som ges för alla enheter efter tröskeln med en viss avkligningsfaktor.
    
    Notera:
        'enheter': Antalet av någonting, ex antal set, ges via input.
        'baspoäng': Bas värdet för vad varje enhet av enheter har för värde (poäng) - platå.
        'tröskel': Tröskeln där platåvärdet för 'baspoäng' börjar minska i värde för varje enhet av enheter    efter att enheter nått tröskelkordinaten.
        'avklingningsfaktor': Ger variabel för beräkning av det minskande värdet på baspoäng som ges per enhet efter 'tröskel'.
    '''
    @print_and_update_score
    def calculate_with_decline(self, enheter: int, tröskel: int, baspoäng: int, avklingningsfaktor: float) -> float:
        if enheter <= tröskel:
            return enheter * baspoäng
        else:
            total_poäng = tröskel * baspoäng
            enheter_över_tröskel = enheter - tröskel	
            for i in range(enheter_över_tröskel):
                total_poäng += baspoäng * (avklingningsfaktor ** (i + 1))
            return total_poäng

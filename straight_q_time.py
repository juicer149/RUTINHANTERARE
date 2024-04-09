from mixins import GetUnitsInputMixin, GetInputMixin, CalculateDeclineMixin

class Activities(GetUnitsInputMixin, CalculateDeclineMixin):
    """Klass för att hantera binära frågor om aktiviteter men också tid spenderad på aktiviteten.
    
    PARAMS: Värden för att hantera beräkningen i calculate_with_decline.
    PROMPT: Lista som gås igenom genom en for loop för att tilldela olika varibaler:
    1: nyckel till PARAMS och aktiviteten i fråga.
    2: prompt för korrekt svar av Ja/Nej fråga för aktivitet.
    3: prompt för att fråga om tid lagd på aktiviteten. 
    4: korrekt svar för poäng. 
    5: svar vid icke korrekt svar.
    GODKÄNDA_SVAR: Lista med svarsalternativen ja/nej för att hantera binär frågeställning.
     """
    def __init__(self, amor_fati):
        self.amor_fati = amor_fati
        self.total_poäng = 0 #används inte i nuläget
        self.PARAMS = {
                'meditation': (20, 1.5, 0.9),
                'kodning': (90, 1, 0),
                'läsning': (60, 0.8, 0.5)
                }

        self.PROMPT = [
            ('meditation', '\nHar du mediterat?', 'Hur många minuter mediterade du?', 'Hakuna matata, kanske nu?'),
            ('kodning', '\nHar du kodat?', 'Hur många minuter kodade du?', 'Ajdå, glöm inte att kontinuitet är nyckeln!'),
            ('läsning', '\nHar du läst någonting idag?', 'Hur många minuter läste du?', 'Inte hela värden, hoppas du gjorde andra produktiva sysslor istället!')
            # Lägg till fler frågor här...
        ]
        
        self.GODKÄNDA_SVAR = ['ja', 'nej']
        
        super().__init__()
        
    def handle_questions(self):
        #går igenom alla frågor i PROMPT
        for nyckel, fråga, fråga_två, nej_svar, in self.PROMPT:
            #hämtar svar om aktiviteten utförts
            svar = self.get_input(fråga, self.GODKÄNDA_SVAR).lower().replace('.','')
            if svar in self.GODKÄNDA_SVAR[0]: # [0] = 'ja'
                #hämtar tid gjord av aktiviteten och beräknar poäng
                tid = self.get_units(fråga_två)
                tröskel, baspoäng, avklingningsfaktor = self.PARAMS.get(nyckel, (0, 0, 0))
                score = self.calculate_with_decline(tid, tröskel, baspoäng, avklingningsfaktor)
                print(f"{tid}-minuter av {nyckel} gav dig: {score}-poäng.")
                self.total_poäng += score

            #om aktiviteten inte utförts.
            else:
                print(f"{nej_svar}")
        #retunerar totalt antal poäng tjänade för hela for-loopen, används inte i nuläget.
        return self.total_poäng

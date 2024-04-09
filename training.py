from mixins import GetInputMixin, GetUnitsInputMixin, CalculateDeclineMixin

class TrainingHandler(GetUnitsInputMixin, CalculateDeclineMixin):	
    """En klass som frågar kring om användaren har tränat och vilka former av träning.
    
    Attributer:
        TRÄNING_PARAMS = Dict. med variabler/parametrar, kopplad till olika träningsaktiviteter, för beräkning med BeräkningAvklingningMixin (tröskel, baspoäng, avklingningsfaktor).
        TRÄNINGS_METOD_DICT = Dict. med listor kopplad till nycklar (träningsformer) och dess underkategorier (träningsmetod).
    """
    def __init__(self, amor_fati):
        self.amor_fati = amor_fati
        
        self.TRÄNING_PARAMS = {	#träningsvärden BEHÖVER UPPDATERAS och STANDARDISERAS
            'hypotrofi': (6, 2.0, 0.9),
            'maxstyrka': (6, 2.0, 0.9),
            'funktionell': (10, 3.5, 0.8),
            'kroppsvikt': (10, 3.5, 0.8),
            'explosivitet': (8, 2.5, 0.9),
            'stretching': (15, 1, 0.9),
            'ytterläge': (10, 2, 0.9),
            'kinstretch': (45, 1.5, 0.9),
            'klättring': (90, 1, 0.9),
            'bjj': (90, 1, 0.9),
            'racket': (120, 0.8, 0.9),
            'golf': (180, 0.3, 0.9),
            'yoga': (30, 0.5, 0.9),            
            'löpning': (30, 1, 0.95), # ev göra en specialare för kondition (UTVECKLING)
            # '': (), Lägg till fler aktiviteter med detaljer här...
            'run': (30, 1, 0.95),
        }
        
        self.TRÄNINGS_METOD_DICT = {
           'kondition': ('löpning', 'run', 'rodd', 'skierg', 'assault bike', 'cykel'),
           'styrka': ('hypotrofi', 'funktionell', 'kroppsvikt', 'maxstyrka', 'explosivitet', 'ytterläge'), 
           'mobilitet': ('stretching', 'kinstretch'),	
           'aktivitet': ('klättring', 'bjj', 'racket', 'golf', 'yoga')
           }
        
        super().__init__()

    def calculate(self, aktivitet: str, enheter: str) -> float:
        '''Beräknar poäng genom BeräkningAvklingningMixin med argument från användarens input om en eller flera träningsformer.'''
        tröskel, baspoäng, avklingningsfaktor = self.TRÄNING_PARAMS.get(aktivitet, (0, 0, 0))
        return self.calculate_with_decline(enheter, tröskel, baspoäng, avklingningsfaktor)

    def handle_training(self):
        """Frågar användaren om form av träning -> gren av träning -> antal set eller tid av träning -> beräknar poäng beroende på val."""
        while True:
            godkända_svar = self.TRÄNINGS_METOD_DICT.keys()
            träningsval = self.get_input('Vilken form av träning', godkända_svar)
#Behöver lägga in ett alternativ för avbryt som tar en tillbaka om man svarar fel.
            while True:
                specifik_träning = self.get_input(f"Vilken typ av {träningsval}?", godkända_svar=self.TRÄNINGS_METOD_DICT[träningsval])
                måttenhet = "set" if träningsval == "styrka" else "minuter"
                
                while True:
                    try:
                        enheter = self.get_units(f"Hur många {måttenhet} utförde du för {specifik_träning}?: ")
                        score = self.calculate(specifik_träning, enheter)
                        print(f"\n{enheter}-{måttenhet} av {specifik_träning} gav dig: {score}-poäng.")
                        break                  
                    except ValueError:
                        print(f"Ange konkreta siffror.")

                mer_träning_samma_metod = self.get_input(f"Gjorde du någon mer {träningsval}?: ", godkända_svar=['ja', 'nej'])
                if mer_träning_samma_metod == 'nej':
                    break
                    
            annan_form_av_träning = self.get_input(f"Körde du någon annan form av träning", godkända_svar=['ja', 'nej'])
            if annan_form_av_träning == 'nej':
                break

    def run(self):
        """Startar programmet och hanterar användarflödet från början till slut i träning."""
        har_tränat = self.get_input(f"\nHar du tränat idag", godkända_svar=['ja', 'nej'])
        if har_tränat == 'ja':
            self.handle_training()
        else:
            print("Du kanske hade en vilodag, man kan fortfarande ta en promenad!")

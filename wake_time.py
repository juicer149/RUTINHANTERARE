from mixins import GetInputMixin, GetUnitsInputMixin, CalculateTriangleFunctionMixin

class WakeTime(GetUnitsInputMixin, CalculateTriangleFunctionMixin):
    """Klass för att beräkna poäng beroende på vilken tid användaren har gått upp.
    
    Klassen ärver funktioner från BeräkningTriangelFunktionMixin för att lägga till värde till amor_fati samt ärver HämtaEnheterMixin för att hämta input.
    
    Attributes:
        amor_fati: Föräldraklass som adderar värde och håller totalt värde.
        PROMPT_DICT (dict): Ordbok för prompts till vakna_input(), innehåller:
            'fråga': Textsträng för inputprompt till mixin hämta_input.
            'felsvar': Meddelande vid ValueError.
            'felsvar_2': Meddelande vid ogiltlig tid.
        VAKNA_TID_PARAMS (dict): Parametrar till BeräkningTriangelFunktionMixin, innehåller:
            'max poäng': Den högsta poäng som kan uppnås.
            'tid för maxpoäng': Tid (i minuter) som ger maximal poäng.
            'tid för 0 värde': Tid (i minuter) efter vilken poängen blir 0.
    """
    def __init__(self, amor_fati):
        self.amor_fati = amor_fati
        self.fråga = "När vaknade du; XX:XX : "
        self.felsvar = 'Ange en giltig tid 00:00 - 23:59'
        self.max = 2359
        self.format = 60
        
        self.VAKNA_TID_PARAMS = {
            'max poäng': 100,
            'tid för maxpoäng': 600,
            'tid för 0 värde': 1030,
        }
        super().__init__()
        
    def wake_up(self) -> float:
        """Hämtar enheter dör beräkning genom variabler från __init__ till HämtaEnheterMixin, sedan beräknar poäng för svar från input med parametrar från VAKNA_TID_PARAMS till BeräkningTriangelFunktionMixin"""
        enheter = self.get_units(self.fråga, prompt=self.felsvar, kontroll_max=self.max, format=self.format)
        if enheter is None:  # Användaren har valt att avbryta vilket retunerar None.
            print("Inmatning avbruten. Ingen poäng tilldelas.")
            return 0  # Avslutar metoden tidigt eftersom inget giltigt värde erhölls.
        lokalt_maximum = self.VAKNA_TID_PARAMS['tid för maxpoäng']
        poäng_vid_lokalt_maximum = self.VAKNA_TID_PARAMS['max poäng']
        tröskel = self.VAKNA_TID_PARAMS['tid för 0 värde']
        return self.calculate_with_triangle_function(enheter, lokalt_maximum, poäng_vid_lokalt_maximum, tröskel)

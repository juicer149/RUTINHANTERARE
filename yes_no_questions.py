from decorators import print_and_update_score
from mixins import GetInputMixin, GetUnitsInputMixin

# ev implementera logik för att hämta tid för de frågor som det är relevanta för och använda samma beräkning som används för träning baserat på tid. vidare skulle man då kunna dela upp alla dessa i egna moduler och olika värden som i träning för, längd elelr antal, enheter.

class YesNoQuestions(GetInputMixin):
    """Klass för att hantera olika binära (ja/nej) frågor för aktiviter som antingen ger poäng eller inte.
    
    Klassen använde en for loop för att tilldela olika värden för olika aktiviteter och olika varibaler till HämtaInputMixin för att ställa olika frågor för den specifika aktiviteten.
    """
    def __init__(self, amor_fati):
        self.amor_fati = amor_fati
        #fråga - korrekt_binär - felaktigt_bibnär
        self.PROMPT = [
            ('Har du bastat idag?', 'ja', 'Imorgon kanske!', 20),
            ('Har du kallbadat eller kallt duschat idag?', 'ja', "Bättre lycka imorgon, eller varför inte göra det nu?", 30,),
            ('Har du städat idag?', 'ja', "Bättre lycka imorgon, eller varför inte göra det nu?", 10),
            ('Har du druckit?', 'ja', 'Bra val!', -30),
            ('Har du rökt?', 'ja', 'Bra val!', -15),
            # Lägg till fler frågor här...
        ]

        self.godkända_svar = ['ja', 'nej']
        
    @print_and_update_score
    def handle_questions(self):
        total_poäng = 0 
        for fråga, korrekt_svar, prompt, poäng in self.PROMPT:
            print(f"\n\tVärde: {poäng}")
            svar = self.get_input(fråga, self.godkända_svar)
            if svar == korrekt_svar:
                total_poäng += poäng
            else:
                print(f"{prompt}")
        return total_poäng

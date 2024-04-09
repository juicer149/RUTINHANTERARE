from decorators import print_and_update_score
from mixins import GetInputMixin, GetUnitsInputMixin

# ev implementera logik för att hämta tid för de frågor som det är relevanta för och använda samma beräkning som används för träning baserat på tid. vidare skulle man då kunna dela upp alla dessa i egna moduler och olika värden som i träning för, längd elelr antal, enheter.

class YesNoQuestions(GetInputMixin):
    """Klass för att hantera olika binära (ja/nej) frågor för aktiviter som antingen ger poäng eller inte.
    
    Klassen använde en for loop för att tilldela olika värden för olika aktiviteter och olika varibaler till HämtaInputMixin för att ställa olika frågor för den specifika aktiviteten.
    """
    def __init__(self, amor_fati):
        self.amor_fati = amor_fati # behöver jag ens dessa då jag har min dekoratör som lägger till värdet redan?
        #fråga - korrekt_binär - felaktigt_bibnär
        """
        skulle möjligtvis kunna skapa en dict med flera olika svar för korrekt svar eller fel svar
        och sedan använda random för att välja svar, eller beroende på längd utförd i andra delar i programmet
        genera specifika svar beroende på hur länge det utfördes"""
        self.PROMPT = [
            ('Har du bastat idag?', 'ja', 'Svettigt, bra gjort!', 'Imorgon kanske!', 20),
            ('Har du kallbadat eller kallduschat idag?', 'ja', 'Wim Hof ger dig en high five, bra jobbat!', "Bättre lycka imorgon, eller varför inte göra det nu?", 30,),
            ('Har du städat idag?', 'ja', 'Ansvarig grabb hör jag!', "Bättre lycka imorgon, eller varför inte göra det nu?", 10),
            ('Har du druckit?', 'nej', 'Bra val!', 'Hoppas du hade kul!', -30),
            ('Har du rökt?', 'nej', 'Bra val!', 'Hoppas det åtminstonne var rätt röka, gör det inte till en vana', -15),
            # Lägg till fler frågor här...
        ]

        self.godkända_svar = ['ja', 'nej']
        
    @print_and_update_score
    def handle_questions(self):
        total_poäng = 0 #används inte eftersom dekoratören gör detta
        for fråga, korrekt_svar, prompt_korrekt, prompt_fel, poäng in self.PROMPT:
            print(f"\n\tVärde: {poäng}")
            svar = self.get_input(fråga, self.godkända_svar)
            if svar == korrekt_svar:
                print(f"{prompt_korrekt}")
                total_poäng += poäng
            else:
                print(f"{prompt_fel}")
        return total_poäng

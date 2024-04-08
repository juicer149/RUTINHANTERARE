class AmorFati:
    def __init__(self, amor_fati_xp=0): 
        """Håller reda på användarens poäng. Ökar med poäng från olika aktiviteter."""
        self.amor_fati_xp = amor_fati_xp 
        
    def __str__(self):
        """Retunerar en sträng av instansen när den kallas på."""
        return f"{self.amor_fati_xp}"
        
    def lägg_till_poäng(self, total_poäng: float):
        """Lägger till värde för instansen."""
        self.amor_fati_xp += total_poäng
    
    def hämta_poäng(self):
        # Används inte i programmet per se, men möjligen i en framtida redigering.
        return self.amor_fati_xp

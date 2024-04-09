import amor_fati

from typing import Callable
def print_and_update_score(dekorera_funktion: Callable[..., float]) -> Callable[..., float]:
    '''Dekoratör för att uppdatera och visa användarens poäng (amor_fati_xp).
    
    Den här dekoratören tar en funktion som argument, kör funktionen som dekorerats,
    avrundar dess resultat till två decimaler, lägger till resultatet
    till användarens totala poäng (amor_fati_xp), skriver ut poäng för det specifika valet
    och sedan det det uppdaterade totala värdet.
    
    Args:
    dekorera_funktion: Den funktion som dekoratören appliceras på.
    
    Returns:
    En wrapper funktion som omsluter och modifierar beteendet för
    dekorera_funktion.'''
    def wrapper(instans, *args, **kwargs) -> float:
        resultat = dekorera_funktion(instans, *args, **kwargs)
        avrundat_resultat = round(resultat, 2)
        instans.amor_fati.lägg_till_poäng(avrundat_resultat)
        #print(f"\n\tDetta gav dig: {avrundat_resultat} poäng.")
        print(f"\tDitt nya totala värde: {instans.amor_fati}")
        return avrundat_resultat
    return wrapper

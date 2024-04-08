from amor_fati import AmorFati
from training import TrainingHandler
from wake_time import WakeTime
from yes_no_questions import YesNoQuestions
from straight_q_time import Activities

class DailyRoutineHandler(AmorFati, WakeTime, YesNoQuestions, TrainingHandler, Activities):
    def __init__(self):
        self.amor_fati = AmorFati()
        self.wake_time = WakeTime(self.amor_fati)
        self.yes_no_questions = YesNoQuestions(self.amor_fati)
        self.training_handler = TrainingHandler(self.amor_fati)
        self.yes_no_time_score = Activities(self.amor_fati)

    def run_program(self):
        print("Välkommen till din daglig rutin hanterare!")
        
        # Frgar om tid för uppstigning och ger poäng därefter
        wake_time = self.wake_time.wake_up()
#        vakna_poäng = self.vakna_tid.beräkna_poäng(vakna_tid)
        
        # Ställer binära frågor och ger poäng därefter
        yes_no_score = self.yes_no_questions.handle_questions()
        
        yes_no_time_score = self.yes_no_time_score.handle_questions()
        
        # Frågar efter träning och ger poäng därefter
        self.training_handler.run()
        
        # Total poäng av de olika frågorna 
        print(f"Totala poäng för idag: {self.amor_fati}")


# Kör programmet
if __name__ == '__main__':
    program = DailyRoutineHandler()
    program.run_program()

import ipywidgets as widgets
from IPython.display import display, clear_output
import random

# --- Game State ---
secret_number = random.randint(1, 100)
attempts = 0

# --- UI Components ---
title = widgets.HTML("<h1 style='color: #6200ee; font-family: sans-serif;'>Number Guessing Game</h1>")
instructions = widgets.HTML("<p>I'm thinking of a number between <b>1 and 100</b>. Can you guess it?</p>")

guess_input = widgets.IntText(value=50, description='Your Guess:', layout=widgets.Layout(width='200px'))
guess_button = widgets.Button(description='Submit Guess', button_style='primary', layout=widgets.Layout(width='150px'))
reset_button = widgets.Button(description='New Game', button_style='warning', layout=widgets.Layout(width='150px'))

feedback_area = widgets.Output()

def check_guess(b):
    global attempts
    attempts += 1
    user_guess = guess_input.value
    
    with feedback_area:
        clear_output()
        if user_guess < secret_number:
            display(widgets.HTML(f"<div style='background-color: #e3f2fd; padding: 10px; border-left: 5px solid #2196f3;'><b>Too Low!</b> Try a higher number. (Attempts: {attempts})</div>"))
        elif user_guess > secret_number:
            display(widgets.HTML(f"<div style='background-color: #fff3e0; padding: 10px; border-left: 5px solid #ff9800;'><b>Too High!</b> Try a lower number. (Attempts: {attempts})</div>"))
        else:
            display(widgets.HTML(f"""
                <div style='background-color: #e8f5e9; padding: 20px; border: 2px solid #4caf50; border-radius: 10px;'>
                    <h2 style='color: #2e7d32;'>🎉 Correct!</h2>
                    <p>The number was <b>{secret_number}</b>. It took you <b>{attempts}</b> tries.</p>
                </div>
            """))

def reset_game(b):
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0
    with feedback_area:
        clear_output()
        display(widgets.HTML("<p style='color: #666;'>Game reset! Start guessing...</p>"))

guess_button.on_click(check_guess)
reset_button.on_click(reset_game)

# --- Layout ---
controls = widgets.VBox([
    title, 
    instructions, 
    widgets.HBox([guess_input, guess_button]), 
    reset_button,
    feedback_area
], layout=widgets.Layout(padding='20px', border='2px solid #6200ee', border_radius='15px', width='450px', background_color='#fafafa'))

display(controls)

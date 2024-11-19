import tkinter as tk
from tkinter import messagebox

votes = {"A": 0, "B": 0, "C": 0}

def vote(candidate):
    votes[candidate] += 1
    update_display()
    messagebox.showinfo("Vote Submitted", f"You voted for Candidate {candidate}!")

def update_display():
    candidate_a_label.config(text=f"Candidate A: {votes['A']} votes ({calculate_percentage('A')}%)")
    candidate_b_label.config(text=f"Candidate B: {votes['B']} votes ({calculate_percentage('B')}%)")
    candidate_c_label.config(text=f"Candidate C: {votes['C']} votes ({calculate_percentage('C')}%)")
    determine_winner()

def calculate_percentage(candidate):
    total_votes = sum(votes.values())
    if total_votes == 0:
        return 0
    return round((votes[candidate] / total_votes) * 100, 2)

def determine_winner():
    max_votes = max(votes.values())
    winners = [candidate for candidate, count in votes.items() if count == max_votes]
    if len(winners) == 1:
        winner_label.config(text=f"Winner: Candidate {winners[0]}")
    else:
        winner_label.config(text="Winner: It's a tie!")

app = tk.Tk()
app.title("Student E-Voting System")
app.geometry("400x400")

heading_label = tk.Label(app, text="Student E-Voting System", font=("Arial", 16))
heading_label.pack(pady=10)

vote_a_button = tk.Button(app, text="Vote for Candidate A", command=lambda: vote("A"), bg="lightblue", font=("Arial", 12))
vote_a_button.pack(pady=5)

vote_b_button = tk.Button(app, text="Vote for Candidate B", command=lambda: vote("B"), bg="lightgreen", font=("Arial", 12))
vote_b_button.pack(pady=5)

vote_c_button = tk.Button(app, text="Vote for Candidate C", command=lambda: vote("C"), bg="lightcoral", font=("Arial", 12))
vote_c_button.pack(pady=5)

candidate_a_label = tk.Label(app, text="Candidate A: 0 votes (0%)", font=("Arial", 12))
candidate_a_label.pack()

candidate_b_label = tk.Label(app, text="Candidate B: 0 votes (0%)", font=("Arial", 12))
candidate_b_label.pack()

candidate_c_label = tk.Label(app, text="Candidate C: 0 votes (0%)", font=("Arial", 12))
candidate_c_label.pack()

winner_label = tk.Label(app, text="Winner: None", font=("Arial", 14), fg="darkred")
winner_label.pack(pady=10)

app.mainloop()

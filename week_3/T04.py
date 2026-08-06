import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


def run_quantum_coin_game(classical_player_flips: bool):
    qc_game = QuantumCircuit(1, 1)

    # Move 1: Quantum Player applies Hadamard gate (Puts coin in superposition)
    qc_game.h(0)

    # Move 2: Classical Player chooses to FLIP (X gate) or PASS (Identity)
    if classical_player_flips:
        qc_game.x(0)  # Classical flip
    else:
        qc_game.id(0)  # Classical pass

    # Move 3: Quantum Player applies Hadamard gate again
    qc_game.h(0)

    # Measurement (0 = Quantum Player Wins, 1 = Classical Player Wins)
    qc_game.measure(0, 0)

    simulator = AerSimulator()
    counts = simulator.run(qc_game, shots=1000).result().get_counts()
    return counts


print("--- Real-World Exercise: Quantum Coin-Flip Game ---")

# Scenario A: Classical player decides to FLIP the coin
counts_flip = run_quantum_coin_game(classical_player_flips=True)
win_prob_flip = (counts_flip.get("0", 0) / 1000) * 100

# Scenario B: Classical player decides NOT to flip the coin
counts_pass = run_quantum_coin_game(classical_player_flips=False)
win_prob_pass = (counts_pass.get("0", 0) / 1000) * 100

print(
    f"Quantum Win Probability when Classical Player FLIPS:  {win_prob_flip:.1f}%"
)
print(
    f"Quantum Win Probability when Classical Player PASSES: {win_prob_pass:.1f}%"
)

# -------------------------------------------------------------
# Visualization: Plotting Win Probabilities Graph
# -------------------------------------------------------------
scenarios = [
    "Classical Player\nFlips (X Gate)",
    "Classical Player\nPasses (Identity)",
]
win_rates = [win_prob_flip, win_prob_pass]

plt.figure(figsize=(7, 5))
bars = plt.bar(
    scenarios, win_rates, color=["mediumpurple", "teal"], width=0.4, alpha=0.85
)

plt.axhline(
    50,
    color="crimson",
    linestyle="--",
    linewidth=1.5,
    label="Classical Fair Odds (50%)",
)
plt.ylabel("Quantum Player Win Rate (%)")
plt.title("Quantum Advantage: Meyer's Quantum Penny Flip Game")
plt.ylim(0, 115)

# Add percentage labels above each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2.0,
        yval + 3,
        f"{yval:.1f}%",
        ha="center",
        va="bottom",
        fontweight="bold",
    )

plt.legend(loc="upper right")
plt.tight_layout()
plt.show()
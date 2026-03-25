"""
sa_timetable.py  -  Simulated Annealing: Exam Timetable Scheduling
===================================================================
This program is COMPLETE and works as-is. DO NOT rewrite it.
"""

import random
import math
import matplotlib.pyplot as plt
import os

# =============================================================================
# PROBLEM DATA
# =============================================================================

EXAMS = [
    "Mathematics","Physics","Chemistry","English","History",
    "Computer Science","Economics","Biology","Statistics","Geography",
]

NUM_EXAMS = len(EXAMS)
NUM_SLOTS = 5

STUDENTS = [
    [0,1,5],[0,2,6],[1,3,7],[2,4,8],[3,5,9],
    [0,4,7],[1,6,8],[2,5,9],[3,6,0],[4,7,1],
    [5,8,2],[6,9,3],[7,0,4],[8,1,5],[9,2,6],
    [0,3,8],[1,4,9],[2,7,5],[3,8,6],[4,9,7],
    [0,5,2],[1,6,3],[2,7,4],[3,8,0],[4,9,1],
    [5,0,6],[6,1,7],[7,2,8],[8,3,9],[9,4,0],
]

# =============================================================================
# OBJECTIVE FUNCTION
# =============================================================================

def count_clashes(timetable):
    clashes = 0
    for student_exams in STUDENTS:
        seen_slots = set()
        for exam in student_exams:
            slot = timetable[exam]
            if slot in seen_slots:
                clashes += 1
            seen_slots.add(slot)
    return clashes

# =============================================================================
# NEIGHBOUR FUNCTION
# =============================================================================

def generate_neighbor(timetable):
    new_tt = timetable[:]
    exam = random.randint(0, NUM_EXAMS - 1)
    current_slot = timetable[exam]
    new_slot = random.choice([s for s in range(NUM_SLOTS) if s != current_slot])
    new_tt[exam] = new_slot
    return new_tt

# =============================================================================
# SIMULATED ANNEALING
# =============================================================================

def run_sa(
    initial_temp=100.0,
    cooling_rate=0.995,
    min_temp=0.1,
    max_iterations=5000,
    seed=42,
):
    random.seed(seed)

    current = [random.randint(0, NUM_SLOTS - 1) for _ in range(NUM_EXAMS)]
    current_c = count_clashes(current)

    best = current[:]
    best_c = current_c

    T = initial_temp
    clash_log = []
    temp_log = []

    for _ in range(max_iterations):
        if T < min_temp:
            break

        neighbour = generate_neighbor(current)
        neighbour_c = count_clashes(neighbour)
        delta = neighbour_c - current_c

        if delta < 0 or random.random() < math.exp(-delta / T):
            current = neighbour
            current_c = neighbour_c

        if current_c < best_c:
            best = current[:]
            best_c = current_c

        clash_log.append(best_c)
        temp_log.append(T)

        T *= cooling_rate

        if best_c == 0:
            break

    return best, best_c, clash_log, temp_log

# =============================================================================
# OUTPUT HELPERS
# =============================================================================

def print_timetable(timetable):
    print("\n  Final Timetable")
    print("-" * 42)
    for slot in range(NUM_SLOTS):
        in_slot = [EXAMS[i] for i in range(NUM_EXAMS) if timetable[i] == slot]
        print(f"  Slot {slot+1}:  {', '.join(in_slot) if in_slot else '(empty)'}")
    print("-" * 42)
    print(f"  Total clashes : {count_clashes(timetable)}\n")

def save_plot(clash_log, temp_log, filename, title):
    os.makedirs("plots", exist_ok=True)
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 6), sharex=True)

    ax1.plot(clash_log, color="crimson", linewidth=1.5)
    ax1.set_ylabel("Best Clashes")
    ax1.set_title(f"SA Convergence - {title}")
    ax1.grid(True, alpha=0.3)

    ax2.plot(temp_log, color="steelblue", linewidth=1.5)
    ax2.set_ylabel("Temperature")
    ax2.set_xlabel("Iteration")
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(filename, dpi=150)
    plt.close()
    print(f"  Saved -> {filename}")

# =============================================================================
# RUN EXPERIMENTS
# =============================================================================

if __name__ == "__main__":

    # EXPERIMENT 1
    print("=" * 48)
    print("  EXPERIMENT 1 - Baseline")
    print("=" * 48)

    tt, clashes, clash_log, temp_log = run_sa(
        initial_temp=100.0, cooling_rate=0.995,
        min_temp=0.1, max_iterations=5000, seed=42
    )

    print_timetable(tt)
    print(f"  Iterations     : {len(clash_log)}")
    print(f"  Start clashes  : {clash_log[0]}")
    print(f"  Final clashes  : {clashes}")

    save_plot(clash_log, temp_log,
              "plots/experiment_1.png", "Baseline cooling_rate=0.995")

    # EXPERIMENT 2

    tt2, clashes2, cl2, tl2 = run_sa(
        initial_temp=100.0, cooling_rate=0.80,
        min_temp=0.1, max_iterations=5000, seed=42
    )
    print_timetable(tt2)
    print(f"  Final clashes : {clashes2}")
    save_plot(cl2, tl2, "plots/experiment_2a.png", "cooling_rate=0.80")

    tt2, clashes2, cl2, tl2 = run_sa(
        initial_temp=100.0, cooling_rate=0.95,
        min_temp=0.1, max_iterations=5000, seed=42
    )
    print_timetable(tt2)
    print(f"  Final clashes : {clashes2}")
    save_plot(cl2, tl2, "plots/experiment_2b.png", "cooling_rate=0.95")

    tt2, clashes2, cl2, tl2 = run_sa(
        initial_temp=100.0, cooling_rate=0.995,
        min_temp=0.1, max_iterations=5000, seed=42
    )
    print_timetable(tt2)
    print(f"  Final clashes : {clashes2}")
    save_plot(cl2, tl2, "plots/experiment_2c.png", "cooling_rate=0.995")
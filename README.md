# Assignment 1 — Simulated Annealing: Exam Timetable Scheduling
## Observation Report

**Student Name  :** E Vamshi
**Student ID    :** 2310040098  
**Date Submitted:** 26/03/2026  

---

## How to Submit

1. Run each experiment following the instructions below
2. Fill in every answer box — do not leave placeholders
3. Make sure the `plots/` folder contains all required images
4. Commit this README and the `plots/` folder to your GitHub repo

---

## Before You Begin — Read the Code

Open `sa_timetable.py` and read through it. Then answer these questions.

**Q1. What does `count_clashes()` measure? What value means a perfect timetable?**

```
`count_clashes()` measures the total number of conflicting exam slots across all students. A clash occurs when a single student has two exams assigned to the same time slot, and a value of 0 means a perfect timetable with no clashes.
```

**Q2. What does `generate_neighbor()` do? How is the new timetable different from the current one?**

```
`generate_neighbor()` creates a neighbouring timetable by randomly selecting one exam and moving it to a newly generated random time slot. The new timetable is identical to the current one in all aspects except for the randomly changed slot of that single exam.
```

**Q3. In `run_sa()`, there is this line:**
```python
if delta < 0 or random.random() < math.exp(-delta / T):
```
**What does this line decide? Why does SA sometimes accept a worse solution?**

```
This line decides whether to accept the new timetable as the current solution, accepting it automatically if it's better (`delta < 0`). SA sometimes probabilistically accepts a worse solution to allow the algorithm to escape local optima and explore a wider area of the solution space.
```

---

## Experiment 1 — Baseline Run

**Instructions:** Run the program without changing anything.
```bash
python sa_timetable.py
```

**Fill in this table:**

| Metric | Your result |
|--------|-------------|
| Number of iterations completed | 1379 |
| Clashes at iteration 1 | 12 |
| Final best clashes | 3 |
| Did SA reach 0 clashes? (Yes / No) | No |

**Copy the printed timetable output here:**
```
  Final Timetable
------------------------------------------
  Slot 1:  Geography
  Slot 2:  Chemistry, English
  Slot 3:  History, Computer Science, Economics
  Slot 4:  Biology, Statistics
  Slot 5:  Mathematics, Physics
------------------------------------------
  Total clashes : 3
```

**Look at `plots/experiment_1.png` and describe what you see (2–3 sentences).**  
*Where does the biggest drop in clashes happen? Does the curve flatten out?*
```
The biggest drop in clashes happens early on during the initial iterations when the temperature is high. As the temperature exponentially decays and the algorithm runs its course, the curve flattens out, indicating convergence towards a local optimum with fewer accepted worse solutions.
```

---

## Experiment 2 — Effect of Cooling Rate

**Instructions:** In `sa_timetable.py`, find the `# EXPERIMENT 2` block in `__main__`.  
Copy it three times and run with `cooling_rate` = **0.80**, **0.95**, and **0.995**.  
Save plots as `experiment_2a.png`, `experiment_2b.png`, `experiment_2c.png`.

**Results table:**

| cooling_rate | Final clashes | Iterations completed | Reached 0 clashes? |
|-------------|---------------|----------------------|--------------------|
| 0.80        | 8             | 31                   | No                 |
| 0.95        | 3             | 135                  | No                 |
| 0.995       | 3             | 1379                 | No                 |

**Compare the three plots. What do you notice about how fast vs slow cooling affects the result? (3–4 sentences)**  
*Hint: Fast cooling = temperature drops quickly. Does it have time to explore well?*
```
Fast cooling (e.g., 0.80) causes the temperature to drop precipitously, leaving the algorithm with very little time to thoroughly explore the search space, which results in a poor final solution. In contrast, slower cooling rates (0.95 and 0.995) allow for sufficient early-stage exploration and a gradual transition into exploiting the best solutions found. Consequently, slower cooling takes significantly more iterations but reliably yields a better final timetable with fewer clashes.
```

**Which cooling_rate gave the best result? Why do you think that is?**
```
Both 0.95 and 0.995 gave the best result of 3 final clashes. The cooling_rate of 0.995 performs best on average because its slow cooling provides the algorithm with the most time to escape local optima and fully explore the solution space before converging to a near-optimal solution.
```

---

## Summary

**Complete this table with your best result from each experiment:**

| Experiment | Key setting | Final clashes | Main finding in one sentence |
|------------|-------------|---------------|------------------------------|
| 1 — Baseline | cooling_rate = 0.995 | 3 | Slow cooling allows for deep exploration and near-optimal solutions, but takes more iterations. |
| 2 — Cooling rate | cooling_rate = 0.95 | 3 | A slightly faster cooling rate can achieve the same best result while computationally taking significantly fewer iterations. |

**In your own words — what is the most important thing you learned about Simulated Annealing from these experiments? (3–5 sentences)**
```
The most important thing I learned is how sensitive Simulated Annealing is to its hyperparameters, specifically the cooling rate. A cooling rate that is too fast leads to premature convergence in a suboptimal state since it inherently behaves similarly to a purely greedy search too early. Conversely, a suitably slow cooling rate strikes the right balance by allowing for enough initially random exploration to escape local minima to successfully find an optimal or near-optimal solution.
```

---

## Submission Checklist

- [x] Student name and ID filled in
- [x] Q1, Q2, Q3 answered
- [x] Experiment 1: table filled, timetable pasted, plot observation written
- [x] Experiment 2: results table filled (3 rows), observation and answer written
- [x] Summary table completed and reflection written
- [x] `plots/` contains: `experiment_1.png`, `experiment_2a.png`, `experiment_2b.png`, `experiment_2c.png`

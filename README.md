# AI Smart Traffic Signal Control System

A simple and practical Reinforcement Learning environment that simulates a 4-way traffic intersection.  
The goal is to control traffic signals intelligently to reduce congestion across all lanes.

---

## Problem Statement

Traffic congestion at intersections leads to wasted time, fuel, and increased pollution.

This project models a traffic junction where an agent decides which lane gets a green signal at each step, with the objective of minimizing the number of waiting vehicles.

---

## Environment Overview

          [North]
             |
[West] ── JUNCTION ── [East]
             |
          [South]

At every timestep:
- Cars arrive randomly in each lane
- One lane gets a green signal
- Cars in that lane pass through
- Other lanes continue to accumulate cars

---

## State Space

The environment state represents the number of cars waiting in each lane:

- North → cars in north lane
- South → cars in south lane
- East  → cars in east lane
- West  → cars in west lane

Example:
[10, 5, 3, 8]

---

## Action Space

The agent selects which lane gets the green signal:

- 0 → North
- 1 → South
- 2 → East
- 3 → West

Only one lane can be green at a time.

---

## Reward Function

reward = -sum(queue) - max(queue)

- Penalizes total congestion  
- Extra penalty for long queues  
- Encourages balanced traffic flow  

---

## Tasks (Difficulty Levels)

- Easy   → Low traffic, easier to control  
- Medium → Moderate traffic, congestion starts building  
- Hard   → Heavy traffic, very challenging  

---

## How It Works

At each timestep:
1. Cars arrive randomly in all lanes  
2. Agent selects a lane to turn green  
3. Cars from that lane pass  
4. Remaining cars accumulate  
5. Reward is calculated based on congestion  

---

## Baseline Agent

A simple greedy agent is used as a baseline:
- Always selects the lane with maximum cars  
- Performs better than random selection  
- Helps evaluate environment quality  

---

## Evaluation

The grader evaluates performance on all difficulty levels:

- Easy → performance in light traffic  
- Medium → performance in moderate traffic  
- Hard → performance under heavy congestion  
- Overall → average score (0.0 to 1.0)  

---

## Design Choices

- Gaussian-based traffic arrival for realism  
- Maximum car limit to prevent overflow  
- Multi-level difficulty for robustness testing  
- Reward function balances total and peak congestion  

These choices make the environment simple yet realistic.

---

## Why Reinforcement Learning?

Traffic control is a sequential decision-making problem where:
- Actions affect future states  
- Optimal strategy is not predefined  
- Adaptability is important  

Reinforcement Learning fits naturally for this type of problem.

---

## Real-World Impact

Traffic congestion is a major issue in urban areas.

This environment can be used to train AI systems that:
- Reduce waiting time  
- Improve traffic flow  
- Optimize signal control dynamically  

---

## How to Run

Run simulation:
python main.py

Run grader:
python grader.py

---

## Project Structure

traffic_env.py   → Environment logic  
tasks.py         → Difficulty settings  
grader.py        → Evaluation system  
main.py          → Simulation demo  
openenv.yaml     → Environment config  
Dockerfile       → Deployment setup  
README.md        → Documentation  

---

## Example

State:
[10, 5, 3, 8]

Action:
0 (North green)

Result:
- Cars from North move  
- Others accumulate  
- Reward reflects congestion  

---

## Personal Note

This project was built as part of a hackathon to explore how AI can help manage traffic better.

I focused on keeping the environment simple, clear, and realistic so it can be easily understood and extended.
# State Machine Engine

## Overview

State Machine Engine is a terminal-based Python application that simulates a Finite State Machine (FSM).

It allows users to create state machines, define states, configure transitions, move between valid states, and monitor the current state of each machine.

This project demonstrates one of the most common software design patterns used in backend systems, workflow engines, robotics, networking, and game development.

---

## Features

- Create State Machines
- Add States
- Define State Transitions
- Execute State Changes
- View Current State
- Delete State Machines
- View Statistics
- JSON Storage

---

## Project Structure

state-machine-engine/

├── state_engine.py

├── state_console.py

├── README.md

└── .gitignore

---

## Requirements

Python 3.x

No external libraries required.

---

## Run

python state_console.py

---

## Example Workflow

Create Machine

Order Processing

↓

Initial State

Pending

↓

Add States

Confirmed

Packed

Shipped

Delivered

↓

Add Transitions

Pending → Confirmed

Confirmed → Packed

Packed → Shipped

Shipped → Delivered

↓

Execute

Pending

↓

Confirmed

↓

Packed

↓

Shipped

↓

Delivered

---

## Example Output

========== STATE MACHINE ==========

Machine : Order Processing

Current State : Packed

States

- Pending

- Confirmed

-> Packed (Current)

- Shipped

- Delivered

Transitions

Pending --> Confirmed

Confirmed --> Packed

Packed --> Shipped

Shipped --> Delivered

---

## Generated File

states.json

Example

{
    "Order Processing": {
        "current": "Pending",
        "states": [
            "Pending",
            "Confirmed",
            "Packed",
            "Shipped",
            "Delivered"
        ],
        "transitions": {
            "Pending": "Confirmed",
            "Confirmed": "Packed",
            "Packed": "Shipped",
            "Shipped": "Delivered"
        }
    }
}

---

## Applications

- Order Processing
- Payment Processing
- User Authentication
- Ticket Workflow
- Manufacturing Pipeline
- Robotics
- Network Protocols
- Game Development
- Approval Systems

---

## Future Improvements

- Event-Based Transitions
- Multiple Transitions Per State
- Transition Conditions
- Rollback Support
- Transition History
- State Validation
- Graph Visualization
- Import / Export
- REST API
- Role-Based Permissions

---

## License

MIT License
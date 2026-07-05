import json
import os


class StateMachineEngine:

    def __init__(self):

        self.file_name = "states.json"

        self.machines = {}

        self.load()

    def load(self):

        if os.path.exists(self.file_name):

            try:

                with open(

                    self.file_name,

                    "r",

                    encoding="utf-8"

                ) as file:

                    self.machines = json.load(file)

            except:

                self.machines = {}

    def save(self):

        with open(

            self.file_name,

            "w",

            encoding="utf-8"

        ) as file:

            json.dump(

                self.machines,

                file,

                indent=4

            )

    def create_machine(self):

        print("\nCreate State Machine\n")

        name = input(

            "Machine Name: "

        ).strip()

        if name == "":

            print("\nInvalid Name")

            return

        if name in self.machines:

            print("\nMachine Already Exists")

            return

        initial = input(

            "Initial State: "

        ).strip()

        self.machines[name] = {

            "current": initial,

            "states": [

                initial

            ],

            "transitions": {}

        }

        self.save()

        print("\nState Machine Created.")

    def add_state(self):

        if not self.machines:

            print("\nNo Machines Found.")

            return

        machine = input(

            "\nMachine Name: "

        ).strip()

        if machine not in self.machines:

            print("\nMachine Not Found")

            return

        state = input(

            "New State: "

        ).strip()

        if state in self.machines[

            machine

        ][

            "states"

        ]:

            print("\nState Already Exists")

            return

        self.machines[

            machine

        ][

            "states"

        ].append(

            state

        )

        self.save()

        print("\nState Added.")

    def add_transition(self):

        if not self.machines:

            print("\nNo Machines Found.")

            return

        machine = input(

            "\nMachine Name: "

        ).strip()

        if machine not in self.machines:

            print("\nMachine Not Found")

            return

        source = input(

            "From State: "

        ).strip()

        target = input(

            "To State: "

        ).strip()

        if source not in self.machines[machine]["states"]:

            print("\nInvalid Source State")

            return

        if target not in self.machines[machine]["states"]:

            print("\nInvalid Target State")

            return

        self.machines[machine][

            "transitions"

        ][source] = target

        self.save()

        print("\nTransition Added.")

    def move_next(self):

        if not self.machines:

            print("\nNo Machines Found.")

            return

        machine = input(

            "\nMachine Name: "

        ).strip()

        if machine not in self.machines:

            print("\nMachine Not Found")

            return

        current = self.machines[machine]["current"]

        transitions = self.machines[machine]["transitions"]

        if current not in transitions:

            print("\nNo Transition Available")

            return

        next_state = transitions[current]

        self.machines[machine]["current"] = next_state

        self.save()

        print(

            f"\nMoved To '{next_state}'"

        )

    def show_machine(self):

        if not self.machines:

            print("\nNo Machines Found.")

            return

        machine = input(

            "\nMachine Name: "

        ).strip()

        if machine not in self.machines:

            print("\nMachine Not Found")

            return

        data = self.machines[machine]

        print("\n========== STATE MACHINE ==========\n")

        print(

            "Machine :",

            machine

        )

        print(

            "Current State :",

            data["current"]

        )

        print("\nStates")

        for state in data["states"]:

            if state == data["current"]:

                print(

                    "->",

                    state,

                    "(Current)"

                )

            else:

                print(

                    "-",

                    state

                )

        print("\nTransitions")

        if not data["transitions"]:

            print("None")

        else:

            for source, target in data["transitions"].items():

                print(

                    f"{source} --> {target}"

                )

    def delete_machine(self):

        if not self.machines:

            print("\nNo Machines Found.")

            return

        machine = input(

            "\nMachine Name: "

        ).strip()

        if machine not in self.machines:

            print("\nMachine Not Found")

            return

        del self.machines[machine]

        self.save()

        print("\nMachine Deleted.")

    def statistics(self):

        total = len(self.machines)

        states = 0

        transitions = 0

        for machine in self.machines.values():

            states += len(machine["states"])

            transitions += len(machine["transitions"])

        print("\n========== STATISTICS ==========\n")

        print("Machines     :", total)

        print("States       :", states)

        print("Transitions  :", transitions)
from state_engine import StateMachineEngine


class StateMachineConsole:

    def __init__(self):

        self.engine = StateMachineEngine()

    def menu(self):

        while True:

            print("\n")

            print("=" * 50)

            print("          STATE MACHINE ENGINE")

            print("=" * 50)

            print("1. Create State Machine")

            print("2. Add State")

            print("3. Add Transition")

            print("4. Move To Next State")

            print("5. View State Machine")

            print("6. Delete State Machine")

            print("7. Statistics")

            print("8. Exit")

            choice = input("\nEnter Choice: ")

            if choice == "1":

                self.engine.create_machine()

            elif choice == "2":

                self.engine.add_state()

            elif choice == "3":

                self.engine.add_transition()

            elif choice == "4":

                self.engine.move_next()

            elif choice == "5":

                self.engine.show_machine()

            elif choice == "6":

                self.engine.delete_machine()

            elif choice == "7":

                self.engine.statistics()

            elif choice == "8":

                print("\nExiting State Machine Engine...")

                break

            else:

                print("\nInvalid Choice.")


if __name__ == "__main__":

    console = StateMachineConsole()

    console.menu()
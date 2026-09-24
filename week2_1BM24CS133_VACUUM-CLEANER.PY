class VacuumWorld:
    def __init__(self):
        # Environment: dictionary with location states
        # True = dirty, False = clean
        self.environment = {
            "Left": True,   # Initially dirty
            "Right": True   # Initially dirty
        }
        self.agent_location = "Left"  # Start position

    def perceive(self):
        """Return whether the current location is dirty."""
        return self.environment[self.agent_location]

    def act(self):
        """Agent action based on perception."""
        if self.perceive():
            print(f"Agent at {self.agent_location}: Location is dirty -> CLEAN")
            self.environment[self.agent_location] = False
        else:
            # Move to the other location
            new_location = "Right" if self.agent_location == "Left" else "Left"
            print(f"Agent at {self.agent_location}: Location is clean -> MOVE to {new_location}")
            self.agent_location = new_location

    def run(self, steps=4):
        """Run the agent for a given number of steps."""
        for step in range(steps):
            print(f"\nStep {step + 1}:")
            self.act()
            print(f"Environment state: {self.environment}")


if __name__ == "__main__":
    # Create and run the vacuum world
    vacuum = VacuumWorld()
    vacuum.run(steps=6)
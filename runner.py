from agents.destination_agent import destination_agent
from agents.booking_agent import booking_agent
from agents.explore_agent import explore_agent

def main():
    print("✈️ Welcome to the Travel Experience Planner ✈️")
    mood = input("What is your travel mood or interest? (e.g., beach, adventure, culture): ")
    destination = destination_agent(mood)
    booking_agent(destination)
    explore_agent(destination)

if __name__ == "__main__":
    main()
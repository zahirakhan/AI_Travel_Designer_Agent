from tools.travel_tools import get_flights, suggest_hotels

def booking_agent(destination: str):
    """Simulates booking flights and hotels"""
    flights = get_flights(destination)
    hotels = suggest_hotels(destination)
    print(f"\n🛫 Booking Info for {destination}:\n{flights}\n{hotels}")

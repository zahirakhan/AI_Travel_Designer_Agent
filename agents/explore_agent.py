def explore_agent(destination: str):
    """Suggests attractions and food in the destination"""
    attractions = {
        "Maldives": ["Snorkeling", "Private Beaches", "Resort Spas"],
        "Nepal": ["Mount Everest", "Hiking Trails", "Temples"],
        "Kyoto": ["Shrines", "Tea Houses", "Geisha District"],
        "Paris": ["Eiffel Tower", "Louvre Museum", "French Cuisine"]
    }
    places = attractions.get(destination, ["Explore local sights!"])
    print(f"🗺️ Things to Explore in {destination}:")
    for item in places:
        print(f" - {item}")
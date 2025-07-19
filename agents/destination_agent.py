def destination_agent(mood: str) -> str:
    """Suggests destinations based on user mood"""
    options = {
        "beach": "Maldives",
        "adventure": "Nepal",
        "culture": "Kyoto"
    }
    destination = options.get(mood.lower(), "Paris")
    print(f"🌍 Suggested Destination: {destination}")
    return destination
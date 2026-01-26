from agent_logic import HealthAgent

a = HealthAgent()
print(a.parse_meal("Chicken Salad, 350, 30, 10"))
print(a.get_totals())
print(a.get_remaining())

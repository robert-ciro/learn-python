years = {2022, 2023, 2024}

print("2024 in years =", 2024 in years)  # true
print("2024 in years =", 2025 not in years)  # true
print("years == {2022, 2023, 2024} =", years == {2022, 2023, 2024})  # true
print("years != {2000, 2023, 2025}=", years != {2000, 2023, 2025})  # true
print("years == {2022, 2023, 2024} =", years is {2022, 2023, 2024})  # false
print("years == {2022, 2023, 2024} =", years is not {2022, 2023, 2024})  # true

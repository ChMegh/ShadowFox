# Task 3: List Operations

justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

print("Original Justice League:", justice_league)
print("Number of members:", len(justice_league))
print("--------------------------------------------------")

# Add Batgirl & Nightwing
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("After adding Batgirl & Nightwing:", justice_league)
print("--------------------------------------------------")

# Make Wonder Woman leader
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("After making Wonder Woman leader:", justice_league)
print("--------------------------------------------------")

# Separate Aquaman & Flash by adding Superman in between
flash_index = justice_league.index("Flash")
justice_league.insert(flash_index, "Superman")
print("After separating Flash & Aquaman:", justice_league)
print("--------------------------------------------------")

# Replace list with new members
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("New team:", justice_league)
print("--------------------------------------------------")

# Sort alphabetically and find new leader
justice_league.sort()
print("Sorted Team:", justice_league)
print("New Leader:", justice_league[0])

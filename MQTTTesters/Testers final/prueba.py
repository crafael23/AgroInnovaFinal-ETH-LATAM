# Define initial concentrations of reactants and products
oxaloacetate = 5
acetyl_coA = 1
citrate = 1
isocitrate = 1
alpha_ketoglutarate = 1
succinyl_coA = 1
succinate = 1
fumarate = 1
malate = 1
NADH = 6
FADH2 = 2
ATP = 2

# Define reaction rates
rate_citrate = 0.1
rate_isocitrate = 0.2
rate_alpha_ketoglutarate = 0.3
rate_succinyl_coA = 0.4
rate_succinate = 0.5
rate_fumarate = 0.6
rate_malate = 0.7
rate_NADH = 0.8
rate_FADH2 = 0.9
rate_ATP = 1.0

# Define time step and simulation duration
dt = 0.01
t_max = 10

# Simulate the Krebs cycle
for t in range(int(t_max / dt)):
    # Calculate reaction rates
    rate_citrate = rate_citrate * (1 - citrate)
    rate_isocitrate = rate_isocitrate * (1 - isocitrate)
    rate_alpha_ketoglutarate = rate_alpha_ketoglutarate * (1 - alpha_ketoglutarate)
    rate_succinyl_coA = rate_succinyl_coA * (1 - succinyl_coA)
    rate_succinate = rate_succinate * (1 - succinate)
    rate_fumarate = rate_fumarate * (1 - fumarate)
    rate_malate = rate_malate * (1 - malate)
    rate_NADH = rate_NADH * (1 - NADH)
    rate_FADH2 = rate_FADH2 * (1 - FADH2)
    rate_ATP = rate_ATP * (1 - ATP)

    # Update concentrations of reactants and products
    citrate += (
        rate_citrate * oxaloacetate * acetyl_coA - rate_isocitrate * citrate
    ) * dt
    isocitrate += (
        rate_isocitrate * citrate - rate_alpha_ketoglutarate * isocitrate
    ) * dt
    alpha_ketoglutarate += (
        rate_alpha_ketoglutarate * isocitrate - rate_succinyl_coA * alpha_ketoglutarate
    ) * dt
    succinyl_coA += (
        rate_succinyl_coA * alpha_ketoglutarate - rate_succinate * succinyl_coA
    ) * dt
    succinate += (rate_succinate * succinyl_coA - rate_fumarate * succinate) * dt
    fumarate += (rate_fumarate * succinate - rate_malate * fumarate) * dt
    malate += (
        rate_malate * fumarate
        - rate_citrate * malate * NADH
        + rate_NADH * oxaloacetate * malate
        - rate_FADH2 * malate
    ) * dt
    NADH += (rate_citrate * malate * NADH - rate_NADH * oxaloacetate * malate) * dt
    FADH2 += (rate_succinate * succinyl_coA - rate_FADH2 * malate) * dt
    ATP += (rate_ATP * succinyl_coA - rate_succinate * ATP) * dt

    # Print current concentrations
    print(f"Time: {t*dt:.2f}s")
    print(f"Oxaloacetate: {oxaloacetate:.2f}")
    print(f"Acetyl-CoA: {acetyl_coA:.2f}")
    print(f"Citrate: {citrate:.2f}")
    print(f"Isocitrate: {isocitrate:.2f}")
    print(f"Alpha-ketoglutarate: {alpha_ketoglutarate:.2f}")
    print(f"Succinyl-CoA: {succinyl_coA:.2f}")
    print(f"Succinate: {succinate:.2f}")
    print(f"Fumarate: {fumarate:.2f}")
    print(f"Malate: {malate:.2f}")
    print(f"NADH: {NADH:.2f}")
    print(f"FADH2: {FADH2:.2f}")
    print(f"ATP: {ATP:.2f}")
    print()

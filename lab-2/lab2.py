# ============================================================
# Lab 2: Knowledge Representation & Formal Logic
# In-class template, we fill in the blanks together
#
# Reminder of the trick we're using everywhere below, PROOF BY
# REFUTATION: assume the premises AND the opposite of the
# conclusion, then ask satisfiable() if that can ever be true.
#   - False -> no such case exists -> the conclusion follows.
#   - a dictionary -> that's a counterexample, the argument is
#     NOT valid.
# ============================================================
 
from sympy import symbols, Implies, And, Or, Not
from sympy.logic.inference import satisfiable
 
 
# ============================================================
# Example 1: Demo, A Tiny Deduction Engine in SymPy
# If it rains, the ground gets wet. It's raining.
# So the ground must be wet. Let's make Python prove it.
# ============================================================
 
rain, ground_wet = symbols("rain ground_wet")
 
# TODO: write the rule (if rain, then ground_wet), combined
# with the fact that it IS raining, using And() and Implies().
premises   = And(Implies(rain, ground_wet), rain)
conclusion = ground_wet
 
check = And(premises, Not(conclusion))
 
print("Example 1:", satisfiable(check))
 
 
# ============================================================
# Example 2: Fill In the Blank, Snow and Coats
# Two rules chained together: snow forces cold, cold forces a
# coat.
# ============================================================
 
cold, wear_coat, snow = symbols("cold wear_coat snow")
 
rule1 = Implies(snow, cold)        # if it snows, it's cold
rule2 = Implies(cold, wear_coat)   # if it's cold, wear a coat
premises = And(rule1, rule2, snow) # ...and it IS snowing
 
conclusion = wear_coat  # TODO: what must follow, if it's snowing?
 
print("Example 2:", satisfiable(And(premises, Not(conclusion))))
 
 
# ============================================================
# Example 3: All Four Connectives Together
# A device: powered on, fan not running, overheating, error
# light, and whether it's safe to use.
# ============================================================
 
power_on, fan_running, overheating, error_light, safe_to_use = symbols(
    "power_on fan_running overheating error_light safe_to_use"
)
 
# TODO: if it's powered on AND the fan is NOT running, it overheats.
rule1 = Implies(And(power_on, Not(fan_running)), overheating)
 
# TODO: overheating implies the error light turns on.
rule2 = Implies(overheating, error_light)
 
# TODO: overheating OR the error light being on means it's not safe to use.
rule3 = Implies(Or(overheating, error_light), Not(safe_to_use))
 
# The facts we observe right now: it's on, and the fan is not running.
facts = And(power_on, Not(fan_running))
 
premises   = And(rule1, rule2, rule3, facts)
conclusion = Not(safe_to_use)
 
check = And(premises, Not(conclusion))
 
print("Example 3:", satisfiable(check))
 
 
# ============================================================
# Example 4: A Case Where It Does NOT Follow
# (Affirming the Consequent)
# Same rain/ground_wet rule as Example 1, but now backwards:
# we observe the ground is wet, and try to conclude it rained.
# ============================================================
 
rain2, ground_wet2 = symbols("rain2 ground_wet2")
 
# TODO: what we know (if rain2, then ground_wet2) AND the fact
# that the ground IS wet right now.
premises = And(Implies(rain2, ground_wet2), ground_wet2)
 
# TODO: the (flawed) claim we want to test: it must have rained.
conclusion = rain2
 
check = And(premises, Not(conclusion))
 
result = satisfiable(check)
print("Example 4:", result)
# Think about it: is this False, or a concrete counterexample?
# What does that tell us about the argument?
 
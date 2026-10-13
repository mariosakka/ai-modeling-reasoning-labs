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
conclusion = Not(ground_wet)  
 
check = And(premises, Not(conclusion))
 
print("Example 1:", satisfiable(check))


"""
If it rains ground is wet
Its raining
The ground must be wet


The ground is not wet

The inverse of the conclusion is false -> conclusion is true

There is an example in which the opposite of the conclusion is not true, conclusion true

Ground is wet & ground is not wet -> contradiction -> opposite of conclusion is false -> conclusion is true
"""
 
 
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
 


# Personal example from my field:
#   If the AI agent gets a vague prompt, it writes buggy code.
#   If the AI agent writes buggy code, the code ships a bug.
#   If the code ships a bug, production has an outage.
#   The prompt was clear and detailed (not vague).
#   Therefore, production will have no outage.
vague_prompt, buggy_code, bug_ships, outage = symbols("vague_prompt buggy_code bug_ships outage")

premises = And(
    Implies(vague_prompt, buggy_code),
    Implies(buggy_code, bug_ships),
    Implies(bug_ships, outage),
    Not(vague_prompt),
)
conclusion = Not(outage)

result = satisfiable(And(premises, Not(conclusion)))
print("My example:", result)  

# Where propositional logic breaks (my field):
#   "Every function that takes user input must validate it.
#    login() takes user input. So login() must validate it."
#   Propositional logic needs one symbol and one rule PER function
#   (login_takes_input -> login_validates, signup_takes_input -> signup_validates, ...),
#   and every new function means new rules.
#   First-order logic says it once: ForAll f. TakesInput(f) -> Validates(f)

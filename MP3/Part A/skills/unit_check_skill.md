---
name: unit_check_skill
description: Helps an AI catch unit-conversion errors and suspicious unit choices in engineering text.
---

# Unit Check Skill

## When to use this skill

Use this skill when reviewing engineering text, calculations, design notes, lab reports, or specifications that include units. Trigger this skill when the text includes dimensions, torque, force, stress, pressure, temperature, tolerance, material properties, or mixed unit systems.

## Steps

1. Identify every numerical value and its unit.
2. Check whether the units are consistent with the engineering context.
3. Look for suspicious conversions, mixed unit systems, or values that are unrealistic in scale.
4. Explain the issue clearly and give the likely correct unit or conversion.
5. If the exact correction cannot be confirmed, flag it as a possible unit issue instead of guessing.

## What to flag

- Mixing metric and imperial units without clear conversion.
- Very large or very small dimensions that do not match the part or load.
- Torque, force, stress, and pressure values used with the wrong equation units.
- Inch values that should likely be millimeters, or millimeter values that should likely be inches.
- Safety factors, tolerances, or material properties paired with inconsistent units.
- Equations such as Lewis bending, shaft stress, beam bending, or pressure calculations where units must match.

## What NOT to do

- Do not silently fix the value without explaining the unit problem.
- Do not assume the final answer is correct just because the equation name sounds correct.
- Do not overstate certainty when the document does not provide enough information.
- Do not rewrite the whole engineering paragraph unless asked.

---
name: engineering_question_with_context
description: Guides an AI to answer engineering questions by combining Ridgeline RAG context with unit conversion tools.
---

# Engineering Question With Context Skill

## When to use this skill

Use this skill when a user asks an engineering question that includes Ridgeline project history, company-specific design choices, prior project examples, internal standards, or unit conversions.

## Steps

1. If the question mentions Ridgeline, a Ridgeline project, internal standards, or past company work, call the Ridgeline RAG tool first.
2. If the question includes a unit that should be converted, call the unit conversion tool instead of converting from memory.
3. Read the tool results and connect them directly to the user’s question.
4. Give a synthesized engineering answer instead of dumping retrieved chunks.
5. Clearly separate project-specific context from general engineering judgment.

## What to flag

- Project names such as CardioSense, Millbrook, or other Ridgeline work.
- Loads, forces, dimensions, pressures, torques, tolerances, or temperatures needing conversion.
- Questions that combine prior design context with a new engineering decision.
- Cases where retrieved project information is incomplete or uncertain.

## What NOT to do

- Do not answer Ridgeline-specific questions from general memory only.
- Do not mentally convert units when the converter tool is available.
- Do not paste raw RAG chunks without explaining how they apply.
- Do not pretend the retrieved context is complete if the tool result is limited.

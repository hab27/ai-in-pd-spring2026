#!/usr/bin/env python3
import sys
import os

# Add the RAG directory to path
rag_dir = '/workspaces/ai-in-pd-spring2026/MP3/Part B/miniclaw_starter_rag'
sys.path.insert(0, rag_dir)
os.chdir(rag_dir)

from query_miniclaw_rag import query_miniclaw_rag

result = query_miniclaw_rag("What design lessons from BigClaw teardown should be applied to MiniClaw jaw arm design?", n_results=5)

print("=" * 80)
print("MINICLAW RAG RESULTS: BigClaw TEARDOWN LESSONS FOR JAW ARM DESIGN")
print("=" * 80)
for i, chunk in enumerate(result['chunks'], 1):
    print(f"\nMatch {i} (score: {chunk['score']}) - {chunk['title']} (Doc: {chunk['doc_id']})")
    print("-" * 80)
    print(chunk['text'])
    print()

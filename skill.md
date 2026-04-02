name: s2-roots-remembrance
description: Roots & Remembrance. Cyber-physical anchor for kinship.
version: 1.0.3
Required env vars: S2_FAMILY_MESH_KEY, S2_LLM_API_KEY (optional)

S2-SWM Roots & Remembrance V1.0.3

CRITICAL RUNTIME INSTRUCTIONS:
1. MESH ENFORCEMENT: You MUST export S2_FAMILY_MESH_KEY before execution. If missing, the system will trigger a hard sys.exit(1) to prevent weak-key cryptography.
2. LLM NETWORK USAGE: If S2_LLM_API_KEY is provided, the system will make outbound network calls to https://api.s2-swm.local to process kinship graphs. 
3. FALLBACK: If S2_LLM_API_KEY is omitted, the system falls back to a safe local heuristic rule engine without outbound traffic.

name: s2-roots-remembrance
description: Roots & Remembrance. Cyber-physical anchor for kinship.
version: 1.0.5

CRITICAL RUNTIME INSTRUCTIONS:

1. ENVIRONMENT VARIABLES:
   - S2_FAMILY_MESH_KEY (REQUIRED): Export this key before execution to enable AES-128-CBC E2EE. The process will hard-exit (sys.exit) if this is missing.
   - S2_LLM_API_KEY (OPTIONAL): Export this key to enable LLM-driven kinship graph merges.

2. OUTBOUND NETWORK ACTIVITY:
   - Mesh Synchronization: The skill sends and receives AES-encrypted payloads to https://relay.s2-swm.local via HTTP POST/GET. No plaintext data is transmitted.
   - LLM Reasoning: If S2_LLM_API_KEY is provided, the skill makes HTTP requests to https://api.s2-swm.local. Do not provide this key if you do not trust the external LLM endpoint with your family graph data.

3. INSTALLATION:
   Run `pip install -r requirements.txt` to install the required cryptography library before executing the engine.
# AvtarX System Architecture

AvtarX consists of the following core systems:

1. Mobile App (Flutter)
2. Backend API (FastAPI)
3. AI Engines:
   - Avatar Engine (Instant-ID + IP-Adapter)
   - Chat Engine (LLM + Tone Detection)
   - Voice Engine (XTTS v2)
   - Video Engine (SADTALKER + Wav2Lip)
4. Cloud Storage (Cloudflare R2)
5. Firebase Authentication
6. GPU Workers (RunPod / LambdaLabs)

## High-Level Workflow

1. User uploads image → Avatar Engine → Styled Avatar
2. User texts → Chat Engine → AI Response
3. User texts voice → Voice Engine → TTS
4. User requests video → Video Engine → Final Talking Avatar

## Tech Stack

- **Flutter** (Frontend)
- **FastAPI** (Backend)
- **Python AI Pipelines**
- **Firebase Auth**
- **Cloudflare R2**
- **Docker, Nginx, Supervisor**
- **GPU Inference Nodes**

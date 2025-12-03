# 🚀 AvtarX — AI Avatar • AI Chat • AI Voice • AI Video

AvtarX is a next-gen AI ecosystem that lets users:

- Create beautiful AI avatars  
- Generate talking-avatar videos  
- Chat with an adaptive AI personality  
- Generate human-like AI voices  
- Use one unified AI pipeline (Avatar → Chat → Voice → Video)

All inside a single app.

---

## ⚡ Features

- 🎭 **AI Avatar Generator** (Instant-ID + IP-Adapter)
- 🧠 **AI Chat Engine** (Tone detection + Adaptive personality)
- 🎤 **AI Voice Engine** (XTTS v2)
- 🎞 **AI Video Engine** (SADTALKER + Wav2Lip)
- 📱 **Flutter App with Neon Dark UI**
- 🔐 **Firebase Authentication**
- ☁️ **Cloudflare R2 Storage**
- 🖥 **GPU-powered microservices**

---

## 🏗 Project Structure

```
avtarx/
│
├── backend/          # FastAPI microservices
├── mobile/           # Flutter Neon App
├── docs/             # Technical documentation
├── devops/           # Docker + Nginx + GPU workers
├── scripts/          # Model install + deploy scripts
├── tests/            # Backend + API + Mobile tests
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🧠 Backend Structure (FastAPI)

```
backend/
│
├── auth/
│   ├── router.py
│   ├── signup.py
│   ├── login.py
│   └── verify.py
│
├── avatar/
│   ├── router.py
│   ├── engine.py
│   ├── instant_id.py
│   ├── ip_adapter.py
│   ├── enhancer.py
│   └── utils.py
│
├── chat/
│   ├── router.py
│   ├── engine.py
│   ├── tone_detector.py
│   ├── personality_adapter.py
│   └── llm_client.py
│
├── voice/
│   ├── router.py
│   ├── voice_mapper.py
│   └── tts/
│       └── xtts_v2.py
│
├── video/
│   ├── router.py
│   ├── caption_gen.py
│   ├── formatter.py
│   └── lipsync/
│       ├── sadtalker.py
│       └── wav2lip.py
│
├── models/
│   ├── instant_id_weights/
│   ├── ip_adapter_weights/
│   ├── stable_diffusion/
│   ├── wav2lip_weights/
│   └── sadtalker_weights/
│
├── config/
│   ├── settings.py
│   └── secrets_example.json
│
├── utils/
│   ├── logger.py
│   ├── storage.py
│   ├── ffmpeg.py
│   ├── cdn.py
│   └── queue_system.py
│
└── main.py
```

---

## 📱 Mobile App Structure (Flutter)

```
mobile/
└── lib/
    ├── main.dart
    ├── theme/
    │   └── app_theme.dart
    ├── screens/
    │   ├── onboarding/
    │   ├── home/
    │   ├── avatar_creator/
    │   ├── chat/
    │   ├── voice_chat/
    │   ├── video_preview/
    │   ├── history/
    │   └── profile/
    ├── components/
    ├── controllers/
    ├── services/
    └── utils/
```

---

## 🤖 AI Pipeline Flow

```
User Image
    ↓
Instant-ID → Identity Extract
    ↓
IP-Adapter → Style Mapping
    ↓
Avatar Enhancer → Glow & Cleanup
    ↓
User Text → Chat Engine → LLM
    ↓
AI Voice (XTTS) → Audio
    ↓
Talking Video (SADTALKER + Wav2Lip)
    ↓
1080x1920 Export → CDN
```

---

## 🐳 Docker Deployment

Start backend + workers + GPU:

```
cd devops
docker-compose up --build -d
```

---

## 📦 Install AI Model Weights

```
python scripts/install_models.py
```

Then place models here:

```
backend/models/
    ├── instant_id_weights/
    ├── ip_adapter_weights/
    ├── stable_diffusion/
    ├── wav2lip_weights/
    └── sadtalker_weights/
```

---

## 🚀 Running the Mobile App

```
cd mobile
flutter pub get
flutter run
```

---

## 📝 Docs Included

- Architecture  
- API Routes  
- Database Structure  
- Design System  
- Deployment Guide  
- Roadmap  

All inside `/docs`.

---

## 📄 License

MIT License © 2025 AvtarX

---

## 💬 Contributing

PRs welcome.  
Let's build the future of AI avatars 🔥

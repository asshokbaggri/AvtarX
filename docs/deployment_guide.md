# AvtarX Deployment Guide

## Step 1 — Backend Docker Build
docker build -t avtarx-backend -f backend.dockerfile .

## Step 2 — Start Services
docker-compose up -d

## Step 3 — GPU Worker Setup
docker build -t avtarx-gpu -f gpu.dockerfile .

## Step 4 — Nginx Reverse Proxy
- Configure SSL
- Enable CDN caching

## Step 5 — Firebase Auth Setup
- Add serviceAccountKey.json
- Update FIREBASE_CREDENTIALS in .env

## Step 6 — Model Installation
python scripts/install_models.py

#!/bin/bash

echo "Configuring firewall for AvtarX..."

ufw allow ssh
ufw allow 80
ufw allow 443
ufw allow 8000
ufw allow 8501

ufw --force enable

echo "Firewall setup complete!"

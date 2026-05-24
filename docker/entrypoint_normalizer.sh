#!/bin/bash
# Entrypoint for semantic normalizer container

echo "[Normalizer] Loading model $MODEL_NAME..."
python -c "
from normalizer import SemanticNormalizer
import torch
normalizer = SemanticNormalizer(model_name='$MODEL_NAME')
torch.save(normalizer.state_dict(), '/tmp/normalizer_state.pth')
print('Model loaded and cached.')
"

# Keep container alive (or run API server)
# For now, simple loop
while true; do
    sleep 3600
done

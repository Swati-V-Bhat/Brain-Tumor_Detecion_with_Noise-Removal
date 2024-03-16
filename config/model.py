import os

MOUNT_PATH = "/bucket"
MODEL_BUCKET = "brain-tumor-detection-model"
SEGMENTATION_MODEL_PATH = os.path.join(MOUNT_PATH, "models", "tumor_detection.keras")
DENOISING_MODEL_PATH = os.path.join(MOUNT_PATH, "models", "noiseremoval.keras")

INPUT_IMAGE_RESCALE = 255.0
MODEL_INPUT_SHAPE = (256, 256)
SEGMENTATION_PREDICTION_THRESHOLD = 0.5

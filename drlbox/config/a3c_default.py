
import multiprocessing

NUM_WORKERS     = multiprocessing.cpu_count()
PORT_BEGIN      = 2220
DISCOUNT        = 0.99
LEARNING_RATE   = 1e-4
ADAM_EPSILON    = 1e-4
GRAD_CLIP_NORM  = 40.0
ENTROPY_WEIGHT  = 0.01
ROLLOUT_MAXLEN  = 20
TRAIN_STEPS     = 1000000
INTERVAL_SAVE   = 10000


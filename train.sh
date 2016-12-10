python train_formatter.py ./data/train.csv ./data/stores.csv ./data/features.csv ./data/stores/train.vw
python3 split-shuffle.py 1.0 ./data/stores/train.vw ./data/stores/train-shuffled.vw
vw -f sales.model --passes=10 --cache_file=sales.cache --kill_cache --nn 100 < ./data/stores/train-shuffled.vw
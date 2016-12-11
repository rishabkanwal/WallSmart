TRAIN="train.vw"
TRAIN_SHUFFLED="train-shuffled.vw"

if [ "$1" = "-b" ] 
then
	OUTPUT_LOCATION=./data/baseline/
	FLAG=""
elif [ "$1" = "-s" ]
then
	OUTPUT_LOCATION=./data/stores/
	FLAG="-s"
elif [ "$1" = "-fs" ]
then
	OUTPUT_LOCATION=./data/stores_features/
	FLAG="-fs"
elif [ "$1" = "-f" ]
then
	OUTPUT_LOCATION=./data/features/
	FLAG="-f"
fi

python train_formatter.py ./data/train.csv ./data/stores.csv ./data/features.csv $OUTPUT_LOCATION$TRAIN $FLAG # Train with baseline
echo python train_formatter.py ./data/train.csv ./data/stores.csv ./data/features.csv $OUTPUT_LOCATION$TRAIN $FLAG # Train with baseline
python3 split-shuffle.py 1.0 $OUTPUT_LOCATION$TRAIN $OUTPUT_LOCATION$TRAIN_SHUFFLED
vw -f sales.model --passes=20 --cache_file=sales.cache --kill_cache --loss_function=quantile < $OUTPUT_LOCATION$TRAIN_SHUFFLED
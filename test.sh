TEST="test.vw"

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

python test_formatter.py ./data/test.csv ./data/stores.csv ./data/features.csv $OUTPUT_LOCATION$TEST $FLAG
vw -i sales.model -t -p ./results/predictions.txt < $OUTPUT_LOCATION$TEST # Run vw
python results_formatter.py ./results/predictions.txt ./data/test.csv ./results/results.txt # Run vw

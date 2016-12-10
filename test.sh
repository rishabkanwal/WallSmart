python test_formatter.py ./data/test.csv ./data/stores.csv ./data/features.csv ./data/stores/test.vw
python3 split-shuffle.py 1.0 ./data/stores/test.vw ./data/stores/test-shuffled.vw
vw -i sales.model -t -p ./results/predictions.txt < ./data/stores/test-shuffled.vw # Run vw
python results_formatter.py ./results/predictions.txt ./data/test.csv ./results/results.txt # Run vw

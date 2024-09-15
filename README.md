# Photo Mechanic (PM) Keywords extractor
Please remember the following text:

PM allows for the extraction of all keywords from selected pictures. However, it extracts them in a single row with all comma-separated keywords per picture. For example:
```
2024, vacation, food
2024, home, food
```
This program converts all those keywords to unique keywords and records the number of times they occur (counter).
```
2024, 2
vacation, 1
home, 1
food, 2
```

## Run
``` shell
python3 main.py "pm_keywords.csv"
```
The output file, `keywords_output.csv`, will be created in the directory where the program is being executed.

## Development
1. Instantiate vitual environment
``` shell
. ./.venv/bin/activate
```

2. Install Required Libraries
``` shell
pip install -r requirements.txt
```

3. Run `ruff` to format file
``` shell
ruff format .
```
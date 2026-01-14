.PHONY : run clean test

run: 
	uv run main.py

clean:
	find . -type d -name '__pycache__' -exec rm -rf {} +
	rm -f data.jsonl

test:
	uv run pytest

	


all:
	python3 gen.py

format:
	black *.py

clean:
	rm -rf cards/*.png
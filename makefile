all: print.pdf

gen:
	python3 gen.py

print.pdf: gen
	montage \
	  cards/*.png \
	  -page 850x1100+60+20 \
	  -geometry 225x350+0+0 \
	  -tile 3x3 \
	  -density 100 \
	  -background "#FFFFFF" \
	  print.pdf

format:
	black *.py

clean:
	rm -rf cards/*.png
	rm -f print.pdf

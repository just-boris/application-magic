all: build/main.pdf

build/main.pdf: img/field_distribution.png img/field_distribution2.png img/gauss3d.png img/intersection.png \
     img/transition.png img/twoCylinders.png img/twoCylinders2.png \
     img/planar_propagation.pdf  img/refraction_full_inner.pdf  img/refraction.pdf  img/transverse_movement.pdf 
	pdflatex -synctex=1 --output-directory=build -interaction=nonstopmode main.tex
%.png: 
	python python/$(*F).py

%.pdf: 
	inkscape -z -f img_static/$(*F).svg -A img/$(*F).pdf  
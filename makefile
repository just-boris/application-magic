all: build/main.pdf

build/main.pdf: img/field_distribution.png img/field_distribution2.png img/gauss3d.png img/intersection.png \
     img/transition.png img/twoCylinders.png img/twoCylinders2.png \
     img/planar_propagation.pdf  img/refraction_full_inner.pdf  img/refraction.pdf  img/transverse_movement.pdf \
     img/cylinder_axes.pdf img/polozok_a.pdf img/polozok_b.pdf img/polozok_c.pdf img/polozok_d.pdf img/polozok_e.pdf \
     img/polozok_f.pdf img/cylinder_sf.pdf img/cylinder_dsf.pdf
	pdflatex -synctex=1 --output-directory=build -interaction=nonstopmode main.tex
	cd .. && bibtex main && cd ..
	pdflatex -synctex=1 --output-directory=build -interaction=nonstopmode main.tex
	
%.png: 
	python python/$(*F).py

%.pdf: 
	inkscape -z -f img_static/$(*F).svg -A img/$(*F).pdf  
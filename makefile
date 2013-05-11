SHELL=C:/Windows/System32/cmd.exe
all: build/main.pdf

build/main.pdf: img/distribution_courning.png img/distribution_fog.png img/distribution_panda.png img/gauss3d.png \
     img/intersection.png img/intersection2.png img/transition.png img/transversal.png img/transversal2.png \
     img/angular.png \
     img/longitudinal.png img/planar_propagation.pdf  img/refraction_full_inner.pdf  img/refraction.pdf  \
     img/transverse_movement.pdf img/cylinder_axes.pdf img/polozok_a.pdf img/polozok_b.pdf img/polozok_c.pdf \
     img/polozok_d.pdf img/polozok_e.pdf img/polozok_f.pdf img/cylinder_sf.pdf img/cylinder_dsf.pdf \
     img/polozok_isometry.pdf img/longitudinal_movement.pdf img/gauss_divergence.pdf img/angular_movement.pdf
	pdflatex -synctex=1 --output-directory=build -interaction=nonstopmode main.tex
	cd build && bibtex main
	pdflatex -synctex=1 --output-directory=build -interaction=nonstopmode main.tex
	
%.png:
	cd python && python $(*F).py

%.pdf: 
	inkscape -z -f img_static/$(*F).svg -A img/$(*F).pdf  

window.onload = function() {
	var r = new X.renderer3D();
	r.init();

	var obj = new X.mesh();
	obj.file = 'http://x.babymri.org/?avf.vtk';

	r.add(obj);
	r.render();
}
(function(){
	window.onload = function() { 
		d3.select('html').style('height','100%').style('width','100%')
		d3.select('body').style('height','100%').style('width','100%')
		d3.select('#divPlot').style('width', "500px").style('height', "500px")
		scatterPlot3d( d3.select('#divPlot'));
	}
}());
	
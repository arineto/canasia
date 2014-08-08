var info_window;
var gdp_table;

function init_map(map){
	var mapOptions = {
		center: new google.maps.LatLng(20.929722535490466, 103.876090453125),
		zoom: 4
	};
	map = new google.maps.Map(document.getElementById("map-canvas"), mapOptions);

	google.maps.event.addListener(map, 'zoom_changed', function() {
	    zoomLevel = map.getZoom();
	    if (zoomLevel <= 7) {
	        gdp_table.setMap(map);
	    } else {
	        gdp_table.setMap(null);
	    }
	}); 

  	return map;
}

function highlight_countries(country){
	var query;
	if (country != "None"){
		query = {
			select: 'Geometry',
			from: '1tkLc2e9Om028843apCcCAsrkLhsK7DL9MnLiqhg6',
			where: "Name IN ('"+country+"')"
		}
	}else{
		query = {
			select: 'Geometry',
			from: '1tkLc2e9Om028843apCcCAsrkLhsK7DL9MnLiqhg6',
		}
	}
	gdp_table = new google.maps.FusionTablesLayer({
		query: query,
		map: map,
		styleId: 2,
		templateId: 2,
		styles: [ { polygonOptions: { fillOpacity: 0.65 } } ]
	});
}


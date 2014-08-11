var info_window;

function init_map(map){
	var mapOptions = {
		center: new google.maps.LatLng(20.929722535490466, 103.876090453125),
		zoom: 4
	};
	map = new google.maps.Map(document.getElementById("map-canvas"), mapOptions);

	google.maps.event.addListener(map, 'zoom_changed', function() {
	    zoomLevel = map.getZoom();
	    if (zoomLevel <= 7) {
	        data_table.setMap(map);
	    } else {
	        data_table.setMap(null);
	    }
	}); 

  	return map;
}

function highlight_countries(country, key, column){
	var query;
	if (country != "None"){
		query = {
			select: column,
			from: key,
			where: "Name IN ('"+country+"')"
		}
	}else{
		query = {
			select: column,
			from: key,
		}
	}
	data_table = new google.maps.FusionTablesLayer({
		query: query,
		map: map,
		styleId: 2,
		templateId: 2,
	});

	data_table.setMap(null);
	return data_table;
}
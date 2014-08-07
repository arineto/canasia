var info_window;

function init_map(map){
	var mapOptions = {
		center: new google.maps.LatLng(20.929722535490466, 103.876090453125),
		zoom: 4
	};
	map = new google.maps.Map(document.getElementById("map-canvas"), mapOptions);

	google.maps.event.addListener(map, 'click', function (e) {
		alert(e.latLng);
  	});

  	var world_geometry = new google.maps.FusionTablesLayer({
		query: {
			select: 'Geometry',
			from: '1tkLc2e9Om028843apCcCAsrkLhsK7DL9MnLiqhg6',
			// where: "Name IN ('China', 'Hong Kong')"
		},
		map: map,
		suppressInfoWindows: true,
		styles: [    
		    { where: "GDP > 5000", polygonOptions: { fillColor: "#000000" } },
		    { where: "GDP > 1000 and GDP < 5000", polygonOptions: { fillColor: "#00FF00" } },
		    // { where: "Name = 'India'", polygonOptions: { fillColor: "#000000" } },
		    // { where: "Name = 'South Korea'", polygonOptions: { fillColor: "#000000" } },
		    // { where: "Name = 'Indonesia'", polygonOptions: { fillColor: "#000000" } },
		    // { where: "Name = 'Thailand'", polygonOptions: { fillColor: "#000000" } },
		    // { where: "Name = 'Philippines'", polygonOptions: { fillColor: "#000000" } },
		    // { where: "Name = 'Singapore'", polygonOptions: { fillColor: "#000000" } },
		    // { where: "Name = 'Vietnam'", polygonOptions: { fillColor: "#000000" } },
		    // { where: "Name = 'Malaysia'", polygonOptions: { fillColor: "#000000" } },
		    // { where: "Name = 'Myanmar'", polygonOptions: { fillColor: "#000000" } },
		    // { where: "Name = 'Brunei'", polygonOptions: { fillColor: "#000000" } },
		    // { where: "Name = 'Cambodia'", polygonOptions: { fillColor: "#000000" } },
		    // { where: "Name = 'Laos'", polygonOptions: { fillColor: "#000000" } },
		    // { where: "Name = 'Taiwan'", polygonOptions: { fillColor: "#000000" } },
		    // { where: "Name = 'Hong Kong'", polygonOptions: { fillColor: "#000000" } }
		]
	});

  	return map;
}


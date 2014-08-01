var comp_hash = {};
var comp_name;
var comp_icon;
var comp_window;

///////////////////////////// TEXT SEAERCH /////////////////////////////
// function toggle_competitor(competitor, icon){
// 	if (competitor.checked){
// 		var request = {
// 		    location: map.getCenter(),
// 		    radius: '50000',
// 		    query: competitor.name
// 		};
		
// 		comp_icon = icon;
// 		comp_name = competitor.name;
// 		comp_hash[comp_name] = [];

// 		service = new google.maps.places.PlacesService(map);
// 		service.textSearch(request, callback);
// 	}else{
// 		array = comp_hash[competitor.name]
// 		for (i=0; i<array.length; i++){
// 			array[i].setMap(null);
// 		}
// 	}
// }

// function callback(results, status) {
//   if (status == google.maps.places.PlacesServiceStatus.OK) {
//     for (var i = 0; i < results.length; i++) {
//       var place = results[i];
//       createMarker(place.name, place.geometry.location, place.formatted_address);
//     }
//   }
// }

// function createMarker(name, latlng, address){
// 	var comp_marker;
// 	comp_marker = new google.maps.Marker({
// 		map: map,
// 		position: latlng,
// 		title: name,
// 		icon: comp_icon
// 	});

// 	google.maps.event.addListener(comp_marker, 'click', function () {
// 		if(comp_window){
// 			comp_window.setMap(null);
// 		}
// 		comp_window = new google.maps.InfoWindow({
// 			content: address
// 		})
// 		comp_window.open(map, comp_marker);
// 	});
// 	comp_hash[comp_name].push(comp_marker);
// }
////////////////////////////////////////////////////////////////////////
///////////////////////////// RADAR SEARCH /////////////////////////////
function toggle_competitor(competitor, icon){
	if (competitor.checked){
		var request = {
			bounds: map.getBounds(),
			keyword: competitor.name
		};
		
		comp_icon = icon;
		comp_name = competitor.name;
		comp_hash[comp_name] = [];
		service = new google.maps.places.PlacesService(map);
		service.radarSearch(request, callback);
	}else{
		array = comp_hash[competitor.name]
		for (i=0; i<array.length; i++){
			array[i].setMap(null);
		}
	}
}

function callback(results, status) {
	if (status != google.maps.places.PlacesServiceStatus.OK) {
	    alert(status);
	    return;
	}
    for (var i = 0; i < results.length; i++) {
		var place = results[i];
		// With detail
		// var request = {
		//   reference: place.reference
		// };
		// service.getDetails(request, callback2);
		// Without detail
		var comp_marker;
		comp_marker = new google.maps.Marker({
			map: map,
			position: place.geometry.location,
			// title: place.name,
			icon: comp_icon
		});
		comp_hash[comp_name].push(comp_marker);
  	}
}

// function callback2(place, status) {
//   if (status == google.maps.places.PlacesServiceStatus.OK) {
//     createMarker(place);
//   }
// }

// function createMarker(place){
// 	var comp_marker;
// 	comp_marker = new google.maps.Marker({
// 		map: map,
// 		position: place.geometry.location,
// 		title: place.name,
// 		icon: comp_icon
// 	});

// 	google.maps.event.addListener(comp_marker, 'click', function () {
// 		if(comp_window){
// 			comp_window.setMap(null);
// 		}
// 		comp_window = new google.maps.InfoWindow({
// 			content: "<p>"+place.name+"</p>"+"<p>"+place.formatted_address+"</p>"
// 		})
// 		comp_window.open(map, comp_marker);
// 	});
// 	comp_hash[comp_name].push(comp_marker);
// }
////////////////////////////////////////////////////////////////////////
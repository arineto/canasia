var info_window;

function init_map(map){
  var mapOptions = {
    center: new google.maps.LatLng(20.929722535490466, 103.876090453125),
    zoom: 4
  };
  map = new google.maps.Map(document.getElementById("map-canvas"), mapOptions);

  google.maps.event.addListener(map, 'click', function (e) {
  });
  return map;
}


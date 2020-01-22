// Function to define marker circle size
function markerSize(population) {
	return population/25;
}

var p1 = d3.json('geo.json');
var p2 = d3.json('visitAvg.json');

var complete = Promise.all([p1, p2]);
// console.log(complete)
complete.then((dat) => {
	// Define variables for our base layers
	var mapLayer = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
	attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
	});

	// var dat = complete

	var geo = p1
	var parks = p2
	//extract data

	var [geo, parks] = dat;

	var geoFeatures = geo.features;

	var park_coordinates = []
	var parkMarkers = []
	for (var key in parks.park_code) {

		var index;
		for (index = 0; index < geoFeatures.length; index++) {
			var current = geoFeatures[index];
			if (current.properties && current.properties.Code === parks.park_code[key])
				break;
		}

		park_coordinates[0] = geoFeatures[index].geometry.coordinates[1].toFixed(4)
		park_coordinates[1] = geoFeatures[index].geometry.coordinates[0].toFixed(4)
		// console.log(park_coordinates)		
		
		parkMarkersJan.push(
			L.circle(park_coordinates, {
				stroke: false,
				fillOpacity: 0.5,
				fillColor: `hsl(${100 - Math.round(pop2019 / 11827112 * 100)},75%,50%)`,
				color: "green",
				radius: 100000
			})
		);
		parkMarkers2.push(
			L.circle(park_coordinates, {
				stroke: false,
				fillOpacity: 0.5,
				fillColor: "red",
				color: "green",
				radius: 100000
			})
		);
	}	

	console.log(parkMarkers);
	var parkCircles = L.layerGroup(parkMarkers);
	var parkCircles2 = L.layerGroup(parkMarkers2);

	// Create a baseMaps object
	var baseMaps = {
		"Maplayer": mapLayer
	};

	// Create an overlay object
	var overlayMaps = {
		"Park": parkCircles,
		"Park2": parkCircles2
	};

	var myMap = L.map('map', {
		center: [39.50, -98.35],
		zoom: 5,
		layers: [mapLayer, parkCircles, parkCircles2]
	});

	// Pass our map layers into our layer control
	// Add the layer control to the map
	L.control.layers(baseMaps, overlayMaps, {
		collapsed: false
	}).addTo(myMap);


});




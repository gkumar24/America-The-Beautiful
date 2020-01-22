// Function to define marker circle size
function markerSize(population) {
	return population/25;
}

var p1 = d3.json('static/json/natparks_geo.json');
var p2 = d3.json('static/json/visitAvg.json');

// read thorugh the json files
var complete = Promise.all([p1, p2]);
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

	// get the features that contain the detail for each national parks
	var geoFeatures = geo.features;


	var park_coordinates = []
	var parkMarkers = {}
	var monvalue = ""
	var parkVisit = 0
	var visitPercent = 0

	for (var datakey in parks) {
		if (datakey != "park_code" && datakey != "avg_monthly" && datakey != "great_month") {
			monvalue = datakey.split("_")[1]
			parkMarkers[monvalue.toUpperCase()] = []
		}		
	}

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
		
		
		var cal20 = parks.avg_monthly[key] * 20 / 50;
		var cal40 = parks.avg_monthly[key] * 40 / 50;
		var cal60 = parks.avg_monthly[key] + ((parks.great_month[key] - parks.avg_monthly[key]) * 10 / 50);
		var cal80 = parks.avg_monthly[key] + ((parks.great_month[key] - parks.avg_monthly[key]) * 30 / 50);		

		for (var datakey in parks) {
			if (datakey != "park_code" && datakey != "avg_monthly" && datakey != "great_month") {
				monvalue = datakey.split("_")[1]
				parkVisit = parks[datakey][key]

				if (parkVisit <= cal20) {
					visitPercent = 10
				} else if (parkVisit <= cal40) {
					visitPercent = 30
				} else if (parkVisit <= cal60) {
					visitPercent = 50
				} else if (parkVisit <= cal80) {
					visitPercent = 70
				} else {
					visitPercent = 90
				}

				parkMarkers[monvalue.toUpperCase()].push(
					L.circle(park_coordinates, {
						stroke: false,
						fillOpacity: 0.9,
						fillColor: `hsl(${100 - visitPercent},75%,50%)`,
						color: "green",
						radius: 100000
					})
				);
			}		
		}
						
	} //end of park key for

	// Create a baseMaps object
	var baseMaps = {
		"Maplayer": mapLayer	
	};

	// Create Over Lay
	var monthlayer = []
	monthlayer.push(mapLayer)

	var overlayMaps = {}
	
	for (var markKey in parkMarkers) {
		var parkCircles = L.layerGroup(parkMarkers[markKey]);	
		monthlayer.push(parkCircles)

		// Create an overlay object
		overlayMaps[markKey] = parkCircles;
	}	

	// Group Over Lay for Radio button
	var groupedOverlays= {}
	groupedOverlays["Month"] = overlayMaps
	

	var myMap = L.map('map', {
		center: [39.50, -98.35],
		zoom: 4,
		layers: monthlayer
	});

	// Pass our map layers into our layer control
	// Add the layer control to the map

	var options = {
		// Make the "Landmarks" group exclusive (use radio inputs)
		exclusiveGroups: ["Month"],
		collapsed: false
	  };

	L.control.groupedLayers(baseMaps, groupedOverlays, options).addTo(myMap);
});




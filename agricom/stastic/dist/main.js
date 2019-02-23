function our_layer(map.options){
	var datasets = new L.GeoJSON.AJAX("{% url 'districts' %}",{

		style: function colors(feature){
			switch(feature.properties.districts){
				case 'kaski':
					return{
						color: 'orange',
						fillOpacity: 0.8
					};
				break;
				case 'syangja':
					return{
						color: 'purple',
						fillOpacity: 0.8
					};
				break;
			}
		}

		onEachFeature: function(feature,layer){
			layer.bindPopup(feature.properties.dist_name.toString());
		}

	});

	var points = new L.GeoJSON.AJAX(" {% url 'incidences' %} ",{
		onEachFeature: function(feature,layer){
			layer.bindPopup(feature.properties.name.toString());
		}

	});

	datasets.addTo(map);
	points.addTo(map);

}


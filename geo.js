// Load a GeoJSON file
var vectorLayer = new ol.layer.Vector({
    source: new ol.source.Vector({
        url: 'https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json',
        format: new ol.format.GeoJSON()
    }),
    style: new ol.style.Style({
        stroke: new ol.style.Stroke({
            color: 'blue',
            width: 2
        }),
        fill: new ol.style.Fill({
            color: 'rgba(0, 0, 255, 0.3)'
        })
    })
});

// Add GeoJSON layer to the map
map.addLayer(vectorLayer);

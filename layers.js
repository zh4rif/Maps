var satelliteLayer = new ol.layer.Tile({
    source: new ol.source.TileWMS({
        url: 'https://gibs.earthdata.nasa.gov/wms/epsg4326/best/wms.cgi',
        params: { 'LAYERS': 'MODIS_Terra_SurfaceReflectance_Bands121', 'TILED': true },
        serverType: 'geoserver'
    })
});

// Add Satellite Layer
map.addLayer(satelliteLayer);

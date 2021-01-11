// Initialize and add the map
function initMap() {
    // The location of Uluru
    const uluru = { lat: 49.250005, lng: -123.138127 };
    // The map, centered at Uluru
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 12,
      center: uluru,
    });

    // The marker, positioned at Uluru
    const marker = new google.maps.Marker({
      position: uluru,
      map: map,
    });

    // create a square
    const rectangle = new google.maps.Rectangle({
      strokeColor: "#FF0000",
      strokeOpacity: 0.6,
      strokeWeight: 2,
      fillColor: "#FF0000",
      fillOpacity: 0,
      map,
      bounds: {
        north: 49.27936860000001,
        south: 49.2571768,
        east: -123.1389362,
        west: -123.1859637,
        // north: 33.685,
        // south: 33.671,
        // east: -116.234,
        // west: -116.251,
      }
    });

}
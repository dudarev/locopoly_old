// Initialization function
function initialize_map() {
    var myOptions = {
        zoom: 3,
        scrollwheel: false,
        center: new google.maps.LatLng(48.03,20),
        mapTypeControl: true,
        mapTypeControlOptions: {style: google.maps.MapTypeControlStyle.DROPDOWN_MENU},
        navigationControl: true,
        navigationControlOptions: {style: google.maps.NavigationControlStyle.ZOOM_PAN},
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };

    map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);
    geocoder = new google.maps.Geocoder();
}

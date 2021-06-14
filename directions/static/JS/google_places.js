
// // $.getScript( "https://maps.googleapis.com/maps/api/js?key=" + google_api_key + "&libraries=places") 
// // .done(function( script, textStatus ) {
// //     google.maps.event.addDomListener(window, "load", initAutocomplete())
// // })


// let autocomplete_a;
// let autocomplete_b;

// function initAutocomplete() {

//   autocomplete_a = new google.maps.places.Autocomplete(
//    document.getElementById('id-google-address-a'),
//    {
//        types: ['address'],
//        componentRestrictions: {'country': ['us']},
//    })
  
//   autocomplete_a.addListener('place_changed', function(){
//     onPlaceChanged('a')
//   });


//   autocomplete_b = new google.maps.places.Autocomplete(
//    document.getElementById('id-google-address-b'),
//    {
//        types: ['address'],
//        componentRestrictions: {'country': ['us']},
//    })
  
//   autocomplete_b.addListener('place_changed', function(){
//     onPlaceChanged('b')
//   });

// }


// function onPlaceChanged (addy){

//     let auto
//     let el_id
//     let lat_id
//     let long_id

//     if ( addy === 'a'){
//         auto = autocomplete_a
//         el_id = 'id-google-address-a'
//         lat_id = 'id-lat-a'
//         long_id = 'id-long-a'
//     }
//     else{
//         auto = autocomplete_b
//         el_id = 'id-google-address-b'
//         lat_id = 'id-lat-b'
//         long_id = 'id-long-b'
//     }

//     var geocoder = new google.maps.Geocoder()
//     var address = document.getElementById(el_id).value

// //     geocoder.geocode( { 'address': address}, function(results, status) {

// //         if (status == google.maps.GeocoderStatus.OK) {
// //             var latitude = results[0].geometry.location.lat();
// //             var longitude = results[0].geometry.location.lng();

// //             $('#' + lat_id).val(latitude) 
// //             $('#' + long_id).val(longitude) 

// //             CalcRoute()
// //         } 
// //     }); 
// // }


// // function validateForm() {
// //     var valid = true;
// //     $('.geo').each(function () {
// //         if ($(this).val() === '') {
// //             valid = false;
// //             return false;
// //         }
// //     });
// //     return valid
// // }


// // function CalcRoute(){

// //     if ( validateForm() == true){
// //       var params = {
// //           lat_a: $('#id-lat-a').val(),
// //           long_a: $('#id-long-a').val(),
// //           lat_b: $('#id-lat-b').val(),
// //           long_b: $('#id-long-b').val(),
// //       };

// //       var esc = encodeURIComponent;
// //       var query = Object.keys(params)
// //           .map(k => esc(k) + '=' + esc(params[k]))
// //           .join('&');

// //       url = '/map/map?' + query
// //       window.location.assign(url)
// //     }

// // }

// This example requires the Places library. Include the libraries=places
// parameter when you first load the API. For example:
// <script
// src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places">
let map;

function initMap() {
    const map = new google.maps.Map(document.getElementById("map"), {
        mapTypeControl: false,
        center: { lat: 40.7128, lng: -74.0060 },
        zoom: 8,
    });
    new AutocompleteDirectionsHandler(map);
}
  
class AutocompleteDirectionsHandler {
    map;
    originPlaceId;
    destinationPlaceId;
    travelMode;
    directionsService;
    directionsRenderer;
    constructor(map) {
        this.map = map;
        this.originPlaceId = "";
        this.destinationPlaceId = "";
        this.travelMode = google.maps.TravelMode.WALKING;
        this.directionsService = new google.maps.DirectionsService();
        this.directionsRenderer = new google.maps.DirectionsRenderer();
        this.directionsRenderer.setMap(map);
        const originInput = document.getElementById("origin-input");
        const destinationInput = document.getElementById("destination-input");
        const modeSelector = document.getElementById("mode-selector");
        const originAutocomplete = new google.maps.places.Autocomplete(originInput);
        // Specify just the place data fields that you need.
        originAutocomplete.setFields(["place_id"]);
        const destinationAutocomplete = new google.maps.places.Autocomplete(destinationInput);
        // Specify just the place data fields that you need.
        destinationAutocomplete.setFields(["place_id"]);
        this.setupClickListener(
            "changemode-walking",
            google.maps.TravelMode.WALKING
        );
        this.setupClickListener(
            "changemode-transit",
            google.maps.TravelMode.TRANSIT
        );
        this.setupClickListener(
            "changemode-driving",
            google.maps.TravelMode.DRIVING
        );
        this.setupPlaceChangedListener(originAutocomplete, "ORIG");
        this.setupPlaceChangedListener(destinationAutocomplete, "DEST");
        this.map.controls[google.maps.ControlPosition.TOP_LEFT].push(originInput);
        this.map.controls[google.maps.ControlPosition.TOP_LEFT].push(destinationInput);
        this.map.controls[google.maps.ControlPosition.TOP_LEFT].push(modeSelector);
    }
    // Sets a listener on a radio button to change the filter type on Places
    // Autocomplete.
    setupClickListener(id, mode) {
        const radioButton = document.getElementById(id);
        radioButton.addEventListener("click", () => {
            this.travelMode = mode;
            this.route();
        });
    }
    setupPlaceChangedListener(autocomplete, mode) {
        autocomplete.bindTo("bounds", this.map);
        autocomplete.addListener("place_changed", () => {
            const place = autocomplete.getPlace();
  
        if (!place.place_id) {
            window.alert("Please select an option from the dropdown list.");
            return;
        }
  
        if (mode === "ORIG") {
        this.originPlaceId = place.place_id;
        } else {
        this.destinationPlaceId = place.place_id;
        }
        this.route();
        });
    }
    route() {
        if (!this.originPlaceId || !this.destinationPlaceId) {
            return;
        }
        const me = this;
        this.directionsService.route(
            {
            origin: { placeId: this.originPlaceId },
            destination: { placeId: this.destinationPlaceId },
            travelMode: this.travelMode,
            },
            (response, status) => {
                if (status === "OK") {
                    me.directionsRenderer.setDirections(response);
                } else {
                    window.alert("Directions request failed due to " + status);
                }
            }
        );
    }
}
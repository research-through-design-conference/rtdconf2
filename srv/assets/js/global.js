/*#############################################

LONDON MAP

##############################################*/

function initialize() {

    var featureOpts = [
        {
            featureType: "transit.line",
            stylers: [
                { saturation: 100 },
                { gamma: 0.99 },
                { hue: "#ff3300" },
                { visibility: "on" }
            ]
        }, {
            featureType: "landscape.man_made",
            elementType: "geometry",
            stylers: [
                { visibility: "off" }
            ]
        }, {
            featureType: "poi.business",
            stylers: [
                { visibility: "on" }
            ]
        }, {
            featureType: "poi.attraction",
            stylers: [
                { visibility: "simplified" }
            ]
        }, {
            stylers: [
                { gamma: 2.58 },
                { saturation: 58 },
                { hue: "#c93225" }
            ]
        }, {
            featureType: "road",
            elementType: "labels.icon",
            stylers: [
                { visibility: "on" }
            ]
        }, {
        }
    ];

    MY_MAPTYPE_ID = 'custom_style';

    contentString = '<p style="margin: 5px;"><a href="https://www.google.co.uk/maps/dir//Microsoft+Research+Ltd,+21+Station+Rd,+Cambridge+CB1+2FB/@52.1949893,0.135552,16z/data=!4m12!1m3!3m2!1s0x0:0x42e20fc9462442a9!2sMicrosoft+Research+Ltd!4m7!1m0!1m5!1m1!1s0x47d8774a2ae748a9:0x42e20fc9462442a9!2m2!1d0.134991!2d52.19488" target="_blank">View directions</a> on Google Maps</p>';

    infowindow = new google.maps.InfoWindow({
        content: contentString,
        maxWidth: 280
    });

    rtd2015_loc = new google.maps.LatLng(52.19488, 0.134991);

    mapOptions = {
        zoom: 16,
        center: rtd2015_loc,
        mapTypeControl: false,
        mapTypeId: MY_MAPTYPE_ID,
        scrollwheel: false,
        draggable: true
    };

    map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

    styledMapOptions = {
        name: 'RTD 2015 Map'
    };

    customMapType = new google.maps.StyledMapType(featureOpts, styledMapOptions);

    map.mapTypes.set(MY_MAPTYPE_ID, customMapType);

    image = window.url + '/img/map_marker.png';

    rtd2015_loc_marker = new google.maps.Marker({
        position: rtd2015_loc,
        map: map,
        icon: {
            url: image,
            scaledSize: new google.maps.Size(30, 55)
        },
        animation: google.maps.Animation.DROP,
        title: 'RTD2015'
    });
    google.maps.event.addListener(rtd2015_loc_marker, 'mouseover', function() {
        infowindow.open(map, rtd2015_loc_marker);
    });
}

google.maps.event.addDomListener(window, 'load', initialize);

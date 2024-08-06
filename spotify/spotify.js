var client_id = "ffce952d017245b191dcf95415691f40";
var client_secret = "01809d81cb9247b1848d2d6cbbf471cf";
var user_id = "khi.kidman";

var authOptions = {
    url: 'https://accounts.spotify.com/api/token',
    headers: {
        'Authorization': 'Basic ' + (new Buffer.from(client_id + ':' + client_secret).toString('base64'))
    },
    form: {
        grant_type: 'client_credentials'
    },
    json: true
};

request.post(authOptions, function(error, response, body) {
    if (!error && response.statusCode === 200) {
      var token = body.access_token;
    }
});

var songs = document.getElementById("songs");

var mytracks = JSON.parse(items);

mytracks.forEach(element => {
    var song = songs.incertCell(-1);
    song.innerHTML = "song";
});

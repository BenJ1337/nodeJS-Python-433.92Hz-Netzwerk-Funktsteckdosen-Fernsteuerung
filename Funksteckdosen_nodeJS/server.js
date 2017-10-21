var winston = require("winston");
var express = require("express");
var http = require("http");
var path = require( "path" );
var gpio = require("pi-gpio");
var PythonShell = require('python-shell');

var PORT = 1337;

var app = express();
var server = http.Server(app);

var PUBLICPATH = path.join( __dirname, 'public' )

app.use('/public', express.static( PUBLICPATH ) );

app.get( '/', function( req, res ){
	res.sendFile( path.join( PUBLICPATH, 'index.html' ) );
});

logger = new ( winston.Logger )({
	transports: [ new (winston.transports.Console)({
		level: 'debug',
		handleExceptions: true,
		json: false,
		colorize: true
		})
	]
});

server.listen( PORT );
logger.info("Server is running!");

var a_on = '11101100110000110'
var a_off = '11101100110000011'
var b_on = '11101100011000110'
var b_off = '11101100011000011'
var c_on = '11101100001100110'
var c_off = '11101100001100011'
var d_on = '11101100000110110'
var d_off = '11101100000110011'

var senden = function( value, stecker, callback ) { 
		if ( active == false) {
			active = true;
     		var options = {
  				mode: 'text',
  				pythonOptions: ['-u'],
  				args: [ value ]
			};
				PythonShell.run('python/sendenArgs.py', options, function (err, result) {
  					if (err) throw err;	
					active = false;
					logger.info( stecker + ' ' + result);
					callback( stecker );
				});	
		} else {
			logger.info( 'python is still active' );		
		}
}


var io = require('socket.io')( server, {});
var active = false;

io.sockets.on('connection', function ( socket ) {
	socket.on("con", function(data, callback) {
		switch( data ) {
			case 'steckerAON':
				senden( a_on, 'A on', callback );
				break;	
			case 'steckerAOFF':
				senden( a_off, 'A off', callback );
				break;	
			case 'steckerBON':
				senden( b_on, 'B on', callback );
				break;		
			case 'steckerBOFF':
				senden( b_off, 'B off', callback  );
				break;	
			case 'steckerCON':
				senden( c_on, 'C on', callback  );
				break;		
			case 'steckerCOFF':
				senden( c_off, 'C off', callback );
				break;	
			case 'steckerDON':
				senden( d_on, 'D on', callback );	
				break;	
			case 'steckerDOFF':
				senden( d_off, 'D off', callback );
				break;	
		} 		
    	});
} );


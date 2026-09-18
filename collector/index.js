"use strict";

var _log4js = _interopRequireDefault(require("log4js"));

var _net = _interopRequireDefault(require("net"));

var _ngeohash = _interopRequireDefault(require("ngeohash"));

var _parser = _interopRequireDefault(require("./parser"));

var _api = _interopRequireDefault(require("./api"));

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

let logger = _log4js.default.getLogger();

logger.level = process.env.DEBUG_LEVEL || 'info';

const Influx = require('influx'); // InfluxDB Initialization.


const influx = new Influx.InfluxDB({
  database: process.env.INFLUX_DB,
  protocol: process.env.INFLUX_PROTOCOL || 'http',
  host: process.env.INFLUX_HOST || process.env.INFLUX_URL,
  port: parseInt(process.env.INFLUX_PORT) || 8086,
  username: process.env.INFLUX_USER || 'EXAMPLE_USER',
  password: process.env.INFLUX_PWD || 'EXAMPLE_PASSWORD'
});
influx.createDatabase(process.env.INFLUX_DB).catch(error => {
  // if the database exists or the user doesn't have sufficient privileges, this will fail
  logger.error(error.message);

  if (error.message.includes('ENOTFOUND')) {
    logger.error('Bye');
    process.exit(1);
  }
});
const port = process.env.PORT || 7070;

const server = _net.default.createServer();

server.on('connection', socket => {
  logger.info(`CONNECTED: ${socket.remoteAddress}:${socket.remotePort}`);
  socket.on('data', async data => {
    try {
      socket.end();
      logger.debug('Received data', data.toString());
      const {
        ip,
        port,
        username
      } = (0, _parser.default)(data.toString());
      logger.debug(`Parsed ${username} ${ip} ${port}`);
      const ipLocation = await (0, _api.default)(ip);

      if (!ipLocation) {
        logger.error('No data retrieved, cannot continue');
        return;
      }

      const geohashed = _ngeohash.default.encode(ipLocation.lat, ipLocation.lon);

      logger.debug(`Geohashing with lat: ${ipLocation.lat}, lon: ${ipLocation.lon}: ${geohashed}`); // Remove lon and lat from tags

      const {
        lon,
        lat,
        ...others
      } = ipLocation;
      influx.writePoints([{
        measurement: 'geossh',
        fields: {
          value: 1,
          latitude: ipLocation.lat,
          longitude: ipLocation.lon
        },
        tags: {
          geohash: geohashed,
          username,
          port,
          ip,
          location: `${ipLocation.regionName}, ${ipLocation.city}`,
          ...others
        }
      }]);
    } catch (e) {
      logger.error('An error has occurred processing one connection:', e.message);
    }
  });
  socket.on('close', () => {
    logger.info(`CLOSED: ${socket.remoteAddress}:${socket.remotePort}`);
  });
});
server.listen(port, () => {
  logger.info(`TCP Server is running on port ${port}.`);
});
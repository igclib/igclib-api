![igclib logo](https://cdn.jsdelivr.net/gh/teobouvard/igclib@master/assets/igclib_logo.svg)

## Setup

```
git clone https://github.com/teobouvard/igclib-api.git
make install
make runserver
```

## Usage

```
curl -L -F "flight=@/path/to/igc/file" -F "airspace=@/path/to/openair/file" http://ENDPOINT/api/xc --max-time 500
```

## Problems

If the airspace file is big, it can take more than one minute to check the whole flight for intersections. This processing time can lead to HTTP timeouts, so if you run this behind a proxy, make sure to tune the right settings.

## Environment variables

Make sure to define

- `AIRSPACE_FILE` : point to an openair airspace file
- `ELEVATION_API_KEY` : API key for [elevation service](https://geolocalisation.ffvl.fr/elevation)

## Requirements

- [igclib](https://www.github.com/teobouvard/igclib)

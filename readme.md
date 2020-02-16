![igclib banner](https://cdn.jsdelivr.net/gh/igclib/assets@master/img/banner/igclib_banner.svg)

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

## Environment variables

Make sure to define

- `AIRSPACE_FILE` : point to an openair airspace file
- `ELEVATION_API_KEY` : API key for [elevation service](https://geolocalisation.ffvl.fr/elevation)

## Requirements

- [igclib](https://www.github.com/igclib/igclib)

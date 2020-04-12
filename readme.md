![igclib banner](https://cdn.jsdelivr.net/gh/igclib/assets@master/img/banner/igclib_api_banner.svg)

## Setup

```
git clone https://github.com/igclib/igclib-api.git
make install
make runserver
```

## Usage

```
curl -L -F "flight=@/path/to/igc/file" -F "airspace=@/path/to/openair/file" endpoint/api/xc
```

## Environment variables

Make sure to define

- `AIRSPACE_FILE` : points to an openair airspace file
- `ELEVATION_API_KEY` : API key for [elevation service](https://geolocalisation.ffvl.fr/elevation)

## Requirements

- [igclib](https://www.github.com/igclib/igclib)

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

- `DEFAULT_AIRSPACE` : points to an openair airspace file, used as fallback when no airspace argument is given
- `ELEVATION_API_KEY` : API key for [elevation service](https://geolocalisation.ffvl.fr/elevation), if you want to validate airspaces relative to ground altitude

## Requirements

- [igclib](https://www.github.com/igclib/igclib)

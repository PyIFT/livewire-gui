# Live-Wire

Simple user interface to perform segmentation using live-wire.

<p align="center">
  <img src="./images/demo.gif" alt="live-wire demo" width="80%"/>
  </a>
</p>

## Installation

```shell script
pip install -r requirements
```

## Usage

```shell script
python app.py <image file>
```

 - Click to select point.
 - Press `S` to close contour.
 - Adjust `sigma` as necessary on bottom left corner.
    * Low `sigma` high boundary adherence (min-max distance).
    * High `sigma` low boundary adherence (geodesic distance).

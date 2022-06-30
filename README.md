# Live-Wire

Simple user interface to perform segmentation using live-wire.

<p align="center">
  <img src="./images/demo.gif" alt="live-wire demo" width="80%"/>
  </a>
</p>

## Installation

Clone the repository into your computer through the command line using git
```bash
git clone https://github.com/PyIFT/livewire-gui
```

Move into cloned directory
```bash
cd livewire-gui
```

Install requirements
```bash
pip install -r requirements
```

## Usage

```bash
python app.py <image file>
```

 - Click to select point.
 - Press `S` to close contour.
 - Adjust `sigma` as necessary on bottom left corner.
    * Low `sigma` high boundary adherence (min-max distance).
    * High `sigma` low boundary adherence (geodesic distance).

#!/usr/bin/env python3

import sys
import napari
import numpy as np
from PIL import Image
from pyift.livewire import LiveWire
from skimage import color
from magicgui import magicgui
from qtpy.QtWidgets import QDoubleSpinBox


def main(args):
    image = np.asarray(Image.open(args[1]))
    default_sigma = 5.0

    with napari.gui_qt():
        viewer = napari.view_image(image, rgb=True)

        livewire = LiveWire(color.rgb2lab(image), sigma=default_sigma)
        layer = viewer.add_labels(livewire.contour,
                                  color={1: 'cyan'},
                                  name='contour', opacity=1.0)

        def valid(coords):
            return 0 <= round(coords[0]) < image.shape[0] and 0 <= round(coords[1]) < image.shape[1]

        @layer.mouse_move_callbacks.append
        def mouse_move(layer, event):
            coords = layer.coordinates
            if valid(coords):
                livewire.select(coords)
                layer.data = livewire.contour

        @layer.mouse_drag_callbacks.append
        def mouse_click(layer, event):
            livewire.confirm()

        @viewer.bind_key('s')
        def close_contour(viewer):
            livewire.close()
            layer.data = livewire.contour

        @magicgui(auto_call=True,
                  sigma={'widget_type': QDoubleSpinBox, 'maximum': 255, 'minimum': 0.01, 'singleStep': 5.0})
        def update_sigma(sigma: float = default_sigma):
            livewire.sigma = sigma

        sigma_box = update_sigma.Gui()
        viewer.window.add_dock_widget(sigma_box, area='left')
        viewer.layers.events.changed.connect(lambda x: sigma_box.refresh_choices())


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("app.py <input image path>")
        sys.exit(-1)
    main(sys.argv)

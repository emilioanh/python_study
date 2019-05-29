import argparse
import os
import importlib.util
spec = importlib.util.spec_from_file_location("interfaces.BarcodeReader", os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\interfaces\\barcode_reader.py")
foo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(foo)
print(foo.BarcodeReader.cac())
# foo.BarcodeReader()
# from interfaces import BarcodeReader
# from pyzbar import pyzbar
# import cv2


class PyzbarReader(foo.BarcodeReader):
    def __init__(self):
        pass

    def read_from_path(self, image_path):
        image = cv2.imread(image_path)
        return self.__decode(image)

    def read_from_buffer(self, buffer):
        return self.__decode(buffer)

    def __decode(self, buffer):
        barcodes = pyzbar.decode(buffer)

        outputs = []

        for barcode in barcodes:
            barcode_type = barcode.type
            content = barcode.data.decode('utf-8')

            # extract barcode location
            (x_axis, y_axis, width, height) = barcode.rect
            location = (x_axis, y_axis, x_axis + width, y_axis + height)

            # append to outputs
            outputs.append({
                'type': barcode_type,
                'content': content,
                'location': location})

        return outputs

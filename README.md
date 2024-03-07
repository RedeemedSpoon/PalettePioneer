![PaletterPioneer Logo](./static/logo.svg)

## Introduction

[PaletterPioneer](https://palettepioneer.onrender.com/) is a web application, designed to generate a 10-color palette from an uploaded image. The generated palette represents the most frequent colors present in the image while ensuring a diverse and aesthetically pleasing range. Whether you're a designer seeking inspiration or just curious about the dominant colors of an image, PaletterPioneer provides a straightforward solution.

## Features

- **Image Upload:** Easily upload any image file format.
- **Color Palette Generation:** Extracts the 10 most frequent and distinct colors from the image.
- **Resolution Details:** Displays the resolution of the uploaded image.
- **Filename Display:** Provides the original filename of the uploaded image.
- **Color Preview:** Renders a visual representation of the generated color palette.
- **Infinite usage:** There are no limitation when it comes to usage.

## Limitations

- **Performance Issues on Limited Resources:** The KMeans clustering algorithm employed for color extraction can be computationally intensive, especially on server with 512MB RAM. This might result in slower processing times or potential timeouts.

## How to Use

1. Navigate to the PaletterPioneer website.
2. Click on the upload button to select an image from your device.
3. After uploading, the system will process the image to extract the 10 most dominant colors.
4. Once processed, you will be presented with a color palette, along with other details such as image resolution and filename.
5. Optionally, you can copy or use the generated color palette for your design projects.

## Contribution

If you're interested in contributing to PaletterPioneer, feel free to fork the repository, make your changes, and submit a pull request. Your contributions, whether it's bug fixes, feature enhancements, or feedback, are highly appreciated.


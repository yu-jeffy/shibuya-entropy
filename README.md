# Shibuya Crossing Entropy Generator

## Overview
Inspired by CloudFlare's creative use of lava lamps to generate randomness for encryption, the Shibuya Crossing Entropy Generator leverages the bustling activity at Shibuya Crossing. By capturing video streams of this intersection, our project utilizes the inherent randomness of the crowd and vehicle movements to generate random, high-entropy data.

## Project Components
- **`shibuyaStream.py`**: This module downloads a frame from a Shibuya Crossing live video stream using `yt-dlp` and `ffmpeg`.
- **`generateEntropy.py`**: Executes the entropy generation. It calls `shibuyaStream.py` to download an image and then processes this image to create a 32-character alphanumeric code, symbolizing the generated entropy.

## Installation
To set up the Shibuya Entropy Generator, you need to install several dependencies. Please run the following commands to ensure all necessary libraries and tools are installed:

```bash
pip install Pillow yt-dlp
sudo apt-get install ffmpeg
```

## Usage
To run the generator, execute the `generateEntropy.py` script:

```bash
python generateEntropy.py
```

This script will automatically download a frame from the Shibuya Crossing video stream, process the image to extract randomness, and print a 64-character alphanumeric code.

## Technical Details
### SHA-256 and Color Channels
The entropy extraction process uses the SHA-256 hashing algorithm to ensure a high degree of randomness. Here’s how we manage the image data:
- **Color Channels**: The image is fully processed in its RGB color spectrum to utilize all visual data. By incorporating each pixel's red, green, and blue values, we enhance the potential randomness derived from the dynamically chaotic scenes of Shibuya Crossing.
- **SHA-256 Hashing**: We convert the entire image into a byte array that includes all RGB values, then compute a SHA-256 hash. This hashing algorithm is key as it produces a fixed-size, 256-bit output, offering a robust foundation for cryptographic security. The resultant hash is encoded into a base64 string. From this string, we randomly select 32 characters to form the final alphanumeric code. This approach not only ensures that the code is URL-safe and uniformly formatted but also introduces an additional layer of randomness by varying the characters used in the final output.

## Youtube Video IDs

In `shibuyaStream.py`, you may use any youtube video ID. The following are three livestreams of Shibuya for examples:

```
Sky View: Tw2RYnTXuy8
Cam 1: RTwNEfirmks
Cam 2: Lfl2Nj_QRXU
```
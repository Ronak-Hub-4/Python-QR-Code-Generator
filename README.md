# Python QR Code Generator

A command-line Python tool that turns any URL into a QR code. Enter a link, and the script saves the QR code as a PNG and opens it automatically. It keeps asking for new links until you quit.

## Features

- Generates a QR code from any URL
- Saves the image as a PNG with a filename based on the URL
- Opens the QR code automatically in your default image viewer
- Adds `https://` automatically if you leave it out
- Rejects empty input and asks again
- Removes characters that are invalid in filenames (`/`, `:`, `?`, etc.)
- Keeps running after errors, so one bad input doesn't end the program
- Type `quit` to exit, or press `Ctrl+C`

## Requirements

- Python 3.8 or newer
- [qrcode](https://pypi.org/project/qrcode/) with Pillow

```bash
pip install "qrcode[pil]"
```

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. Run the script:

   ```bash
   python qr.py
   ```

3. Enter a URL when prompted:

   ```
   Enter the URL to generate QR code (or 'quit' to exit): www.linkedin.com/in/your-profile
   Saved as www.linkedin.com_in_your-profile_qr.png
   ```

4. The QR code opens in your image viewer. Enter another URL, or type `quit` to exit.

## How It Works

1. Reads the URL from user input and trims extra spaces.
2. Adds `https://` if the URL has no scheme, so phone scanners open it as a link.
3. Builds a safe filename by replacing invalid characters with underscores and limiting the name to 50 characters.
4. Generates the QR code with `qrcode.make()`, saves it as a PNG, and displays it.

## Troubleshooting

**`ModuleNotFoundError: No module named 'PIL'`**
Pillow isn't installed. Run `pip install pillow`, or reinstall with `pip install "qrcode[pil]"`.

**The image doesn't open automatically**
The QR code is still saved in the folder where you ran the script. Open the PNG manually.

## License

This project is licensed under the [MIT License](LICENSE).

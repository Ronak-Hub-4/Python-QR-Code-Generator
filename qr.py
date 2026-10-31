import re
import qrcode

while True:
    try:
        url = input("Enter the URL to generate QR code (or 'quit' to exit): ").strip()

        if url.lower() == 'quit':
            break

        if not url:
            print("Input can't be empty. Please try again.\n")
            continue

        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url

        # Turn the URL into a safe filename (removes characters like / : ? that Windows doesn't allow)
        name = re.sub(r'[^A-Za-z0-9._-]', '_', url.replace('https://', '').replace('http://', ''))
        filename = f"{name[:50]}_qr.png"

        img = qrcode.make(url)
        img.save(filename)
        print(f"Saved as {filename}\n")
        img.show()

    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
        break
    except Exception as e:
        print(f"An error occurred: {e}. Please try again.\n")

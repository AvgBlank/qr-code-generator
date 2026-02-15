from qrcodegen import QrCode
import argparse
import sys


def to_svg_str(qr: QrCode, border: int) -> str:
    """Returns a string of SVG code for an image depicting the given QR Code, with the given number
    of border modules. The string always uses Unix newlines (\n), regardless of the platform.
    """
    if border < 0:
        raise ValueError("Border must be non-negative")

    parts: list[str] = []
    for y in range(qr.get_size()):
        for x in range(qr.get_size()):
            if qr.get_module(x, y):
                parts.append(f"M{x+border},{y+border}h1v1h-1z")
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg xmlns="http://www.w3.org/2000/svg" version="1.1" viewBox="0 0 {qr.get_size()+border*2} {qr.get_size()+border*2}" stroke="none">
	<rect width="100%" height="100%" fill="#FFFFFF"/>
	<path d="{" ".join(parts)}" fill="#000000"/>
</svg>
"""


def print_qr(qrcode: QrCode, border: int) -> None:
    """Prints the given QrCode object to the console."""
    if border < 0:
        raise ValueError("Border must be non-negative")

    for y in range(-border, qrcode.get_size() + border):
        for x in range(-border, qrcode.get_size() + border):
            print("\u2588 "[1 if qrcode.get_module(x, y) else 0] * 2, end="")
        print()
    print()


def parse_ecc(level: str):
    levels = {
        "low": QrCode.Ecc.LOW,
        "medium": QrCode.Ecc.MEDIUM,
        "quartile": QrCode.Ecc.QUARTILE,
        "high": QrCode.Ecc.HIGH,
    }
    return levels[level.lower()]


def main():
    parser = argparse.ArgumentParser(
        description="Generate QR codes from text or URLs",
        epilog=f"""
Examples:
  {sys.argv[0]} "https://google.com" -p
  {sys.argv[0]} "hello world" -o qr.svg
  {sys.argv[0]} "data" -e low -b 4 -p
""",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("text", help="Text or URL to encode")
    parser.add_argument(
        "-e",
        "--ecc",
        choices=["low", "medium", "quartile", "high"],
        default="high",
        help="Error correction level (default: high)",
    )
    parser.add_argument(
        "-b", "--border", type=int, default=2, help="Border size (default: 2)"
    )
    parser.add_argument("-o", "--output", help="Output SVG file")
    parser.add_argument(
        "-p", "--print", action="store_true", help="Print ASCII QR code to terminal"
    )

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    args = parser.parse_args()

    qr = QrCode.encode_text(args.text, parse_ecc(args.ecc))

    # Print if (--print) is called or if nothing is specified
    if args.print or (not args.output and not args.print):
        print_qr(qr, args.border)

    # Save SVG if (--output) is called
    if args.output:
        svg = to_svg_str(qr, args.border)
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(svg)
        print(f"Saved SVG to {args.output}")


if __name__ == "__main__":
    main()

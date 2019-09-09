from PIL import Image
import argparse


def get_char(r, g, b, alpha=256):
    """ gary / 256 == x / len(ascii_char) """
    if alpha == 0:
        return " "
    gary = (2126 * r + 7152 * g + 722 * b) / 10000
    #print(gary)
    ascii_char = list("$@B%8&WM#*oahkbdpqwnZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.")

    x = int((gary / (alpha + 1.0)) * len(ascii_char))

    return ascii_char[x]


def write_file(out_file_name, content):
    with open(out_file_name, "w") as f:
        f.write(content)


def main(in_file_name="in_file", width=80, height=80, out_file_name="out_file"):
    text = ""
    img = Image.open(in_file_name)
    img = img.resize((width, height), Image.NEAREST)
    for i in range(height):
        for j in range(width):
            content = img.getpixel((j, i))
            text += get_char(*content)
            #print(content)
        text += "\n"
    write_file(out_file_name, text)


def parse_param():
    """para analyzer"""
    parser = argparse.ArgumentParser()
    # input_file
    parser.add_argument("input_file")
    parser.add_argument("out_file")

    parser.add_argument("width", type=int, default=80)
    parser.add_argument("height", type=int, default=80)

    args = parser.parse_args();
    in_file, out_file, width, height = args.input_file, args.out_file, args.width, args.height
    return in_file, out_file, width, height


if __name__ == '__main__':
    in_file, out_file, width, height = parse_param()
    main(in_file_name=in_file, out_file_name=out_file, width=width, height=height)

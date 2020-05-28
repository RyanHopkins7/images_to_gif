import imageio, os, sys, argparse

"""
Example usage: python3 images_to_gif.py <images_directory> <output_gif_file> -d='<duration_seconds>'
"""

def main(images_directory, output_gif_file, duration_seconds=0.02):
    """
    Converts all of the images in images_directory into a GIF in output_gif_file

    Args:
        images_directory (str): Directory where the images to be turned into a gif are stored
        output_gif_file (str): Location to save the output gif file
        duration_seconds (float, default=0.02): Duration of each frame in the output gif
    """
    with imageio.get_writer(output_gif_file, mode='I', duration=duration_seconds) as writer:
        dirpath, _, filenames = next(os.walk(images_directory))
        for i, filename in enumerate(filenames):
            try:
                image = imageio.imread(f'{dirpath}/{filename}')
                writer.append_data(image)
            except ValueError:
                print(f'{filename} is not a valid image')
            print(f'Generating gif file {i/len(filenames)*100:.2f}%', end='\r')


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument('images_directory', help="Directory where the images to be turned into a gif are stored")
    ap.add_argument('output_gif_file', help="Location to save the output gif file")
    ap.add_argument("-d", "--duration", type=float, help="Duration of each frame in the output gif")
    args = vars(ap.parse_args())

    main(*args.values())

import os


def zip_dataset(path, zip_file):
    """
    Writes all content of a dataset to a zip file.

    by Jonathan Schilling

    :param path: Path to the source  directory to be zipped
    :param zip_file: Target zip file object where the data will be written
    :return: None
    """
    for root, dirs, files in os.walk(path):
        for file in files:
            src_path = root + '/' + file
            dest_path = root.replace(str(path), '') + '/' + file

            zip_file.write(src_path, dest_path)

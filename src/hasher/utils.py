import os
import hashlib
from pathlib import Path
from functools import partial


def hash_file(file, block_size: int = 65536) -> str:

    hasher = hashlib.md5()
    for bufffer in iter(partial(file.read, block_size), b''):
        hasher.update(bufffer)

    return hasher.hexdigest()


def handle_uploaded_file(file) -> str:
    md5_hash = hash_file(file)

    catalog = md5_hash[:2]
    filepath = "./store/{}".format(md5_hash[:2])

    ext = os.path.splitext(file.name)[1]

    Path(filepath).mkdir(parents=True, exist_ok=True)

    with open('{}/{}{}'.format(filepath, md5_hash, ext), 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    return md5_hash

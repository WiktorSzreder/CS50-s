def main():
    filmeName = input("File name: ").strip().lower()
    ext = filmeName.rsplit(".", 1)[1]

    types = {
        "gif": "image/gif",
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "png": "image/png",
        "pdf": "application/pdf",
        "txt": "text/plain",
        "zip": "application/zip",
    }


    print(types.get(ext, "application/octet-stream"))



main()
import threading
import urllib.request


def download_file(url: str, filename: str):
    print(f"\nDownloading {filename} from {url}...")
    _, _ = urllib.request.urlretrieve(url, filename)
    print(f"\n{filename} downloaded successfully.")


files_to_download = [
    {"url": "https://www.dundeecity.gov.uk/sites/default/files/publications/civic_renewal_forms.zip",
     "filename": "/home/skartavykh/MyProjects/concurrency/threads_exercises/file1"},
    {"url": "https://github.com/yourkin/fileupload-fastapi/raw/a85a697cab2f887780b3278059a0dd52847d80f3/tests/data"
            "/test-5mb.bin",
     "filename": "/home/skartavykh/MyProjects/concurrency/threads_exercises/file2"},
    {"url": "https://github.com/yourkin/fileupload-fastapi/raw/a85a697cab2f887780b3278059a0dd52847d80f3/tests/data"
            "/test-10mb.bin",
     "filename": "/home/skartavykh/MyProjects/concurrency/threads_exercises/file3"}
]

threads = []

for file_info in files_to_download:
    thread = threading.Thread(target=download_file,
                              args=(file_info["url"], file_info["filename"]))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

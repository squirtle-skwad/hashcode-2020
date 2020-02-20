import os


OUTPUT_FILE_PATH = os.path.abspath('./output.txt')


def write_to_output_file(libraries):
    with open(OUTPUT_FILE_PATH, 'w') as output_file:
        no_of_libraries = len(libraries)
        output_file.write(str(no_of_libraries) + '\n\n')

        for library in libraries:
            library_id = library["lib_id"]
            no_of_books = len(library["books_order"])

            output_file.write(str(library_id) + " " + str(no_of_books) + "\n")

            books_order_str = ""
            for book in library["books_order"]:
                books_order_str += str(book) + " "
            books_order_str.rstrip()

            output_file.write(str(books_order_str) + "\n\n")


if __name__ == "__main__":
    libraries = [
        {
            "lib_id": 1,
            "books_order": [0,1,2,3,4]
        },
        {
            "lib_id": 2,
            "books_order": [5,6,7]
        }
    ]

    write_to_output_file(libraries)
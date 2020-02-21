OUTPUT_FILE_PATH = './d_output.txt'

def write_to_output_file(library_list):
    with open(OUTPUT_FILE_PATH, 'w') as output_file:
        output_file.write(str(len(library_list)) + '\n')

        for library in library_list:
            library_id = library["lib_id"]
            num_books = len(library["books_order"])

            output_file.write(f"{library_id} {num_books}\n")
            
            books_order_str = ' '.join(map(str, library["books_order"]))
            output_file.write(books_order_str + "\n")
from includes.reverse_index.reverse_index import *
import sys

BOOKS_PATH = "includes/database/books"
EXTRACT_FILE_PATH = "includes/database/books/data.json"
COMPRESS_FILENAME = "compressRI.pkl"
UNCOMPRESS_FILENAME = "uncompressRI.pkl"
 
if __name__ == "__main__":
    
    if len(sys.argv) > 1 and sys.argv[1] == "--save-indexes":
        # without compression
        #ri = ReverseIndex(BOOKS_PATH, EXTRACT_FILE_PATH, False)
        #ReverseIndex.save(ri, BOOKS_PATH + '/' + UNCOMPRESS_FILENAME)

        # with compression
        ri2 = ReverseIndex(BOOKS_PATH, EXTRACT_FILE_PATH, True)
        ReverseIndex.save(ri2, BOOKS_PATH + '/' + COMPRESS_FILENAME)
    

    if len(sys.argv) > 1 and sys.argv[1] == "--load-indexes":
        # without compression
        #ri = ReverseIndex.load(BOOKS_PATH + '/' + UNCOMPRESS_FILENAME)
        #print(ri.get_postings_dict())
        #print(ri.does_compression())
        #print(ri.get_document_map())
        
        # with compression
        ri2 = ReverseIndex.load(BOOKS_PATH + '/' + COMPRESS_FILENAME)
        print(ri2.get_postings_dict())
        print(ri2.does_compression())
        print(ri2.get_document_map())
import os 
import sys
import glob

def get_foldersd():
    # This function returns the list of folders
    # in the current directory.
    items = glob.glob(os.path.join("", "*"))
    folders_list = [item for item in items if os.path.isdir(item)]
    return folders_list


def extract_chats():
    # This function extract chats from the 
    # text file and save it in a csv file.
    # Text file path 

    folder_list = glob.glob(os.path.join("", "*"))
    print(folder_list)

if __name__ == '__main__':
    extract_chats()










# import os
# import sys
# import glob
# import PyPDF2


# def extract_and_save():
#     # This function extract data from the 
#     # pdf files and save it in a text file.
#     script_path = "marvel_dataset/"
#     file_list = glob.glob(os.path.join(script_path, "*"))
#     # Text folder path 
#     txt_file_path = "marvel_dataset_txt/"
#     if os.path.exists(txt_file_path):
#         pass
#     else:
#         os.mkdir(txt_file_path)
#     # Check text file path exists or not
#     if os.path.exists(txt_file_path+"marvel_dataset.txt"):
#         pass
#     else:
#         # create a text file 
#         text_file = open(txt_file_path+"marvel_dataset.txt", "w")
#         text_file.close()
#     # iterate over the pdf files
#     for file_path in file_list:
#         # Open the Text file
#         text_file = open(txt_file_path+"marvel_dataset.txt", "a")
#         movie_script = ""
#         # open the pdf file
#         pdf_file = open(file_path, 'rb')
#         # create pdf reader object 
#         reader = PyPDF2.PdfReader(pdf_file)
#         # Get the number of pages in pdf file
#         num_pages = len(reader.pages)
#         # iterate over the pages of pdf file
#         for i in range(len(reader.pages)):
#             # get current page
#             page = reader.pages[i]
#             # extract text from the current page
#             text = page.extract_text()
#             # encode the text
#             text = text.encode('utf-8')
#             # append the text to the movie_script
#             movie_script += str(text)
#         # write the movie_script to the text file
#         text_file.write(movie_script)
#         # close the pdf file
#         pdf_file.close()
#         # close the text file
#         text_file.close()
#         # delete active objects
#         del reader, movie_script, text, text_file
#         # print the file name and number of pages
#         print(str(pdf_file), num_pages)
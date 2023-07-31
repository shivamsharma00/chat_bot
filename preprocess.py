# This script takes whatsapp chat text file and convert it into a json file to train LLM.
import os 
import sys
import glob
import json
import re
import emoji



def get_folders():
    # This function returns the list of folders
    # in the current directory.
    items = glob.glob(os.path.join("chats/", "*"))
    folders_list = [item for item in items if os.path.isdir(item)]
    return folders_list

def make_json(input_user_message, output_user_message):
    instructions = "Write the reply for this message, using the context of the conversation."
    return [
                    {
                        "instruction": instructions,
                        "input": input_user_message,
                        "output": output_user_message
                    }
    ]

def preprocess(text):
    # Preprocess the text
        
    pattern = re.compile(r'https?://\S+')
    try:
        text = pattern.sub(' ', text)
        text.strip()
        text = emoji.demojize(text)
        text = text.replace('\\n', '')
        
        text = text.replace('\u2019', '`')
        text = text.replace('\u2026', '`')
        text = text.replace('\u200e', '')
        text = text.replace('\u2022', '')
        text = text.replace('\u092c', '')
        text = text.replace('\u0947', '')
        text = text.replace('\u091f', '')
        text = text.replace('\u0947', '')
        text = text.replace('Messages and calls are end-to-end encrypted. No one outside of this chat, not even WhatsApp, can read or listen to them.', '')
        text = text.replace('image omitted', '')

    except:
        pass
    return text

def get_chat_list(chat):
    # this function makes JSON files from the chats
    chat_list = []
    
    dateRegex = r"[\d]{1,2}/[\d]{1,2}/[\d]{2}"
    timeRegex = r"[\d]{1,2}:[\d]{1,2}:[\d]{1,2} (AM|PM)"
    messageRegex = dateRegex+', '+timeRegex
    input_user_message = ""
    output_user_message = ""
    input_user_flag = False

    for line in chat:
        # print(line)
        # We will remove the date and time from the line
        try:
            message_start_index = re.search(messageRegex, line).span()[1]
        except:
            continue
        line = line.strip()
        line = preprocess(line[message_start_index:])
        # check if the sender is the shivam sharma
        check_user = re.search(r"Shivam Sharma", line)

        # below condition will convert chat into pair of message and reply format
        if check_user == None:
            # After each pair of chat, we will append it to the chat_list
            if input_user_flag:
                input_user_flag = False
                chat_list.extend(make_json(input_user_message, output_user_message))
                input_user_message = ""
                output_user_message = ""

            input_user_message += line[line.index(':')+2:]
        else:
            output_user_message += line[line.index(':')+2:]
            input_user_flag = True
        
    return chat_list

def extract_chats():
    # This function extract chats from the 
    # text file and save it in a csv file.
    # Text file path
    chat_file_name = "_chat.txt" 
    folders = get_folders()

    chat_dataset = []

    for folder in folders:
        try:
            chatfile = os.path.join(folder, chat_file_name)
            chat = open(chatfile, encoding="utf-8")
        except:
            print("Wrong file extension")

        chat_dataset.extend(get_chat_list(chat))
    return chat_dataset

def train_test_vali(chat_dataset):
    # This function split the dataset into train, test and validation set
    # and save it in a json file.
    train = chat_dataset[:int(0.9*len(chat_dataset))]
    test = chat_dataset[int(0.8*len(chat_dataset)):int(0.9*len(chat_dataset))]
    vali = chat_dataset[int(0.9*len(chat_dataset)):]

    return train, test, vali

if __name__ == '__main__':

    train, test, vali = train_test_vali(extract_chats())
    with open("chats/chat_train_dataset.json", "w") as f:
        json.dump(train, f, indent=3)
    # with open("chats/chat_test_dataset.json", "w") as f:
    #     json.dump(test, f, indent=3)
    with open("chats/chat_vali_dataset.json", "w") as f:
        json.dump(vali, f, indent=3)




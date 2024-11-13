import glob
import os

def open_file_location(file_path):
    print(f"File found! You can access it here: {file_path}")
    
    folder_path = os.path.dirname(file_path)
    os.startfile(folder_path)

def find_file(file_name):
    file_name += '.txt'
    current_directory = os.getcwd()
    
    txt_files = glob.glob(current_directory + "/*.txt")

    for file_path in txt_files:
        if os.path.basename(file_path) == file_name:
            open_file_location(file_path)
            break
    else:
        print("File not found.")

def load_words_from_file(file_path):
    stop_words = set()
    with open(file_path, 'r') as file:
        for line in file:
            stop_word = line.strip().lower()
            if stop_word:
                stop_words.add(stop_word)
    return stop_words

def get_base_word(word):

    global prefixes
    global suffixes

    for prefix in prefixes:
        if word.startswith(prefix) and len(word) > len(prefix):
            word = word[len(prefix):]
            break

    for suffix in suffixes:
        if word.endswith(suffix) and len(word) > len(suffix):
            word = word[:-len(suffix)]
            break

    return word

def remove_punctuation(word):
    punctuation = ".,?!()"
    cleaned_word = ""
    
    for char in word:
        if char not in punctuation:
            cleaned_word += char
    
    return cleaned_word

def createIndex():
    stop_words_file = "stop_words.txt"
    prefixes_file = "prefixes.txt"
    suffixes_file = "suffixes.txt"
    stop_words = load_words_from_file(stop_words_file)
    global prefixes
    prefixes = load_words_from_file(prefixes_file)
    global suffixes
    suffixes = load_words_from_file(suffixes_file)

    documents_folder = "Browsing/"
    
    file_names = []
    txt_files = glob.glob(documents_folder + "*.txt")

    for file_path in txt_files:
        file_name_only = os.path.basename(file_path)
        file_names.append(file_name_only)

    index_dict = {}

    for file_name in file_names:
        file_path = os.path.join(documents_folder, file_name)
        with open(file_path, 'r') as file:
            lines = file.readlines()

            for line_num, line in enumerate(lines, start=1):
                words = line.split()

                for word in words:
                    clean_word = remove_punctuation(word).lower()

                    if clean_word in stop_words or not clean_word:
                        continue

                    base_word = get_base_word(clean_word)

                    if base_word not in index_dict:
                        index_dict[base_word] = {file_name: {'count': 1, 'lines': [line_num]}}
                    else:
                        if file_name not in index_dict[base_word]:
                            index_dict[base_word][file_name] = {'count': 1, 'lines': [line_num]}
                        else:
                            index_dict[base_word][file_name]['count'] += 1
                            if line_num not in index_dict[base_word][file_name]['lines']:
                                index_dict[base_word][file_name]['lines'].append(line_num)


    file_names = [file_name.replace('.txt', '') for file_name in file_names]
    
    return file_names, index_dict

def searchByDocumentContent(index_dict):

    global prefixes
    global suffixes

    query = input('Input Search Word in files: ')
    query = query.lower()
    full_query_words = query.split()
    query_words = []

    for w in full_query_words:
        query_words.append(get_base_word(w, prefixes, suffixes))

    files = []
    counts = []
    lines = []

    for word in query_words:
        if word in index_dict:
            for file_name, data in index_dict[word].items():
                if file_name in files:
                    file_index = files.index(file_name)
                    counts[file_index] += data['count']
                    lines[file_index].extend(data['lines'])
                else:
                    files.append(file_name)
                    counts.append(data['count'])
                    lines.append(data['lines'])

    if len(files) > 0:
        combined = list(zip(files, counts, lines))
        combined.sort(key=lambda x: x[1], reverse=True)

        files, counts, lines = zip(*combined)
        files = list(files)
        counts = list(counts)
        lines = list(lines)

        print('')
        print('files               lines')
        print('')
        for i in range(0,len(files)):
            print(f'{files[i]}              {lines[i]}')
    else:
        print('Query not Found!')

def searchByDocumentName(file_names):
    query = input('Search file: ')
    if query in file_names:
        find_file(query)
    else:
        print('File does not exist')

def menu():

    browserName()
    print('            Menu')
    print('')
    print('1. Refresh Indexer Manually')
    print('2. Search by Document Name')
    print('3. Search by Document Content')
    print('4. Exit Browser')
    print('')

    while(True):

        option = input('Choose an option from above: ')

        try:
            option = int(option)
            if 0 < option < 5:
                break
            else:
                print("Invalid choice! Choose carefully from the menu.")
                print('')
                continue
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            print('')
            continue

    return option

def browserName():
    print('                 ******************************************')
    print('                 *                                        *')
    print('                 *                My Browser              *')
    print('                 *                                        *')
    print('                 ******************************************')
    print('')

def main():
    file_names, index_dict = createIndex()

    # print(index_dict.keys())

    while(True):
        os.system('cls')

        option = menu()

        if option == 1:
            file_names, index_dict = createIndex()
            print('Indexer Refreshed Successfully!')
        elif option == 2:
            searchByDocumentName(file_names)
        elif option == 3:
            searchByDocumentContent(index_dict)
        else:
            break

        print('')
        input('Press Enter to continue.')

    os.system('cls')
    browserName()
    print('')
    print('Thank You for using "My Browser"')
    print('')

if __name__ == "__main__":
    main()

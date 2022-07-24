from translate import Translator


try:
    with open('test.txt', mode='r') as my_file:
        print(my_file.read())
        my_file.seek(0)
        translator = Translator(to_lang="ja")
        translation = translator.translate(my_file.read())
        with open('test.txt', 'a', encoding="utf-8") as my_file2:
            my_file2.write("\n")
            my_file2.write(translation)
        
        
except FileNotFoundError as e:
    print("check your file!")

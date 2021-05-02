def select_lang():
    print('デコードする言語を選択してください(日本語(かな): ja /英語: en)')
    lang = input()
    if lang == 'en':
        english = {
            'language': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
            'length': 26
        }
        return english
    elif lang == 'ja':
        japanease = {
            'language': ["あ","い","う","え","お","か","き","く","け","こ","さ","し","す","せ","そ","た","ち","つ","て","と","な","に","ぬ","ね","の","は","ひ","ふ","へ","ほ","ま","み","む","め","も","や","ゆ","よ","ら","り","る","れ","ろ","わ","を","ん"],
            'length': 50
        }
        return japanease
    else :
        error = {
            'error': '指定外の文字が入力されました。'
        }
        return error

def reset_counter(default_number, limit_number):
    if default_number > limit_number:
        return default_number - limit_number - 1
    else:
        return default_number

def search(text, difference, lang_info):
    decode_text = ''
    text_list = list(text)
    for i in text_list:
        for j_index, j_item in enumerate(lang_info['language']):
            if i == j_item:
                decode_text += lang_info['language'][reset_counter(j_index + difference, lang_info['length'] - 1)]
    return decode_text

def main():
    input_language = select_lang()

    if 'error' in input_language.keys() == True:
        exit

    print('デコードする文字列を入力してください。')
    rot13_text = input()

    for k in range(1, input_language['length']):
        print(str(k) + '文字ずらし\n')
        print(search(rot13_text, k, input_language) + '\n')
        print('-----------------------------------------------------------------------')

main()
                
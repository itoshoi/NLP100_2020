import NLP100_27
import re

def get_template_no_mediawiki_markup():
    dict = NLP100_27.get_template_no_emphasis_markup()
    dict = remove_file_markup(dict)
    dict = remove_template_lang(dict)
    dict = remove_ref(dict)
    dict = remove_external_link(dict)
    return dict

def remove_file_markup(dict):
    for k, v in dict.items():
        # ファイルの除去
        p = re.compile(r'''
            \[\[            # [[からスタート
            ファイル:       # ファイルの文字列
            ([^|]*?)       # (|を含まない文字列) の繰り返し (url)
            (\|[^|]*?)?     # |と(|を含まない文字列)| の繰り返し (thumb)
            (\|[^|]*?)?     # |を含まない文字列(非貪欲) (説明文)
            \]\]            # ]]で終わり
        ''', re.MULTILINE + re.VERBOSE)
        dict[k] = p.sub(r'\3', v)
    return dict

def remove_template_lang(dict):
    for k, v in dict.items():
        p = re.compile(r'''
            \{\{
            lang        # langで始まる
            \|.*?        # |文字列 (言語タグ)
            \|(.*?)      # |文字列
            \}\}
        ''', re.MULTILINE + re.VERBOSE)
        dict[k] = p.sub(r'\1', v)
    return dict

def remove_ref(dict):
    for k, v in dict.items():
        p = re.compile(r'''
            \<
            \/?         # /が0か1回
            [ref|br]    # refかbrが出現
            .*?         # 文字列
            \>          # >で終わる
        ''', re.MULTILINE + re.VERBOSE)
        dict[k] = p.sub('', v)
    return dict

def remove_external_link(dict):
    for k, v in dict.items():
        # 外部リンクの除去 []ありの場合
        p1 = re.compile(r'''
            (\[             # [からスタート(明示的な場合)
            http            # httpから始まる
            .*?             # 文字列
            (\s(.*?))?a     # 空白+文字列 (表示文字)
            \])             #]でおわり(明示的な場合)
        ''', re.MULTILINE + re.VERBOSE)
        dict[k] = p1.sub(r'\2', v)
        
        p2 = re.compile(r'''
            http.*?([\s\|])   # httpから始まって空白か|が来るまでの文字列  
        ''', re.MULTILINE + re.VERBOSE)
        dict[k] = p2.sub('', dict[k])
    return dict


if __name__ == "__main__":
    dict = get_template_no_mediawiki_markup()
    for k, v in dict.items():
        print('{key}: {value}'.format(key=k, value=v))
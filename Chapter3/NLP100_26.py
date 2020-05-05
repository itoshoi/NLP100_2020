import re
import NLP100_25


def get_template_no_emphasis():
    dict = NLP100_25.get_template_dict()
    for k, v in dict.items():
        p = re.compile(r'\'{2,5}', re.MULTILINE)
        dict[k] = p.sub('', v)
    return dict


if __name__ == "__main__":
    dict = get_template_no_emphasis()
    for k, v in dict.items():
        print('{key}: {value}'.format(key=k, value=v))

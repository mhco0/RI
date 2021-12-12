from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup
from utils import Utils
import re
import unidecode
# Remove stopwords
import nltk
from mutual_information import MutualInformation
nltk.download('punkt')

nltk.download('stopwords')

BOOKS_PATH = '../books/'
DOMAINS = ['americanas', 'cultura', 'curitiba', 'magazine',
           'mercadoLivre', 'saraiva', 'shoptime', 'submarino', 'travessa', 'vila']


def tokenize(text):
    soup = BeautifulSoup(text, 'html.parser')

    for script in soup(["script", "style"]):
        script.extract()    # rip it out
    html_text = soup.get_text(' ')

    # change characters
    html_text = unidecode.unidecode(html_text)

    # Substitute point and go to lower case

    html_text = re.sub('[^A-Za-z]', ' ', html_text)
    html_text = html_text.lower()

    # tokenize
    tokenized_text = word_tokenize(html_text)
    for word in tokenized_text:
        if word in stopwords.words('portuguese'):
            tokenized_text.remove(word)

    # text = " ".join(tokenized_text)

    return tokenized_text


def pageToResult(page: str):
    url = Utils.regexSearch('saved from url=\(\d\d\d\d\)(.+?) -->', page)
    soup = BeautifulSoup(page, 'html.parser')
    head = soup.head

    title = head.title
    description = ''
    if title:
        title = title.text
    else:
        'Sem Titulo'
    metas = head.find_all('meta')
    for meta in metas:
        if meta.has_attr('name'):
            if meta['name'] == 'description':
                description = meta['content']
                break

    return [title, description, url]


paths = {
    0: "../books/americanas/1.html",
    1: "../books/americanas/10.html",
    2: "../books/americanas/2.html",
    3: "../books/americanas/3.html",
    4: "../books/americanas/4.html",
    5: "../books/americanas/5.html",
    6: "../books/americanas/6.html",
    7: "../books/americanas/7.html",
    8: "../books/americanas/8.html",
    9: "../books/americanas/9.html",
    10: "../books/cultura/1.html",
    11: "../books/cultura/10.html",
    12: "../books/cultura/2.html",
    13: "../books/cultura/3.html",
    14: "../books/cultura/4.html",
    15: "../books/cultura/5.html",
    16: "../books/cultura/6.html",
    17: "../books/cultura/7.html",
    18: "../books/cultura/8.html",
    19: "../books/cultura/9.html",
    20: "../books/curitiba/1.html",
    21: "../books/curitiba/10.html",
    22: "../books/curitiba/2.html",
    23: "../books/curitiba/3.html",
    24: "../books/curitiba/4.html",
    25: "../books/curitiba/5.html",
    26: "../books/curitiba/6.html",
    27: "../books/curitiba/7.html",
    28: "../books/curitiba/8.html",
    29: "../books/curitiba/9.html",
    30: "../books/magazine/1.html",
    31: "../books/magazine/10.html",
    32: "../books/magazine/2.html",
    33: "../books/magazine/3.html",
    34: "../books/magazine/4.html",
    35: "../books/magazine/5.html",
    36: "../books/magazine/6.html",
    37: "../books/magazine/7.html",
    38: "../books/magazine/8.html",
    39: "../books/magazine/9.html",
    40: "../books/mercadoLivre/1.html",
    41: "../books/mercadoLivre/10.html",
    42: "../books/mercadoLivre/2.html",
    43: "../books/mercadoLivre/3.html",
    44: "../books/mercadoLivre/4.html",
    45: "../books/mercadoLivre/5.html",
    46: "../books/mercadoLivre/6.html",
    47: "../books/mercadoLivre/7.html",
    48: "../books/mercadoLivre/8.html",
    49: "../books/mercadoLivre/9.html",
    50: "../books/saraiva/1.html",
    51: "../books/saraiva/10.html",
    52: "../books/saraiva/2.html",
    53: "../books/saraiva/3.html",
    54: "../books/saraiva/4.html",
    55: "../books/saraiva/5.html",
    56: "../books/saraiva/6.html",
    57: "../books/saraiva/7.html",
    58: "../books/saraiva/8.html",
    59: "../books/saraiva/9.html",
    60: "../books/shoptime/1.html",
    61: "../books/shoptime/10.html",
    62: "../books/shoptime/2.html",
    63: "../books/shoptime/3.html",
    64: "../books/shoptime/4.html",
    65: "../books/shoptime/5.html",
    66: "../books/shoptime/6.html",
    67: "../books/shoptime/7.html",
    68: "../books/shoptime/8.html",
    69: "../books/shoptime/9.html",
    70: "../books/submarino/1.html",
    71: "../books/submarino/10.html",
    72: "../books/submarino/2.html",
    73: "../books/submarino/3.html",
    74: "../books/submarino/4.html",
    75: "../books/submarino/5.html",
    76: "../books/submarino/6.html",
    77: "../books/submarino/7.html",
    78: "../books/submarino/8.html",
    79: "../books/submarino/9.html",
    80: "../books/travessa/1.html",
    81: "../books/travessa/10.html",
    82: "../books/travessa/2.html",
    83: "../books/travessa/3.html",
    84: "../books/travessa/4.html",
    85: "../books/travessa/5.html",
    86: "../books/travessa/6.html",
    87: "../books/travessa/7.html",
    88: "../books/travessa/8.html",
    89: "../books/travessa/9.html",
    90: "../books/vila/1.html",
    91: "../books/vila/10.html",
    92: "../books/vila/2.html",
    93: "../books/vila/3.html",
    94: "../books/vila/4.html",
    95: "../books/vila/5.html",
    96: "../books/vila/6.html",
    97: "../books/vila/7.html",
    98: "../books/vila/8.html",
    99: "../books/vila/9.html",
    100: "../books/americanas/1.html",
    101: "../books/americanas/10.html",
    102: "../books/americanas/2.html",
    103: "../books/americanas/3.html",
    104: "../books/americanas/4.html",
    105: "../books/americanas/5.html",
    106: "../books/americanas/6.html",
    107: "../books/americanas/7.html",
    108: "../books/americanas/8.html",
    109: "../books/americanas/9.html",
    110: "../books/cultura/1.html",
    111: "../books/cultura/10.html",
    112: "../books/cultura/2.html",
    113: "../books/cultura/3.html",
    114: "../books/cultura/4.html",
    115: "../books/cultura/5.html",
    116: "../books/cultura/6.html",
    117: "../books/cultura/7.html",
    118: "../books/cultura/8.html",
    119: "../books/cultura/9.html",
    120: "../books/curitiba/1.html",
    121: "../books/curitiba/10.html",
    122: "../books/curitiba/2.html",
    123: "../books/curitiba/3.html",
    124: "../books/curitiba/4.html",
    125: "../books/curitiba/5.html",
    126: "../books/curitiba/6.html",
    127: "../books/curitiba/7.html",
    128: "../books/curitiba/8.html",
    129: "../books/curitiba/9.html",
    130: "../books/magazine/1.html",
    131: "../books/magazine/10.html",
    132: "../books/magazine/2.html",
    133: "../books/magazine/3.html",
    134: "../books/magazine/4.html",
    135: "../books/magazine/5.html",
    136: "../books/magazine/6.html",
    137: "../books/magazine/7.html",
    138: "../books/magazine/8.html",
    139: "../books/magazine/9.html",
    140: "../books/mercadoLivre/1.html",
    141: "../books/mercadoLivre/10.html",
    142: "../books/mercadoLivre/2.html",
    143: "../books/mercadoLivre/3.html",
    144: "../books/mercadoLivre/4.html",
    145: "../books/mercadoLivre/5.html",
    146: "../books/mercadoLivre/6.html",
    147: "../books/mercadoLivre/7.html",
    148: "../books/mercadoLivre/8.html",
    149: "../books/mercadoLivre/9.html",
    150: "../books/saraiva/1.html",
    151: "../books/saraiva/10.html",
    152: "../books/saraiva/2.html",
    153: "../books/saraiva/3.html",
    154: "../books/saraiva/4.html",
    155: "../books/saraiva/5.html",
    156: "../books/saraiva/6.html",
    157: "../books/saraiva/7.html",
    158: "../books/saraiva/8.html",
    159: "../books/saraiva/9.html",
    160: "../books/shoptime/1.html",
    161: "../books/shoptime/10.html",
    162: "../books/shoptime/2.html",
    163: "../books/shoptime/3.html",
    164: "../books/shoptime/4.html",
    165: "../books/shoptime/5.html",
    166: "../books/shoptime/6.html",
    167: "../books/shoptime/7.html",
    168: "../books/shoptime/8.html",
    169: "../books/shoptime/9.html",
    170: "../books/submarino/1.html",
    171: "../books/submarino/10.html",
    172: "../books/submarino/2.html",
    173: "../books/submarino/3.html",
    174: "../books/submarino/4.html",
    175: "../books/submarino/5.html",
    176: "../books/submarino/6.html",
    177: "../books/submarino/7.html",
    178: "../books/submarino/8.html",
    179: "../books/submarino/9.html",
    180: "../books/travessa/1.html",
    181: "../books/travessa/10.html",
    182: "../books/travessa/2.html",
    183: "../books/travessa/3.html",
    184: "../books/travessa/4.html",
    185: "../books/travessa/5.html",
    186: "../books/travessa/6.html",
    187: "../books/travessa/7.html",
    188: "../books/travessa/8.html",
    189: "../books/travessa/9.html",
    190: "../books/vila/1.html",
    191: "../books/vila/10.html",
    192: "../books/vila/2.html",
    193: "../books/vila/3.html",
    194: "../books/vila/4.html",
    195: "../books/vila/5.html",
    196: "../books/vila/6.html",
    197: "../books/vila/7.html",
    198: "../books/vila/8.html",
    199: "../books/vila/9.html"
}

print('getting text...')
results = {}
for id, path in paths.items():
    page = Utils.readFile(path)
    result = pageToResult(page)
    results[id] = result

print('writting text...')
Utils.writeJsonFile('./results.json', results)

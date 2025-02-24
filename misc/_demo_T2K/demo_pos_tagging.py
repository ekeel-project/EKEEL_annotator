import requests
import argparse
import time
import os

SERVER_PATH = "http://api.italianlp.it"


def load_document(text, async_call):
    r = requests.post(SERVER_PATH + '/documents/',
                      data={'text': text,  # si carica il documento nel server
                            'lang': 'IT',
                            'async': async_call})  # indica se la chiamata alle api viene fatta in modo sincrono o asincrono

    doc_id = r.json()['id']  # questo è l'id del documento nel server

    return doc_id


def wait_for_pos_tagging(doc_id):
    page = 1
    # inizializzazione dummy della risposta del server per poter scrivere la condizione del while
    api_res = {'postagging_executed': False, 'sentences': {'next': False, 'data': []}}
    while not api_res['postagging_executed'] or api_res['sentences']['next']:
        r = requests.get(SERVER_PATH + '/documents/details/%s?page=%s' % (doc_id, page))
        api_res = r.json()

        if not api_res['postagging_executed']:
            print('Waiting for pos tagging...')
            time.sleep(1)
            continue
        else:
            api_res.pop("sentiment_executed")
            api_res.pop("sentiment_negative_probability")
            api_res.pop("sentiment_neutral_probability")
            api_res.pop("sentiment_positive_negative_probability")
            from pprint import pprint
            pprint(api_res)
            import json
            with open("res.json","w") as f:
                json.dump(api_res,f,indent=4)
            

        if api_res['sentences']['next']:
            page += 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_directory',
                        help='Percorso della cartella contenente i file da annotare.')
    parser.add_argument('-o', '--output_path', default='ids.txt',
                        help='Percorso del file su cui salvare gli id dei file annotati.')
    parser.add_argument('-a', '--async_call', action='store_true',
                        help='Flag che indica se eseguire la chiamata alle API in modo asincrono.')
    args = parser.parse_args()

    with open(args.output_path, 'w') as out_file:
        for file_name in os.listdir(args.input_directory):
            src_path = os.path.join(args.input_directory, file_name)
            with open(src_path, 'r') as src_file:
                text = src_file.read()
                print(args.async_call)
                doc_id = load_document(text, args.async_call)
                if args.async_call:
                    wait_for_pos_tagging(doc_id)  # ci assicuriamo che l'annotazione linguisica sia conclusa
                out_file.write(f'{doc_id}\n')


if __name__ == '__main__':
    #main()
    text = "Buongiorno Oggi vi presento la mia famiglia Io sono il padre mi chiamo Gennaro Pirlo ho trentasette anni e lavoro come scrittore e giornalista da quando ne avevo venti"
    #doc_id = load_document(text, True)
    #print(doc_id)
    wait_for_pos_tagging(1729)
import requests
import argparse
import time

SERVER_PATH = "http://api.italianlp.it"


def execute_term_extraction(doc_ids, configuration=None):
    configuration = {
        'pos_start_term': ['c:S'],
        'pos_internal_term': ['c:S'],
        'pos_end_term': ['c:S'],
        'max_length_term': 5
    }
    configuration = {}
    if configuration is None:
        response = requests.post(SERVER_PATH + '/documents/term_extraction',
                                 # richiesta al server di fare la term extraction su una lista di id
                                 json={'doc_ids': doc_ids})
    else:
        response = requests.post(SERVER_PATH + '/documents/term_extraction',
                                 # richiesta al server di fare la term extraction su una lista di id
                                 json={'doc_ids': doc_ids,
                                       'configuration': configuration})
    term_extraction_id = response.json()['id']  # id dove controllare se l'operazione è conclusa
    while True:
        r = requests.get(SERVER_PATH + '/documents/term_extraction',
                         {'id': term_extraction_id})
        res = r.json()
        print('Waiting for results...')
        if res['status'] == "OK":  # se lo status è OK significa che l'estrazione terminologica è completata
            return res["terms"]  # altrimenti si fa uno sleep di un secondo prima di controllare nuovamente
        time.sleep(5)

def get_similarity(doc_ids):
    response = requests.get(SERVER_PATH + "/documents/similarity",
                             params= {"doc_id_1":doc_ids[0], 
                                    "doc_id_2":doc_ids[1]})
    print(response.json())

from pprint import pprint
import pandas as pd
terms = pd.DataFrame(execute_term_extraction([1570])).sort_values(by='domain_relevance', ascending=False)
#terms = terms[terms["frequency"] > 1]
print(terms)
#get_similarity([1424, 1425])

def load_document_ids(src_path):  # caricamento della lista degli id (sul server) dei tweet di un file
    server_ids = []
    for line in open(src_path):
        server_ids.append(int(line.strip()))
    return server_ids


def write_results(result, out_path):
    with open(out_path, 'w+') as out_file:
        out_file.write('term\tdomain_relevace\tfrequency\n')
        for term_dict in result['terms']:
            info = [str(term_dict[key]) for key in term_dict]
            out_file.write('\t'.join(info) + '\n')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--ids_file',
                        help='Percorso del file contenente gli id dei documenti su cui fare l\'estrazione terminologica.')
    parser.add_argument('-o', '--output_file', default='terms.txt',
                        help='Percorso del file in cui salvare i risultati dell\'estrazione terminologica.')

    args = parser.parse_args()

    # configuration = None       # se configuration è None utilizza quella di default
    configuration = {
        'pos_start_term': ['c:S'],
        'pos_internal_term': ['c:S'],
        'pos_end_term': ['c:S'],
        'max_length_term': 1
    }

    document_ids = load_document_ids(args.ids_file)  # carichiamo gli id dei documenti annotati dal file
    print(document_ids)
    terms = execute_term_extraction(document_ids, configuration)
    write_results(terms, args.output_file)


if __name__ == '__main__':
    pass
    #main()

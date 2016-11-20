import pprint


def sentence_split(sentences, nodes):
    if len(sentences) > 0 and len(nodes) > 0:
        iter_sentences = iter(sentences)
        iter_nodes = iter(nodes)
    else:
        return []

    processed_node = []
    nodes_sentences = []

    sent_len = len(iter_sentences.next())
    cur_node = iter_nodes.next()

    try:
        while True:
            if cur_node[1] == 'TEXT':
                substr = cur_node[0]
                substr_len = len(substr)

                if substr_len <= sent_len:
                    processed_node.append(cur_node)
                    sent_len -= len(substr)
                    cur_node = iter_nodes.next()

                else:
                    slice_pos = sent_len + 1

                    processed_node.append((substr[:slice_pos], 'TEXT'))
                    nodes_sentences.append(processed_node)
                    processed_node = []

                    cur_node = (substr[slice_pos:], 'TEXT')
                    sent_len = len(iter_sentences.next())

            else:
                processed_node.append(cur_node)
                cur_node = iter_nodes.next()

    except StopIteration:
        nodes_sentences.append(processed_node)

    return nodes_sentences


if __name__ == "__main__":
    sentences = [
        "Startup's participation in this program is voluntary.",
        "Nothing in this Agreement restricts Startup from supporting non-Microsoft technology.",
        "Participants will receive benefits."
    ]

    nodes = [
        ('w:r id="1"', 'TAG'),
        ("Startup's participation ", 'TEXT'),
        ('/w:r', 'TAG'),
        ('w:r', 'TAG'),
        ('w:t', 'TAG'),
        ('in this program is ', 'TEXT'),
        ('/w:t', 'TAG'),
        ('/w:r', 'TAG'),
        ('w:r', 'TAG'),
        ('voluntary. Nothing in', 'TEXT'),
        ('/w:r', 'TAG'),
        ('w:r', 'TAG'),
        (' this Agreement restricts Startup from supporting non-Microsoft'
         ' technology. Participants will receive benefits.', 'TEXT'),
        ('/w:r', 'TAG')
    ]
    result = sentence_split(sentences, nodes)

    pp = pprint.PrettyPrinter()
    pp.pprint(result)
# -*- coding: utf-8 -*-

import operator


def top_cooccorrent_terms(cooccurence_matrix):
    max_matrix = []
    # For each term, look for the most common co-occurrent terms
    for term1 in cooccurence_matrix:
        term1_max_terms = sorted(cooccurence_matrix[term1].items(), key=operator.itemgetter(1), reverse=True)[:5]
        for term2, term2_count in term1_max_terms:
            max_matrix.append(((term1, term2), term2_count))
    terms_max = sorted(max_matrix, key=operator.itemgetter(1), reverse=True)
    return terms_max

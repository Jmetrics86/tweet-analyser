# -*- coding: utf-8 -*-

import operator
from collections import defaultdict


def top_cooccorrent_terms(cooccurence_matrix):
    max_matrix = []
    # For each term, look for the most common co-occurrent terms
    for term1 in cooccurence_matrix:
        term1_max_terms = sorted(cooccurence_matrix[term1].items(), key=operator.itemgetter(1), reverse=True)[:5]
        for term2, term2_count in term1_max_terms:
            max_matrix.append(((term1, term2), term2_count))
    terms_max = sorted(max_matrix, key=operator.itemgetter(1), reverse=True)
    return terms_max


def term_probabilities(total_doc_count, all_terms_counter, term_cooccurence_matrix):
    probability_term = {}
    prob_term_cooccurence_matrix = defaultdict(lambda: defaultdict(int))

    for term1, term1_frequency in all_terms_counter.items():
        probability_term[term1] = term1_frequency / total_doc_count
        for term2 in term_cooccurence_matrix[term1]:
            prob_term_cooccurence_matrix[term1][term2] = term_cooccurence_matrix[term1][term2] / total_doc_count

    return prob_term_cooccurence_matrix

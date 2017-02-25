# -*- coding: utf-8 -*-

from collections import defaultdict
from math import log2
from operator import itemgetter

from utils.ListLoader import ListLoader


def top_cooccorrent_terms(cooccurence_matrix):
    max_matrix = []
    # For each term, look for the most common co-occurrent terms
    for term1 in cooccurence_matrix:
        term1_max_terms = sorted(cooccurence_matrix[term1].items(), key=itemgetter(1), reverse=True)[:5]
        for term2, term2_count in term1_max_terms:
            max_matrix.append(((term1, term2), term2_count))
    terms_max = sorted(max_matrix, key=itemgetter(1), reverse=True)
    return terms_max


def term_probabilities(total_doc_count, all_terms_counter, term_cooccurence_matrix):
    probability_term = {}
    prob_term_cooccurence_matrix = defaultdict(lambda: defaultdict(int))

    for term1, term1_frequency in all_terms_counter.items():
        probability_term[term1] = term1_frequency / total_doc_count
        for term2 in term_cooccurence_matrix[term1]:
            prob_term_cooccurence_matrix[term1][term2] = term_cooccurence_matrix[term1][term2] / total_doc_count

    return prob_term_cooccurence_matrix, probability_term


def calculate_pmi(probability_term, cooccurrence_matrix, prob_term_cooccurence_matrix):
    """Calculates the Pointwise Mutual Information of each pair of terms occurring together"""
    pmi = defaultdict(lambda: defaultdict(int))
    for term1 in probability_term:
        for term2 in cooccurrence_matrix[term1]:
            denom = probability_term[term1] * probability_term[term2]
            pmi[term1][term2] = log2(prob_term_cooccurence_matrix[term1][term2] / denom)
    return pmi


def calculate_semantic_orientation(probability_term, pmi):
    semantic_orientation = {}
    positive_lexicon = ListLoader().load('resources/positive-words.txt')
    negative_lexicon = ListLoader().load('resources/negative-words.txt')

    for term, n in probability_term.items():
        positive_assoc = sum(pmi[term][word] for word in positive_lexicon)
        negative_assoc = sum(pmi[term][word] for word in negative_lexicon)
        semantic_orientation[term] = positive_assoc - negative_assoc
    return semantic_orientation


def top_semantic_terms(semantic_orientation_dict, num_terms):
    """Returns top positive and negative terms with semantic orientation"""
    semantic_sorted = sorted(semantic_orientation_dict.items(), key=itemgetter(1), reverse=True)
    top_positive = semantic_sorted[:num_terms]
    top_negative = semantic_sorted[-num_terms:]
    return top_positive, top_negative

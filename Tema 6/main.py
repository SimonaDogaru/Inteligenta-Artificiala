# parse de rdf file
import random
import rdflib
from rdflib import Graph
from nltk.corpus import wordnet as wn
import nltk

nltk.download('wordnet')
def get_rdf_triplets(graph):
    triplets = []
    for (subject, predicate, object) in graph:
        subj_name = get_name_from_uri(subject)
        pred_name = get_name_from_uri(predicate)
        obj_name = get_name_from_uri(object)
        if subj_name is None or pred_name is None or obj_name is None:
            continue
        print(subj_name, " - ", pred_name, " - ", obj_name)
        triplets.append((subj_name, pred_name, obj_name))
    return triplets


def get_name_from_uri(uri):
    name = None
    if isinstance(uri, rdflib.term.URIRef):
        name = uri.split('#')[-1]
    return name


def get_answers(index, triplets, triplet):
    a = []
    for t in triplets:
        if index == 0:
            if triplet[1] == t[1] and triplet[2] == t[2] :
                a.append(t[0].lower())
        elif index == 1:
            if triplet[0] == t[0] and triplet[2] == t[2] :
                a.append(t[1].lower())
        else:
            if triplet[0] == t[0] and triplet[1] == t[1] :
                a.append(t[2].lower())
    return a

def generate_question(triplets):
    triplet = random.choice(triplets)
    random_word = random.choice(triplet)
    #answers = get_answers(triplet, random_word)
    index = None
    if random_word == triplet[0]:
        question = "Who is in relationship " + triplet[1] + " with " + triplet[2] + "?"
        index = 0
    elif random_word == triplet[1]:
        question = "What is the relationship between " + triplet[0] + " and " + triplet[2] + "?"
        index = 1
    else:
        question = "Who is in relationship " + triplet[1] + " with " + triplet[0] + "?"
        index = 2
    answers = get_answers(index, triplets, triplet)
    return question, answers, index, triplet


def get_synonyms(word):
    synonyms = list()
    for syn in wn.synsets(word):
        for l in syn.lemmas():
            if l.name().lower() != word.lower():
                synonyms.append(l.name().lower())
    if len(synonyms) != 0:
        return synonyms
    return [word]


def game(triplets):
    while True:
        q, a, index, triplet = generate_question(triplets)
        print(q)
        print(a)
        your_answer = input("Please type your answer: ")
        if your_answer.lower() in a:
            print("Correct answer!")
        elif your_answer in answer_synonyms:
            print("Correct answer!")
        else:
            print("Incorrect answer!")
        answer_synonyms = get_synonyms(triplet[index])
        syn_triplet = (get_synonyms(triplet[0])[0], get_synonyms(
            triplet[1])[0], get_synonyms(triplet[2])[0])
        # print(q)
        # print(a)
        syn_question, _, _, _ = generate_question([syn_triplet])
        print(syn_question)
        print(answer_synonyms)
        your_answer = input("Please type your answer: ")
        if your_answer.lower() in a:
            print("Correct answer!")
        elif your_answer in answer_synonyms:
            print("Correct answer!")
        else:
            print("Incorrect answer!")
        response = input("Do you want to continue? (yes/no)\n")
        if response == 'no':
            break

    word = input("Type a word:")
    for synset in wn.synsets(word):
        print(synset, " = ", synset.definition())


def play(fisname):
    graph = Graph()
    graph.parse(fisname)
    triplets = get_rdf_triplets(graph)
    game(triplets)


play("food.rdf")
import mathematical_calculation as ms

all_tagged_sentences = [{"words":["dev","love","cube"],"tags":{"0":"Noun","1":"Verb","2":"Noun"}},{"words":["can","dev","google","cube"],"tags":{"0":"Modal Auxiliary","1":"Noun","2":"Verb","3":"Noun"}},{"words":["will","juliet","google","cube"],"tags":{"0":"Modal Auxiliary","1":"Noun","2":"Verb","3":"Noun"}},{"words":["juliet","love","will"],"tags":{"0":"Noun","1":"Verb","2":"Noun"}},{"words":["will","love","google"],"tags":{"0":"Noun","1":"Verb","2":"Noun"}}]

result = ms.calculate_transition_probability(data= all_tagged_sentences)

print(result)

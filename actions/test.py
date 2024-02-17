
# from rasa.shared.nlu.interpreter import NaturalLanguageInterpreter as Interpreter
# pipeline_config = [
#     {"name": "WhitespaceTokenizer"},
#     {"name": "LexicalSyntacticFeaturizer"},
#     {"name": "CountVectorsFeaturizer"},
#     {"name": "CountVectorsFeaturizer", "analyzer": "char_wb", "min_ngram": 1, "max_ngram": 4},
#     {"name": "DIETClassifier", "epochs": 100, "constrain_similarities": True}
# ]

# # Load the trained NLU model with the defined pipeline
# interpreter = Interpreter.load("../models/nlu-20240216-213607-archaic-frogman.tar", pipeline=pipeline_config)
# # Process the text to get the output until DIETClassifier
# text = "how to get citizenship"
# output = interpreter.parse(text)

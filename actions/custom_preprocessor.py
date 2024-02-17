# from rasa.shared.core.events import format_message
# import logging
# from rasa.engine.recipes.default_recipe import DefaultV1Recipe
# from rasa.shared.nlu.interpreter import NaturalLanguageInterpreter
# from rasa.engine.graph import GraphComponent

# @DefaultV1Recipe.register(
#     DefaultV1Recipe.ComponentType.ENTITY_EXTRACTOR, is_trainable=False
# )
# class CustomPreprocessor(NaturalLanguageInterpreter, GraphComponent):
    
#     def process(self, message: format_message, **kwargs):
#         text = message.text
#         logging.info(f"Text before DIETClassifier: {text}")
#         # ... additional processing if needed ...
#         return message



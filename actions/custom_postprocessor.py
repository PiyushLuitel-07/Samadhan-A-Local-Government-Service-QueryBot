# from rasa.shared.core.events import format_message
# import logging
# from rasa.engine.recipes.default_recipe import DefaultV1Recipe
# from rasa.shared.nlu.interpreter import NaturalLanguageInterpreter

# @DefaultV1Recipe.register(
#     DefaultV1Recipe.ComponentType.ENTITY_EXTRACTOR, is_trainable=False
# )
# class CustomPostprocessor(NaturalLanguageInterpreter):
   
#     def process(self, message: format_message, **kwargs):
#         text = message.text  # This should be processed text by DIETClassifier
#         logging.info(f"Text after DIETClassifier: {text}")
#         # ... additional processing if needed ...
#         return message
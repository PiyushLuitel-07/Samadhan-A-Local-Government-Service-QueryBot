# # This files contains your custom actions which can be used to run
# # custom Python code.
# #
# # See this guide on how to implement these action:
# # https://rasa.com/docs/rasa/custom-actions



# from typing import Text, List, Any, Dict
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.events import SlotSet


# class ActionHandleCitizenshipQuery(Action):
#     def name(self) -> Text:
#         return "action_handle_citizenship_query"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         # Extract entities from the user's message
#         entity_values = next(tracker.get_latest_entity_values('type'),None)
#         if  entity_values == 'citizenship by descent': 
#                 dispatcher.utter_message(response="utter_citizenship_by_descent_eligibility_criteria")
#                 dispatcher.utter_message(response="utter_citizenship_by_descent_documents_required")
#                 dispatcher.utter_message(response="utter_citizenship_by_descent_steps")
#         elif  entity_values == 'citizenship by birth':
#                     dispatcher.utter_message(response="utter_citizenship_by_birth_eligibility_criteria")
#                     dispatcher.utter_message(response="utter_citizenship_by_birth_documents_required")
#                     dispatcher.utter_message(response="utter_citizenship_by_birth_steps")
#         else:
#                 dispatcher.utter_message(response="utter_citizenship")
#         return []

 
# class ActionHandleCitizenshipQueryRomanized(Action):
#     def name(self) -> Text:
#         return "action_handle_citizenship_query_romanized"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         # Extract entities from the user's message
#         entity_values = next(tracker.get_latest_entity_values('type'),None)
#         if  entity_values == 'descent': 
#                 dispatcher.utter_message(response="utter_citizenship_by_descent_eligibility_romanized")
#                 dispatcher.utter_message(response="utter_citizenship_by_descent_documents_romanized")
#                 dispatcher.utter_message(response="utter_citizenship_by_descent_steps_romanized")
#         elif  entity_values == 'birth':
#                     dispatcher.utter_message(response="utter_citizenship_by_birth_eligibility_romanized")
#                     dispatcher.utter_message(response="utter_citizenship_by_birth_documents_romanized")
#                     dispatcher.utter_message(response="utter_citizenship_by_birth_steps_romanized")
#         else:
#                 dispatcher.utter_message(response="utter_citizenship")
#         return []


from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.interfaces import Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted
import google.generativeai as genai
from config import apikey
# from rasa.engine.recipes.default_recipe import DefaultV1Recipe, GraphComponent

# @DefaultV1Recipe.register(
#     DefaultV1Recipe.Component, is_trainable=True
# )

class RephraseFallbackAction(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(self,dispatcher: CollectingDispatcher,tracker: Tracker, domain: Dict[Text, Any],) -> List[Dict[Text, Any]]:
        # Get the name of the intent and action
        # intent = tracker.latest_message['intent'].get('name')
        # action = tracker.latest_action_name
        user_message = tracker.latest_message.get('text')
        # Configure Generative AI model

        genai.configure(api_key=apikey)

        # Set up the model
        generation_config = {
            "temperature": 0.9,
            "top_p": 1,
            "top_k": 1,
            "max_output_tokens": 2048,
          }

        safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
        ]

        model = genai.GenerativeModel(model_name="gemini-pro",
                                      generation_config=generation_config,
                                      safety_settings=safety_settings)

        # Construct prompt as a single string
        prompt = (
            'You are an AI assistant for the citizens of nepal. '
            'You help to solve user queries related to government services like citizenship,birth certificate, marriage certificate,migration, divorce,death certificate. '
            'Here is the user message answer it in context of nepal '
            # f"User intent: {intent}\n"
            # f"informations: {action}\n"
            f'You: {user_message}'
        )

        # Generate content
        response = model.generate_content(prompt)
        dispatcher.utter_message(text=response)
        print(response.text)
        return []  
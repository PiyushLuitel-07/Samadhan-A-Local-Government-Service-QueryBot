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


    
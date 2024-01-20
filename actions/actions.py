# # This files contains your custom actions which can be used to run
# # custom Python code.
# #
# # See this guide on how to implement these action:
# # https://rasa.com/docs/rasa/custom-actions



from typing import Text, List, Any, Dict
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionHandleCitizenshipQuery(Action):
    def name(self) -> Text:
        return "action_handle_citizenship_query"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Extract entities from the user's message
        entities = tracker.latest_message['entities']

        # Default value for citizenship type
        citizenship_type = "unspecified"

        # Check if there are entities
        if entities:
            entity_values = [entity['value'] for entity in entities]
            
            if 'citizenship by descent' in entity_values:
                citizenship_type = 'citizenship by descent'
                dispatcher.utter_message(response="utter_citizenship_by_descent_eligibility_criteria")
                dispatcher.utter_message(response="utter_citizenship_by_descent_documents_required")
                dispatcher.utter_message(response="utter_citizenship_by_descent_steps")
            elif 'citizenship by birth' in entity_values:
                citizenship_type = 'citizenship by birth'
                dispatcher.utter_message(response="utter_citizenship_by_birth_eligibility_criteria")
                dispatcher.utter_message(response="utter_citizenship_by_birth_documents_required")
                dispatcher.utter_message(response="utter_citizenship_by_birth_steps")
            elif 'citizenship by naturalization' in entity_values:
                citizenship_type = 'citizenship by naturalization'
                dispatcher.utter_message(response="utter_citizenship_by_naturalization_criteria")
                dispatcher.utter_message(response="utter_citizenship_by_naturalization_required")
                dispatcher.utter_message(response="utter_citizenship_by_naturalization_steps")
            else:
                citizenship_type = 'unspecified' 
        # Set the slot value for 'citizenship_type'
        return [SlotSet("citizenship_type", citizenship_type)]
        
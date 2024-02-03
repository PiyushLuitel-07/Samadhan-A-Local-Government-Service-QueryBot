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
        entity_values = next(tracker.get_latest_entity_values('type'),None)
        if  entity_values == 'citizenship by descent': 
                dispatcher.utter_message(response="utter_citizenship_by_descent_eligibility_criteria")
                dispatcher.utter_message(response="utter_citizenship_by_descent_documents_required")
                dispatcher.utter_message(response="utter_citizenship_by_descent_steps")
        elif  entity_values == 'citizenship by birth':
                    dispatcher.utter_message(response="utter_citizenship_by_birth_eligibility_criteria")
                    dispatcher.utter_message(response="utter_citizenship_by_birth_documents_required")
                    dispatcher.utter_message(response="utter_citizenship_by_birth_steps")
        else:
                dispatcher.utter_message(response="utter_citizenship")
        return []

class ActionHandleCertificateQuery(Action):
    def name(self) -> Text:
        return "action_handle_certificate_query"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Extract entities from the user's message
        entities = tracker.latest_message['entities']

        if entities:
            entity_values = [entity['value'] for entity in entities]
            
            if 'birth certificate' in entity_values:
                if 'documents' in entity_values: 
                    dispatcher.utter_message(response="utter_birth_certificate_documents")
                elif 'steps' in entity_values: 
                    dispatcher.utter_message(response="utter_birth_certificate_steps")
                else: 
                    dispatcher.utter_message(response="utter_birth_certificate_documents")
                    dispatcher.utter_message(response="utter_birth_certificate_steps")
            elif 'death certificate' in entity_values:
                if 'documents' in entity_values: 
                    dispatcher.utter_message(response="utter_death_certificate_documents")
                elif 'steps' in entity_values: 
                    dispatcher.utter_message(response="utter_death_certificate_steps")
                else: 
                    dispatcher.utter_message(response="utter_death_certificate_documents")
                    dispatcher.utter_message(response="utter_death_certificate_steps")
            elif 'marriage certificate' in entity_values:
                if 'documents' in entity_values: 
                    dispatcher.utter_message(response="utter_marriage_certificate_documents")
                elif 'steps' in entity_values: 
                    dispatcher.utter_message(response="utter_marriage_certificate_steps")
                else: 
                    dispatcher.utter_message(response="utter_marriage_certificate_documents")
                    dispatcher.utter_message(response="utter_marriage_certificate_steps")
            elif 'divorce certificate' in entity_values:
                if 'documents' in entity_values: 
                    dispatcher.utter_message(response="utter_divorce_certificate_documents")
                elif 'steps' in entity_values: 
                    dispatcher.utter_message(response="utter_divorce_certificate_steps")
                else: 
                    dispatcher.utter_message(response="utter_divorce_certificate_documents")
                    dispatcher.utter_message(response="utter_divorce_certificate_steps")
            elif 'migration certificate' in entity_values:
                if 'documents' in entity_values: 
                    dispatcher.utter_message(response="utter_migration_certificate_documents")
                elif 'steps' in entity_values: 
                    dispatcher.utter_message(response="utter_migration_certificate_steps")
                else: 
                    dispatcher.utter_message(response="utter_migration_certificate_documents")
                    dispatcher.utter_message(response="utter_migration_certificate_steps")
            else:
                dispatcher.utter_message(response="utter_certificate_query")
        return []
    
class ActionHandleCitizenshipQueryRomanized(Action):
    def name(self) -> Text:
        return "action_handle_citizenship_query_romanized"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Extract entities from the user's message
        entity_values = next(tracker.get_latest_entity_values('type'),None)
        if  entity_values == 'descent': 
                dispatcher.utter_message(response="utter_citizenship_by_descent_eligibility_romanized")
                dispatcher.utter_message(response="utter_citizenship_by_descent_documents_romanized")
                dispatcher.utter_message(response="utter_citizenship_by_descent_steps")
        elif  entity_values == 'birth':
                    dispatcher.utter_message(response="utter_citizenship_by_birth_eligibility_romanized")
                    dispatcher.utter_message(response="utter_citizenship_by_birth_documents_romanized")
                    dispatcher.utter_message(response="utter_citizenship_by_birth_steps_romanized")
        else:
                dispatcher.utter_message(response="utter_citizenship")
        return []

class ActionHandleCertificateQueryRomanized(Action):
    def name(self) -> Text:
        return "action_handle_certificate_query_romanized"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Extract type of certificate 
        entity_values = next(tracker.get_latest_entity_values('type'),None)
      
        if 'birth' == entity_values:
            dispatcher.utter_message(response="utter_birth_certificate_documents_romanized")
            dispatcher.utter_message(response="utter_birth_certificate_steps_romanized")
        elif 'death' == entity_values:
            dispatcher.utter_message(response="utter_death_certificate_documents_romanized")
            dispatcher.utter_message(response="utter_death_certificate_steps_romanized")
        elif 'marriage' == entity_values:
            dispatcher.utter_message(response="utter_marriage_certificate_documents_romanized")
            dispatcher.utter_message(response="utter_marriage_certificate_steps_romanized")
        elif 'divorce' == entity_values:
            dispatcher.utter_message(response="utter_divorce_certificate_documents_romanized")
            dispatcher.utter_message(response="utter_divorce_certificate_steps_romanized")
        elif 'migration' == entity_values:
            dispatcher.utter_message(response="utter_migration_certificate_documents_romanized")
            dispatcher.utter_message(response="utter_migration_certificate_steps_romanized")
        else:
            dispatcher.utter_message(text="maff garnu hola yo service ahile upalabdha chaina")
        return []
    
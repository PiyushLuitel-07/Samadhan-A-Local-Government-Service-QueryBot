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

        if entities:
            entity_values = [entity['value'] for entity in entities]
            
            if 'citizenship by descent' in entity_values:
                if 'eligibility' in entity_values:
                    dispatcher.utter_message(response="utter_citizenship_by_descent_eligibility_criteria")
                elif 'documents' in entity_values: 
                    dispatcher.utter_message(response="utter_citizenship_by_descent_documents_required")
                elif 'steps' in entity_values: 
                    dispatcher.utter_message(response="utter_citizenship_by_descent_steps")
                else: 
                    dispatcher.utter_message(response="utter_citizenship_by_descent_eligibility_criteria")
                    dispatcher.utter_message(response="utter_citizenship_by_descent_documents_required")
                    dispatcher.utter_message(response="utter_citizenship_by_descent_steps")
            elif 'citizenship by birth' in entity_values:
                if 'eligibility' in entity_values:
                    dispatcher.utter_message(response="utter_citizenship_by_birth_eligibility_criteria")
                elif 'documents' in entity_values: 
                    dispatcher.utter_message(response="utter_citizenship_by_birth_documents_required")
                elif 'steps' in entity_values: 
                    dispatcher.utter_message(response="utter_citizenship_by_birth_steps")
                else: 
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
        entities = tracker.latest_message['entities']

        if entities:
            entity_values = [entity['value'] for entity in entities]
            
            if 'descent' in entity_values:
                if 'eligibility' in entity_values:
                    dispatcher.utter_message(response="utter_citizenship_by_descent_eligibility_criteria_romanized")
                elif 'documents' in entity_values: 
                    dispatcher.utter_message(response="utter_citizenship_by_descent_documents_required_romanized")
                elif 'steps' in entity_values: 
                    dispatcher.utter_message(response="utter_citizenship_by_descent_steps_romanized")
                else: 
                    dispatcher.utter_message(response="utter_citizenship_by_descent_eligibility_criteria_romanized")
                    dispatcher.utter_message(response="utter_citizenship_by_descent_documents_required_romanized")
                    dispatcher.utter_message(response="utter_citizenship_by_descent_steps_romanized")
            elif 'birth' in entity_values:
                if 'eligibility' in entity_values:
                    dispatcher.utter_message(response="utter_citizenship_by_birth_eligibility_criteria_romanized")
                elif 'documents' in entity_values: 
                    dispatcher.utter_message(response="utter_citizenship_by_birth_documents_required_romanized")
                elif 'steps' in entity_values: 
                    dispatcher.utter_message(response="utter_citizenship_by_birth_steps_romanized")
                else: 
                    dispatcher.utter_message(response="utter_citizenship_by_birth_eligibility_criteria_romanized")
                    dispatcher.utter_message(response="utter_citizenship_by_birth_documents_required_romanized")
                    dispatcher.utter_message(response="utter_citizenship_by_birth_steps_romanized")
            else:
                dispatcher.utter_message(response="utter_citizenship_romanized")
        return []

class ActionHandleCertificateQueryRomanized(Action):
    def name(self) -> Text:
        return "action_handle_certificate_query_romanized"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Extract entities from the user's message
        entities = tracker.latest_message['entities']

        if entities:
            entity_values = [entity['value'] for entity in entities]
            if 'birth' in entity_values:
                if 'documents' in entity_values: 
                    dispatcher.utter_message(response="utter_birth_certificate_documents_romanized")
                elif 'steps' in entity_values: 
                    dispatcher.utter_message(response="utter_birth_certificate_steps_romanized")
                else: 
                    dispatcher.utter_message(response="utter_birth_certificate_documents_romanized")
                    dispatcher.utter_message(response="utter_birth_certificate_steps_romanized")
            elif 'death' in entity_values:
                if 'documents' in entity_values: 
                    dispatcher.utter_message(response="utter_death_certificate_documents_romanized")
                elif 'steps' in entity_values: 
                    dispatcher.utter_message(response="utter_death_certificate_steps_romanized")
                else: 
                    dispatcher.utter_message(response="utter_death_certificate_documents_romanized")
                    dispatcher.utter_message(response="utter_death_certificate_steps_romanized")
            elif 'marriage' in entity_values:
                if 'documents' in entity_values: 
                    dispatcher.utter_message(response="utter_marriage_certificate_documents_romanized")
                elif 'steps' in entity_values: 
                    dispatcher.utter_message(response="utter_marriage_certificate_steps_romanized")
                else: 
                    dispatcher.utter_message(response="utter_marriage_certificate_documents_romanized")
                    dispatcher.utter_message(response="utter_marriage_certificate_steps_romanized")
            elif 'divorce' in entity_values:
                if 'documents' in entity_values: 
                    dispatcher.utter_message(response="utter_divorce_certificate_documents_romanized")
                elif 'steps' in entity_values: 
                    dispatcher.utter_message(response="utter_divorce_certificate_steps_romanized")
                else: 
                    dispatcher.utter_message(response="utter_divorce_certificate_documents_romanized")
                    dispatcher.utter_message(response="utter_divorce_certificate_steps_romanized")
            elif 'migration' in entity_values:
                if 'documents' in entity_values: 
                    dispatcher.utter_message(response="utter_migration_certificate_documents_romanized")
                elif 'steps' in entity_values: 
                    dispatcher.utter_message(response="utter_migration_certificate_steps_romanized")
                else: 
                    dispatcher.utter_message(response="utter_migration_certificate_documents_romanized")
                    dispatcher.utter_message(response="utter_migration_certificate_steps_romanized")
            else:
                dispatcher.utter_message(response="utter_certificate_query_romanized")
        return []
    
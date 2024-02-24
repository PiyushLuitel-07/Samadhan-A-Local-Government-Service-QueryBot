# # This files contains your custom actions which can be used to run
# # custom Python code.
# #
# # See this guide on how to implement these action:
# # https://rasa.com/docs/rasa/custom-actions



from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.interfaces import Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted
import google.generativeai as genai

import os
#import config
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
        genai.configure(api_key= os.getenv('gemini_api_key'))

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
            'if user message is in in roman nepali, you should give response in roman nepali.'
            'if user message is in english give the response in english language.'
            'nepal ko area kati ho. is the example of roman nepali message, which should be response with nepal ko area 1,47,181 ho'
            'Here is the user message answer it in the context of nepal'
                       
            # f"User intent: {intent}\n"
            # f"informations: {action}\n"
            f'user: {user_message}'
        )

        # Generate content
        response = model.generate_content(prompt)
        dispatcher.utter_message(response.text)

        prev_action_name = None

# Iterate through the events to find the previous action
        for event in reversed(tracker.events):
            if event.get("event") == "action" and event.get("name") != "action_listen":
                prev_action_name = event.get("name")
                break
        print(prev_action_name)
# Determine the appropriate response based on the previous action
        if prev_action_name == "utter_citizenship":
            dispatcher.utter_message("let's continue from where we left off.")
            dispatcher.utter_message(response="utter_citizenship")
       
        elif prev_action_name == "utter_citizenship_by_naturalization":
            # If the previous action was asking for the user's name, prompt for their email
            dispatcher.utter_message("let's continue from where we left off.")
            dispatcher.utter_message(response="utter_citizenship_by_naturalization")
        elif prev_action_name == "utter_citizenship_romanized":
            dispatcher.utter_message("let's continue from where we left off.")
            dispatcher.utter_message(response="utter_citizenship")
       
        elif prev_action_name == "utter_citizenship_by_naturalization_romanized":
            # If the previous action was asking for the user's name, prompt for their email
            dispatcher.utter_message("let's continue from where we left off.")
            dispatcher.utter_message(response="utter_citizenship_by_naturalization")
        # else:
        #     # If the previous action doesn't match any known context, handle appropriately
        #     dispatcher.utter_message("I'm not sure what to do next. Let's start over.")

        print(tracker.events)
        return [UserUtteranceReverted]  
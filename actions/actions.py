# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionOrder(Action):

    def name(self) -> Text:
        return "action_order"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        pizza_count = tracker.get_slot('pizza_count')
        pizza_size = tracker.get_slot('pizza_size')
        pizza_type = tracker.get_slot('pizza_type')
        
        dispatcher.utter_message(text = f"OK, your order is {pizza_count} {pizza_size} {pizza_type} pizzas")

        return []

# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.forms import FormAction


# class ActionOrder(FormAction):

#     def name(self) -> Text:
#         return "action_order"

#     @staticmethod
#     def required_slots(tracker: Tracker) -> List[Text]:
#         return ["pizza_count", "pizza_size", "pizza_type"]

#     def submit(
#             self,
#             dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         pizza_count = tracker.get_slot('pizza_count')
#         pizza_size = tracker.get_slot('pizza_size')
#         pizza_type = tracker.get_slot('pizza_type')

#         print(pizza_count, pizza_size, pizza_type)
        
#         dispatcher.utter_message(text = f"OK, your order is {pizza_count} {pizza_size} {pizza_type} pizzas")

#         return []

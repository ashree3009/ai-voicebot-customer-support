from app.core.logger import get_logger

logger = get_logger()

class ResponseGenerator:

    def __init__(self):

        self.responses = {

            "order_status":
            "Sure. Please provide your order ID so I can check the delivery status.",

            "cancel_order":
            "I can help cancel your order. Please share your order ID.",

            "refund_request":
            "I'm sorry for the inconvenience. Please provide your order ID to start the refund process.",

            "subscription_issue":
            "I understand you're facing a subscription issue. Please provide your account email.",

            "payment_issue":
            "It looks like there was a payment problem. Please confirm your order ID.",

            "account_update":
            "Sure. Please tell me which account detail you'd like to update.",

            "technical_support":
            "I'm here to help. Please describe the technical issue you're experiencing.",

            "product_information":
            "I'd be happy to provide product information. Which product are you asking about?",

            "complaint":
            "I'm sorry to hear that. Please tell me more about the issue so I can assist you.",

            "speak_to_agent":
            "No problem. I will connect you to a customer support agent shortly."
        }

        self.default_response = "I'm sorry, I didn't fully understand your request. Could you please repeat?"

    def generate(self, intent):

        response = self.responses.get(intent, self.default_response)

        logger.info(f"Generated response for intent {intent}")

        return response
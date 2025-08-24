from app.utils.messageUtil import MessagesUtil
from app.service.llmService import LLMService

llmService = LLMService()
class MessageService:
    def __init__(self):
        self.messageUtil = MessagesUtil()
        self.llmService = LLMService()    

    def process_message(self, message):
        if self.messageUtil.isBankSms(message):
            return self.llmService.runLLM(message)
        else:
            return None
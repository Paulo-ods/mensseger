from BO.coreBO.integration import IntegrationBO
from DBA.whatsappDBA.whatsappDBA import whatsappDBA


class WhatsappBO(IntegrationBO):

    def send_mensage(self):
        status, description, self.url = self.get_url_whatsapp(accont_code='113926755135673')

        if status:
            status, description, self.headers = self.get_header_whatsapp()

        if status:
            status, description, self.body = self.get_body_whatsapp()

        if status:
            try:
                self.post()
                status = self.response.status_code
                description = self.response.content
            except:
                status = False
                description = 'error when ordering'

        return status, description

    @staticmethod
    def get_url_whatsapp(accont_code=None):
        try:
            url = f'https://graph.facebook.com/v17.0/{accont_code}/messages'
            return True, '', url
        except:
            return False, 'request url not found', None

    @staticmethod
    def get_header_whatsapp(self):
        auth_code = whatsappDBA.get_auth_token()
        if auth_code:
            auth = f"Authorization: Bearer {auth_code}"
            auth += 'Content-Type: application/json'
            return True, '', auth
        else:
            return False, 'authentication code not found!', None

    @staticmethod
    def get_body_whatsapp():
        try:
            body = {
                "messaging_product": "whatsappBO",
                "to": "5546991128600",
                "type": "template",
                "template": {
                    "name": "hello_world",
                    "language": {
                        "code": "en_US"
                    }
                }
            }
            return True, '', body
        except:
            return False, 'request body not found', None

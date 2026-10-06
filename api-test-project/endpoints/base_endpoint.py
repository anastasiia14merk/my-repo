class BaseEndpoint:

 def __init__(self):
    self.response = None

 @property
 def json(self):
     return self.response.json()

 def check_status_code(self, code):
     assert self.response.status_code == code
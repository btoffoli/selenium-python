

class LoginPage
	
	#def __init__(self, *args, **kwargs):
	#    super(CLASS_NAME, self).__init__(*args, **kwargs)
	def __init__(self, webdriver, url):
		self.webdriver = webdriver
		self.url = url

	def visita(self):
		self.driver.get()
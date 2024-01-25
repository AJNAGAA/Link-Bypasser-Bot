class Config(object):
   # Url Shortner Information 
    TECH_VJ = bool(environ.get('TECH_VJ', True)) # Set False If you want shortlink off else True
    TECH_VJ_URL = environ.get('TECH_VJ_URL', 'moneykamalo.com') # your shortlink url domain or url without https://
    TECH_VJ_API = environ.get('TECH_VJ_API', '0eefb93e1e3ce9470a7033115ceb1bad13a9d674') # your url shortner api

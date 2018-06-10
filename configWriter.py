import configparser

config = configparser.ConfigParser()
config.add_section('Spotify')
config.set('Spotify', 'client_id', 'b88d0c99674247bcb826148026417e6f')
config.set('Spotify', 'client_secret', "fcc139e4e91f4a78aa797bd11a194ce3")
config.set('Spotify', 'tej_id', "12129226315")
config.set('Spotify', 'rohan_id', "1250975621")
config.set('Spotify', 'ram_id', "rammk1999")
config.set('Spotify', 'yash_id', "yash.bora")
config.set('Spotify', 'shivam_id', "1228148210")


with open('config.ini', 'w') as configfile:
	config.write(configfile)

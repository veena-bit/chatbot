from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import requests
import json
class ActionPoster(Action):
	def name(self):
		return 'action_poster'
		
	def run(self, dispatcher, tracker, domain):
		# Get a free apikey from omdbapi.com and set the value here. for eg. apikey = 'abcdef98'
		apikey = "aeaafb76"
		movieName = tracker.get_slot('movie')
		if not apikey:
			dispatcher.utter_message("OMDB API Key not set. Cannot fetch movie")
			return [SlotSet('movie', movieName)]

		retStr= ""
		if movieName:
			url = r'http://www.omdbapi.com/?s=' + movieName + "&apikey=" + apikey
			r = requests.get(url)
			if r.ok:
				data = json.loads(r.text)
				posters = [ m['Poster'] for m in data['Search'] if m and m['Poster'] != 'N/A']
			retStr = "Here are a few: \n" + "\n".join(posters[:2])
		else:
			retStr = "Are you sure this movie , {}, exists?".format(movieName)
		response = retStr

		dispatcher.utter_message(response)
		return [SlotSet('movie',movieName)]
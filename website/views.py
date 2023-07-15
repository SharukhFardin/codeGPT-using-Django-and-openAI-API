from django.shortcuts import render
from django.contrib import messages
import openai
# Create your views here.


# API key = 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


def home(request):

	# list of coding language for codeGPT
	lang_list = ['c', 'clike', 'cpp', 'csharp', 'css', 'dart', 'django', 'go', 'html', 'java', 'javascript', 'kotlin', 'markup', 'matlab', 'mongodb', 'objectivec', 'perl', 'php', 'plsql', 'powershell', 'python', 'r', 'regex', 'ruby', 'rust', 'sql', 'swift', 'yaml']

	if request.method == "POST":
		code = request.POST['code']
		lang = request.POST['lang']

		# check to make sure a lanuage is selected
		if lang == "Select Programming Language":
			messages.success(request, "Hey! Please select a programming language.")
			return render(request, 'home.html', {'lang_list':lang_list, 'code':code, 'lang':lang})

		else:
			#OpenAI Key!!!!
			openai.api_key = "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"
			# Create OpenAI instance
			openai.Model.list()
			# Make an OpenAI Request
			try:
				response = openai.Completion.create(
					engine = 'text-davinci-003',
					prompt = f"Respond only with code. Fix this {lang} code: {code}",
					temperature = 0,
					max_tokens = 1000,
					top_p = 1.0,
					frequency_penalty = 0.0,
					presence_penalty = 0.0,
					)
				# Parse the response
				response = (response["choices"][0]["text"]).strip()

				return render(request, 'home.html', {'lang_list':lang_list, 'response':response, 'lang':lang})

			except Exception as e:
				return render(request, 'home.html', {'lang_list':lang_list, 'response':e, 'lang':lang})


	return render(request, 'home.html', {'lang_list':lang_list})


def suggest(request):

	# list of coding language for codeGPT
	lang_list = ['c', 'clike', 'cpp', 'csharp', 'css', 'dart', 'django', 'go', 'html', 'java', 'javascript', 'kotlin', 'markup', 'matlab', 'mongodb', 'objectivec', 'perl', 'php', 'plsql', 'powershell', 'python', 'r', 'regex', 'ruby', 'rust', 'sql', 'swift', 'yaml']

	if request.method == "POST":
		code = request.POST['code']
		lang = request.POST['lang']

		# check to make sure a lanuage is selected
		if lang == "Select Programming Language":
			messages.success(request, "Hey! Please select a programming language.")
			return render(request, 'suggest.html', {'lang_list':lang_list, 'code':code, 'lang':lang})

		else:
			#OpenAI Key!!!!
			openai.api_key = "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"
			# Create OpenAI instance
			openai.Model.list()
			# Make an OpenAI Request
			try:
				response = openai.Completion.create(
					engine = 'text-davinci-003',
					prompt = f"Respond only with code. {code}",
					temperature = 0,
					max_tokens = 1000,
					top_p = 1.0,
					frequency_penalty = 0.0,
					presence_penalty = 0.0,
					)
				# Parse the response
				response = (response["choices"][0]["text"]).strip()

				return render(request, 'suggest.html', {'lang_list':lang_list, 'response':response, 'lang':lang})

			except Exception as e:
				return render(request, 'suggest.html', {'lang_list':lang_list, 'response':e, 'lang':lang})


	return render(request, 'suggest.html', {'lang_list':lang_list})
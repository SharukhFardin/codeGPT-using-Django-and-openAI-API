from django.shortcuts import render
from django.contrib import messages
# Create your views here.

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

		return render(request, 'home.html', {'lang_list':lang_list, 'code':code, 'lang':lang})


	return render(request, 'home.html', {'lang_list':lang_list})

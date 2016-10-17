
""" 
Joris de Ruiter (2016) | Python/Django sample code
For a game with Themes, Challenges and a Leaderboard;
Use of no try-except statements on purpose
"""

"""
1. Play the game
"""
def start(request):
    return render(request, 'challenge/start.html')


"""
2. Choose a Theme
"""
def choose_theme(request):
    themes = Theme.objects.filter(active=True).order_by('title')
    return render(request, 'challenge/choose_theme.html', {'themes':themes})


"""
3. Choose a Chalenge from the Theme
"""
def choose_challenge(request, themeID):

    theme = Theme.objects.get(id=themeID)
    challenges = Challenge.objects.filter(theme=themeID).filter(active=True)

    return render(request, 'challenge/choose_challenge.html', {'theme':theme, 'challenges':challenges})


"""
4. Play the challenge
"""
def challenge(request, challengeID):

    challenge = Challenge.objects.get(id=challengeID)
    choices = challenge.choice_set.all()

    participantForm = ParticipantForm(request.POST or None)
    if request.POST:
        if participantForm.is_valid() and participantForm.has_changed():
        	#etc 
        
    return render(request, 'challenge/challenge.html', {'challenge': challenge, 'choices': choices, 'participantForm': participantForm})



"""
5. Leaderboard
"""
def leaderboard(request):
 
	participants = Participant.objects.exclude(score=None).exclude(challenge=None).order_by('score')[0:10]
 
 	return render(request, 'challenge/leaderboard.html', {'participants':participants})




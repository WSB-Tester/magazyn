# To jest grupa Tester WSB, ktora zalozylem zebysmy mogli wspolnie pogrzebac w jakichs projektach albo cos podlubac :)

Zeby to bylo czytelne, bo podglad zbija tekst w calosc polecam kliknac w olowek - edycje tego pliku, aby sobie przejrzec i bylo wygodnie :)

## WAZNE
Stworzylem nam grupe na hangoutsie, zeby mozna sie jakos kulturalnie kontaktowac, polecam wtyczke:
https://chrome.google.com/webstore/detail/google-hangouts/nckgahadagoaajjgafhacjanaoiihapd?hl=pl
(do chroma, do firefoxa/opery powinny byc analogiczne)
Wtyczna dodaje hangouts do przegladarki, wtedy mamy fajne okienko czatu, a mysle, ze wspolnie latwiej sie rozwiaze jakies dziwne problemy zamiast samemu sie glowic kilka godzin

# przydatne linki:
https://github.com/wojciech11/se_teaching_vm_images/blob/master/vagrant/ubuntu/Vagrantfile - info od naszego wykladowcy co i jak, albo mozna pobrac repo i odpalic z terminala albo recznie sobie poinstalowac potrzebne rzeczy
https://code.visualstudio.com/docs/setup/linux - VSC - visual studio code, ja korzystam bo ma min. wbudowany terminal
https://itsfoss.com/install-atom-ubuntu/ - atom, ten ktory byl na zajeciach i jest na virtualce na WSB

Podstawy gita:
$git init - inicjalizacja repo, mozna w tej grupie sobie tworzyc repozytoria itd, mamy nielimitowane repo publiczne
$git status - warto sprawdzac co mamy do zacommitowania, git status pokazuje nam rowniez aktywny branch w gicie (pierwsza linijka, np "On branch master" albo "On branch maniek")
$git add <nazwa-pliku> (raczej nie uzywajmy git add . bo sie moze pokaszanic)
$git commit -m "komentarz" (dobre praktyki mowia, zeby komentarze mialy strukture typu "Add costam costam" - co wynika ze stwierdzenia "When merged this commit will <komentarz> - jednakze nie musimy sie koniecznie do tego stosowac)

Zaawansowany git:

$ git checkout -b <nazwa-brancha> - tworzy nowy branch
$ git branch - wyswietla wszystkie brache w aktualnym repozytorium
$ git checkout <nazwa-brancha> - zmienia nasz aktywny branch na ten podany jako nazwa
                                czyli przykladowo $ git checkout maniek -> przelaczy nas na brancha 'maniek'. Warto zawsze sprawdzic komenda git branch na ktory branch pushujemy zmiany :) 
                                Przydatny link: https://git-scm.com/book/pl/v1/Ga%C5%82%C4%99zie-Gita-Podstawy-rozga%C5%82%C4%99ziania-i-scalania




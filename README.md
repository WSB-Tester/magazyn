# To jest grupa Tester WSB, ktora zalozylem zebysmy mogli wspolnie pogrzebac w jakichs projektach albo cos podlubac :)

Slowem wstepu - na branchu master jest wrzucony nasz kod z zajec z magazynem, ja sobie go jeszcze sklonowalem na brancha maniek - to bedzie docelowo moj branch 'produkcyjny' naszej wypasionej aplikacji :)

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


Wtyczka dodaje hangouts do przegladarki, wtedy mamy fajne okienko czatu, a mysle, ze wspolnie latwiej sie rozwiaze jakies dziwne problemy zamiast samemu sie glowic kilka godzin

# przydatne linki:
https://github.com/wojciech11/se_teaching_vm_images/blob/master/vagrant/ubuntu/Vagrantfile - info od naszego wykladowcy co i jak, albo mozna pobrac repo i odpalic z terminala albo recznie sobie poinstalowac potrzebne rzeczy

https://code.visualstudio.com/docs/setup/linux - VSC - visual studio code, ja korzystam bo ma min. wbudowany terminal

https://itsfoss.com/install-atom-ubuntu/ - atom, ten ktory byl na zajeciach i jest na virtualce na WSB

Podstawy gita:

$ git clone <link> - pozwala na pobranie zewnetrznego repozytorium z sieci - link mamy np. na githubie na widoku ogolnym repozytorium

$ git init - inicjalizacja repo, mozna w tej grupie sobie tworzyc repozytoria itd, mamy nielimitowane repo publiczne

$ git status - warto sprawdzac co mamy do zacommitowania, git status pokazuje nam rowniez aktywny branch w gicie (pierwsza linijka, np "On branch master" albo "On branch maniek")

$ git add <nazwa-pliku> (raczej nie uzywajmy git add . bo sie moze pokaszanic)

$ git commit -m "komentarz" (dobre praktyki mowia, zeby komentarze mialy strukture typu "Add costam costam" - co wynika ze stwierdzenia "When merged this commit will <komentarz> - jednakze nie musimy sie koniecznie do tego stosowac)

$ git pull - pobiera nam zmiany z githuba na aktualnym branchu


Zaawansowany git:

$ git checkout -b <nazwa-brancha> - tworzy nowy branch

$ git branch - wyswietla wszystkie brache w aktualnym repozytorium
$ git checkout <nazwa-brancha> - zmienia nasz aktywny branch na ten podany jako nazwa
                                czyli przykladowo $ git checkout maniek -> przelaczy nas na brancha 'maniek'. Warto zawsze sprawdzic komenda git branch na ktory branch pushujemy zmiany :) 
                                Przydatny link: https://git-scm.com/book/pl/v1/Ga%C5%82%C4%99zie-Gita-Podstawy-rozga%C5%82%C4%99ziania-i-scalania


$ git branch - wyswietla wszystkie brache w aktualnym repozytorium

$ git checkout <nazwa-brancha> - zmienia nasz aktywny branch na ten podany jako nazwa

czyli przykladowo $ git checkout maniek -> przelaczy nas na brancha 'maniek'. Warto zawsze sprawdzic komenda git branch na ktory branch pushujemy zmiany :) 
                                
Przydatny link: https://git-scm.com/book/pl/v1/Ga%C5%82%C4%99zie-Gita-Podstawy-rozga%C5%82%C4%99ziania-i-scalania



Zadanie :)

Stworzyc sobie folder na komputerze

Sklonowac sobie do tego folderu nasze repozytorium 'magazyn' z projektu (link: https://github.com/WSB-Tester/magazyn.git)

Pobrac sobie to repozytorium na lokalny komputer (git pull)

Stworzyc sobie swoj branch (np. od imienia, ksywy, czego tam chcecie)


A potem to mozna sobie przelaczyc sie na branch 'maniek', poedytowac cos, potem przed git add, git commit przelaczyc sie na swoj branch, ktory juz stworzyliscie i tam wrzucic zmiany :) 

Jak juz bedzie tak daleko, to ogarniemy merge do 'mastera' zeby sobie mozna bylo fajnie pykac z tym kodem :) 





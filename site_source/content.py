"""English and German copy for the Safe AI Bremen website."""

OPERATOR_NAME = "Valeriya Zelenkova"
OPERATOR_EMAIL = "vzelenkova03@gmail.com"
OPERATOR_ADDRESS = ("c/o AI Safety Aachen e. V.", "Hünefeldstraße 35", "52068 Aachen", "Deutschland")
BREMEN_COMPLAINTS = "https://www.datenschutz.bremen.de/wir-ueber-uns/online-meldungen/beschwerdeformular-15253"

COFOUNDERS = (
    (OPERATOR_NAME, OPERATOR_EMAIL),
    ("Fatema Zara Hussain", "fzh647@gmail.com"),
)

FOUNDER_CONTACT = {
    "en": {
        "title": "Get in touch",
        "text": "Have a question about AI safety or want to learn more about Safe AI Bremen? Email either of us. We’d love to hear from you.",
        "role": "Co-founder",
    },
    "de": {
        "title": "Kontakt",
        "text": "Schreib uns gerne, wenn du Fragen zur KI-Sicherheit hast oder mehr über Safe AI Bremen erfahren möchtest.",
        "role": "Mitgründerin",
    },
}

PAGES = {
    "en": {
        "imprint": {
            "title": "Imprint",
            "intro": "Provider information under section 18(1) of the German Interstate Media Treaty (MStV).",
            "sections": [
                {
                    "title": "Website operator",
                    "operator_address": True,
                },
                {
                    "title": "About the group",
                    "text": (
                        "Safe AI Bremen is a non‑commercial local group without its own legal form. "
                        "It is not a registered association and does not act on behalf of AI Safety Aachen e. V., "
                        "which provides the postal address above by arrangement only. "
                        "Safe AI Bremen is not affiliated with the University of Bremen."
                    ),
                },
            ],
        },
        "privacy": {
            "title": "Privacy",
            "intro": "How we handle your data when you visit this website or contact Safe AI Bremen.",
            "sections": [
                {
                    "title": "Who is responsible?",
                    "operator_address": True,
                },
                {
                    "title": "When you visit the site",
                    "paragraphs": [
                        "When you visit the site on GitHub Pages, your browser sends GitHub your IP address "
                        "and the file it is requesting. GitHub logs visitor IP addresses for security. "
                        "Our legal basis for delivering the site is our legitimate interest in making it "
                        "available securely and reliably (Article 6(1)(f) GDPR).",
                        "GitHub bases retention on the purpose of the processing and applicable legal "
                        "obligations. It does not specify a fixed retention period for Pages IP logs in "
                        "its documentation. Opening a local copy of this site requires no connection to GitHub.",
                        "The site serves its own fonts, images and scripts. We use no analytics, tracking "
                        "cookies or third-party embeds. Following an external event or resource link takes "
                        "you to the linked provider, whose privacy policy applies there.",
                    ],
                    "links": [
                        ("How GitHub Pages handles visitor data", "https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages#data-collection"),
                    ],
                },
                {
                    "title": "When you contact us",
                    "paragraphs": [
                        "You can write to either founder. When you send an email, the founder you address "
                        "receives your email address, any name you provide, your message and any attachments. "
                        "Google provides our Gmail mailboxes and processes the message for delivery and storage. "
                        "Contact is voluntary. We need a return address if you would like a reply.",
                        "We use correspondence to answer your enquiry and coordinate any follow-up you request. "
                        "That is our legitimate interest under Article 6(1)(f) GDPR. We keep correspondence "
                        "for as long as needed for that purpose, or longer if a legal obligation or a legal "
                        "claim requires it. If you write by post, AI Safety Aachen e. V. may receive the envelope "
                        "at the address above for forwarding to Valeriya.",
                    ],
                    "links": [("Google’s privacy policy", "https://policies.google.com/privacy?hl=en")],
                },
                {
                    "title": "International transfers",
                    "text": (
                        "GitHub and Google may process data outside the European Economic Area, including "
                        "in the United States. For transfers to participating US organisations, the providers "
                        "describe relying on the EU–US Data Privacy Framework. For other transfers they may "
                        "use the European Commission’s standard contractual clauses. The providers explain "
                        "which safeguards apply and where to find them."
                    ),
                    "links": [
                        ("GitHub’s privacy statement", "https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement#international-data-transfers"),
                        ("Google’s data transfer safeguards", "https://policies.google.com/privacy/frameworks?hl=en"),
                    ],
                },
                {
                    "title": "Your rights",
                    "text": (
                        "You can ask Valeriya for access to your personal data, correction, erasure or a "
                        "restriction on processing. Where the legal conditions apply, you also have a right "
                        "to data portability. Use the contact details above to exercise your rights. You can "
                        "lodge a complaint with a data protection authority, including the one in Bremen."
                    ),
                    "links": [("Bremen data protection authority’s complaint form", BREMEN_COMPLAINTS)],
                },
                {
                    "title": "Your right to object",
                    "text": (
                        "You may object at any time, on grounds relating to your particular situation, to "
                        "processing based on our legitimate interests (Article 21 GDPR). We will stop that "
                        "processing unless we can demonstrate compelling overriding grounds or need the "
                        "data to establish, exercise or defend legal claims."
                    ),
                },
            ],
        },
        "about": {
            "title": "Safe AI Bremen",
            "intro": (
                "We’re a local community for people in Bremen who want to understand "
                "the risks of advanced AI and what we can do about them."
            ),
            "sections": [
                {
                    "title": "The questions we ask",
                    "items": [
                        {
                            "title": "Can we tell when a system will fail?",
                            "text": (
                                "An AI model can pass a test and still make mistakes in everyday use. "
                                "How can researchers design tests that reveal those gaps before deployment?"
                            ),
                        },
                        {
                            "title": "Who gets to decide what is safe enough?",
                            "text": (
                                "Releasing a system affects people beyond the team that built it. "
                                "What evidence should developers share, and who should review it?"
                            ),
                        },
                    ],
                },
                {
                    "title": "Who belongs here?",
                    "text": (
                        "You might come to these questions through computer science, public policy, "
                        "philosophy or your own experience using AI. You’re welcome to start "
                        "with a question you haven’t found an answer to."
                    ),
                },
                {"founders": True},
            ],
        },
        "events": {
            "title": "Talks and meetups",
            "intro": "Find local announcements and selected online talks you can join from Bremen.",
            "sections": [
                {
                    "title": "In Bremen",
                    "text": "We’re planning our first event in Bremen. We’ll share the date and venue here once they’re confirmed.",
                },
                {
                    "title": "Online with Safe AI Germany",
                    "items": [
                        {
                            "title": "Is Kimi K3.1 Benchmaxxed?",
                            "text": (
                                "Joachim Schaeffer explains how a model appeared to know rules "
                                "missing from its instructions, and what that means for benchmark scores."
                            ),
                            "date": "2026-11-24",
                            "meta": "24 November 2026 · 18:00–19:00 CET · Online",
                            "href": "https://luma.com/7eqao0gc",
                            "link": "Event details on Luma",
                        },
                        {
                            "title": "Telling FIBS",
                            "text": (
                                "Alex Spies and Oskar Hollinsworth discuss how looking inside "
                                "a model can reveal deceptive behaviour that its outputs conceal."
                            ),
                            "date": "2026-12-09",
                            "meta": "9 December 2026 · 18:00–19:00 CET · Online",
                            "href": "https://luma.com/yapvsthe",
                            "link": "Event details on Luma",
                        },
                    ],
                },
            ],
        },
        "resources": {
            "title": "Explore AI safety",
            "intro": (
                "Start with an introduction, find a research question to follow, "
                "or look up the evidence behind a claim."
            ),
            "sections": [
                {
                    "title": "Reading list",
                    "items": [
                        {
                            "title": "Why AI safety matters",
                            "meta": "Introduction · Safe AI Germany",
                            "text": (
                                "David Williams-King explains how harm can arise from misuse, "
                                "systems pursuing unintended goals, and the ways people and institutions interact."
                            ),
                            "href": "https://safeaigermany.org/why-ai-safety/",
                            "link": "Read the introduction",
                        },
                        {
                            "title": "A concept map of AI safety",
                            "meta": "Reference · Safe AI Germany",
                            "text": (
                                "Pick a term such as alignment or oversight and follow it from a "
                                "working definition to research papers and open questions."
                            ),
                            "href": "https://safeaigermany.org/concept-map/",
                            "link": "Browse the concept map",
                        },
                        {
                            "title": "International AI Safety Report 2026",
                            "meta": "Research review · International team led by Yoshua Bengio",
                            "text": (
                                "Read the executive summary for an overview of general-purpose AI "
                                "capabilities, emerging risks and the evidence for safeguards."
                            ),
                            "href": "https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026",
                            "link": "Open the report",
                        },
                    ],
                },
            ],
        },
        "get-involved": {
            "title": "Connect in Bremen",
            "intro": (
                "Have a question you’d like to discuss with others in Bremen, "
                "a paper to read together or an idea for a talk? We’d like to hear from you."
            ),
            "sections": [
                {"founders": True},
                {
                    "title": "Ways to get started",
                    "items": [
                        {
                            "title": "Join a talk",
                            "text": "See which talks you can attend online and check for local meetup dates.",
                            "href": "events",
                            "link": "View events",
                        },
                        {
                            "title": "Find a starting point",
                            "text": "Choose a question from our reading list to explore at your own pace.",
                            "href": "resources",
                            "link": "Explore the reading list",
                        },
                    ],
                },
            ],
        },
    },
    "de": {
        "imprint": {
            "title": "Impressum",
            "intro": "Anbieterkennzeichnung gemäß § 18 Abs. 1 Medienstaatsvertrag (MStV).",
            "sections": [
                {
                    "title": "Betreiberin der Website",
                    "operator_address": True,
                },
                {
                    "title": "Über die Gruppe",
                    "text": (
                        "Safe AI Bremen ist eine nichtkommerzielle lokale Gruppe ohne eigene Rechtsform. "
                        "Sie ist kein eingetragener Verein und handelt nicht im Namen von AI Safety Aachen e. V. "
                        "Der Verein stellt nach Absprache ausschließlich die oben genannte Postanschrift zur "
                        "Verfügung. Safe AI Bremen ist der Universität Bremen nicht angegliedert."
                    ),
                },
            ],
        },
        "privacy": {
            "title": "Datenschutz",
            "intro": "So verarbeiten wir deine Daten, wenn du diese Website besuchst oder Safe AI Bremen kontaktierst.",
            "sections": [
                {
                    "title": "Wer ist verantwortlich?",
                    "operator_address": True,
                },
                {
                    "title": "Beim Besuch der Website",
                    "paragraphs": [
                        "Wenn du die Website über GitHub Pages besuchst, übermittelt dein Browser deine "
                        "IP-Adresse und die angeforderte Datei an GitHub. GitHub protokolliert die IP-Adressen "
                        "der Besucherinnen und Besucher aus Sicherheitsgründen. Rechtsgrundlage für die "
                        "Bereitstellung der Website ist unser berechtigtes Interesse an ihrem sicheren und "
                        "zuverlässigen Betrieb (Art. 6 Abs. 1 Buchst. f DSGVO).",
                        "GitHub richtet die Speicherdauer nach dem Verarbeitungszweck und gesetzlichen "
                        "Pflichten aus. Für IP-Protokolle von GitHub Pages nennt GitHub keine feste Frist. "
                        "Wenn du die Website als lokale Kopie öffnest, ist keine Verbindung zu GitHub nötig.",
                        "Schriften, Bilder und Skripte kommen direkt von dieser Website. Wir verwenden keine "
                        "Analysewerkzeuge, Tracking-Cookies oder eingebetteten Inhalte Dritter. Wenn du einem "
                        "externen Link zu einer Veranstaltung oder einem Lesetipp folgst, gelangst du zur "
                        "Website des jeweiligen Anbieters. Dort gilt dessen Datenschutzerklärung.",
                    ],
                    "links": [
                        ("Datenerfassung bei GitHub Pages", "https://docs.github.com/de/pages/getting-started-with-github-pages/what-is-github-pages"),
                    ],
                },
                {
                    "title": "Wenn du uns kontaktierst",
                    "paragraphs": [
                        "Du kannst beiden Gründerinnen schreiben. Die jeweils angeschriebene Gründerin erhält "
                        "deine E-Mail-Adresse, deinen gegebenenfalls angegebenen Namen, deine Nachricht und "
                        "etwaige Anhänge. Unsere Postfächer liegen bei Gmail. Google verarbeitet die Nachricht "
                        "zur Zustellung und Speicherung. Der Kontakt ist freiwillig. Für eine Antwort brauchen "
                        "wir eine Rückadresse.",
                        "Wir verwenden deine Nachricht, um dein Anliegen zu beantworten und die von dir "
                        "gewünschten nächsten Schritte abzustimmen. Darin liegt unser berechtigtes Interesse "
                        "gemäß Art. 6 Abs. 1 Buchst. f DSGVO. Wir bewahren den Schriftverkehr so lange auf, wie "
                        "dies dafür erforderlich ist. Eine längere Aufbewahrung kommt in Betracht, wenn eine "
                        "Rechtspflicht oder ein Rechtsanspruch sie erfordert. Bei einem Brief an die oben "
                        "genannte Anschrift kann AI Safety Aachen e. V. den Umschlag zur Weiterleitung an "
                        "Valeriya entgegennehmen.",
                    ],
                    "links": [("Datenschutzerklärung von Google", "https://policies.google.com/privacy?hl=de")],
                },
                {
                    "title": "Internationale Datenübermittlung",
                    "text": (
                        "GitHub und Google können Daten außerhalb des Europäischen Wirtschaftsraums verarbeiten, "
                        "auch in den USA. Für Übermittlungen an teilnehmende US-Organisationen berufen sich die "
                        "Anbieter auf den EU–US-Datenschutzrahmen. Bei anderen Übermittlungen können sie die "
                        "Standardvertragsklauseln der Europäischen Kommission verwenden. Die Anbieter erläutern, "
                        "welche Garantien jeweils gelten und wo du sie einsehen kannst."
                    ),
                    "links": [
                        ("Datenschutzerklärung von GitHub", "https://docs.github.com/de/site-policy/privacy-policies/github-general-privacy-statement"),
                        ("Googles Garantien für Datenübermittlungen", "https://policies.google.com/privacy/frameworks?hl=de"),
                    ],
                },
                {
                    "title": "Deine Rechte",
                    "text": (
                        "Du kannst von Valeriya Auskunft über deine personenbezogenen Daten, ihre Berichtigung "
                        "oder Löschung sowie die Einschränkung der Verarbeitung verlangen. Unter den gesetzlichen "
                        "Voraussetzungen hast du auch das Recht auf Datenübertragbarkeit. Du erreichst Valeriya "
                        "über die oben genannten Kontaktdaten. Du kannst dich bei einer Datenschutzaufsichtsbehörde "
                        "beschweren, zum Beispiel bei der in Bremen."
                    ),
                    "links": [("Beschwerde bei der Bremer Datenschutzaufsicht", BREMEN_COMPLAINTS)],
                },
                {
                    "title": "Dein Widerspruchsrecht",
                    "text": (
                        "Du kannst der Verarbeitung aufgrund unserer berechtigten Interessen aus Gründen, die "
                        "sich aus deiner besonderen Situation ergeben, jederzeit widersprechen (Art. 21 DSGVO). "
                        "Wir beenden diese Verarbeitung, es sei denn, wir können zwingende, überwiegende "
                        "schutzwürdige Gründe nachweisen oder benötigen die Daten zur Geltendmachung, Ausübung "
                        "oder Verteidigung von Rechtsansprüchen."
                    ),
                },
            ],
        },
        "about": {
            "title": "Safe AI Bremen",
            "intro": (
                "Wir sind eine Gruppe für alle in Bremen, die verstehen wollen, welche Risiken "
                "von fortgeschrittener KI ausgehen und was wir dagegen tun können."
            ),
            "sections": [
                {
                    "title": "Fragen, die uns beschäftigen",
                    "items": [
                        {
                            "title": "Woran erkennen wir, wann ein System versagt?",
                            "text": (
                                "Ein KI-Modell kann einen Test bestehen und im Alltag trotzdem Fehler machen. "
                                "Wie lassen sich Tests entwickeln, die solche Schwächen schon vor dem Einsatz aufdecken?"
                            ),
                        },
                        {
                            "title": "Wer entscheidet, was sicher genug ist?",
                            "text": (
                                "Der Einsatz eines Systems betrifft auch Menschen außerhalb des Entwicklungsteams. "
                                "Welche Nachweise sollten die Verantwortlichen vorlegen und wer sollte sie prüfen?"
                            ),
                        },
                    ],
                },
                {
                    "title": "Wer kann mitmachen?",
                    "text": (
                        "Vielleicht kennst du diese Fragen aus der Informatik, der Politik oder der Philosophie. "
                        "Vielleicht sind sie dir beim Umgang mit KI begegnet. Auch mit einer ersten offenen "
                        "Frage bist du hier willkommen."
                    ),
                },
                {"founders": True},
            ],
        },
        "events": {
            "title": "Vorträge und Treffen",
            "intro": "Hier findest du Termine in Bremen und ausgewählte Vorträge, an denen du online teilnehmen kannst.",
            "sections": [
                {
                    "title": "In Bremen",
                    "text": "Wir planen unsere erste Veranstaltung in Bremen. Sobald Termin und Ort feststehen, geben wir sie hier bekannt.",
                },
                {
                    "title": "Online bei Safe AI Germany",
                    "items": [
                        {
                            "title": "Is Kimi K3.1 Benchmaxxed?",
                            "text": (
                                "Joachim Schaeffer zeigt, wie ein Modell offenbar Bewertungsregeln kannte, die in "
                                "seinen Anweisungen fehlten. Was sagt das über die Aussagekraft der Testergebnisse?"
                            ),
                            "date": "2026-11-24",
                            "meta": "24. November 2026 · 18:00–19:00 Uhr MEZ · Online",
                            "href": "https://luma.com/7eqao0gc",
                            "link": "Veranstaltung auf Luma ansehen",
                        },
                        {
                            "title": "Telling FIBS",
                            "text": (
                                "Alex Spies und Oskar Hollinsworth untersuchen, wie sich Täuschungsverhalten "
                                "im Inneren eines Modells erkennen lässt, auch wenn seine Antworten unauffällig sind."
                            ),
                            "date": "2026-12-09",
                            "meta": "9. Dezember 2026 · 18:00–19:00 Uhr MEZ · Online",
                            "href": "https://luma.com/yapvsthe",
                            "link": "Veranstaltung auf Luma ansehen",
                        },
                    ],
                },
            ],
        },
        "resources": {
            "title": "KI-Sicherheit verstehen",
            "intro": (
                "Hier kannst du dir einen Überblick verschaffen, einer Forschungsfrage nachgehen "
                "oder nachlesen, welche Erkenntnisse hinter einer Behauptung stehen."
            ),
            "sections": [
                {
                    "title": "Leseliste",
                    "items": [
                        {
                            "title": "Warum KI-Sicherheit wichtig ist",
                            "meta": "Einführung · Safe AI Germany",
                            "text": (
                                "David Williams-King erklärt drei Quellen von Risiken. Dazu zählen Missbrauch, "
                                "Systeme, die unbeabsichtigte Ziele verfolgen, und das Zusammenspiel von Menschen und Institutionen."
                            ),
                            "href": "https://safeaigermany.org/de/why-ai-safety/",
                            "link": "Einführung lesen",
                        },
                        {
                            "title": "Begriffe der KI-Sicherheit",
                            "meta": "Nachschlagewerk · Safe AI Germany",
                            "text": (
                                "Die interaktive Übersicht erklärt Begriffe wie Alignment und Scalable Oversight. Zu jedem Thema "
                                "findest du Definitionen, Fachartikel und offene Forschungsfragen."
                            ),
                            "href": "https://safeaigermany.org/de/concept-map/",
                            "link": "Begriffe erkunden",
                        },
                        {
                            "title": "International AI Safety Report 2026",
                            "meta": "Forschungsüberblick · Internationales Team unter Leitung von Yoshua Bengio",
                            "text": (
                                "Die englische Kurzfassung fasst zusammen, was vielseitig einsetzbare KI-Systeme können, "
                                "welche Risiken sich abzeichnen und was über die Wirksamkeit von Schutzmaßnahmen bekannt ist."
                            ),
                            "href": "https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026",
                            "link": "Bericht lesen",
                        },
                    ],
                },
            ],
        },
        "get-involved": {
            "title": "In Bremen mitmachen",
            "intro": (
                "Hast du eine Frage, über die du mit anderen in Bremen sprechen möchtest, einen Lesetipp "
                "oder eine Idee für einen Vortrag? Wir freuen uns, von dir zu hören."
            ),
            "sections": [
                {"founders": True},
                {
                    "title": "So kannst du einsteigen",
                    "items": [
                        {
                            "title": "Einen Vortrag besuchen",
                            "text": "Hier findest du Online-Vorträge und Ankündigungen für Treffen in Bremen.",
                            "href": "events",
                            "link": "Veranstaltungen ansehen",
                        },
                        {
                            "title": "Ein Thema erkunden",
                            "text": "Such dir aus der Leseliste eine Frage aus, der du nachgehen möchtest.",
                            "href": "resources",
                            "link": "Zur Leseliste",
                        },
                    ],
                },
            ],
        },
    },
}

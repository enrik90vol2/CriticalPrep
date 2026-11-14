#!/usr/bin/env python3
"""Genera la pagina di prodotto di CriticalPrep in italiano (index.html) e inglese (en/index.html).

Un solo modello HTML, i testi delle due lingue in TEXT. Uso:  python3 tools/build_site.py
Nessuna dipendenza: basta il python3 di sistema.
"""
from pathlib import Path
import html

ROOT = Path(__file__).resolve().parent.parent
REPO = "https://github.com/enrik90vol2/CriticalPrep"
SITE = "https://enrik90vol2.github.io/CriticalPrep/"
VERSION = "0.8"
DL_MAC = f"{REPO}/releases/latest/download/CriticalPrep-macOS.dmg"
DL_WIN = f"{REPO}/releases/latest/download/CriticalPrep-Windows-Setup.exe"
RELEASES = f"{REPO}/releases"

APPLE = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M16.4 12.6c0-2.4 2-3.6 2.1-3.7-1.1-1.7-2.9-1.9-3.5-1.9-1.5-.2-2.9.9-3.7.9-.8 0-1.9-.9-3.2-.8-1.6 0-3.1 1-4 2.4-1.7 3-.4 7.3 1.2 9.7.8 1.2 1.8 2.5 3 2.4 1.2 0 1.7-.8 3.1-.8 1.5 0 1.9.8 3.2.8 1.3 0 2.2-1.2 3-2.4.9-1.4 1.3-2.7 1.3-2.8 0 0-2.5-1-2.5-3.8zM14 5.4c.7-.8 1.1-1.9 1-3-1 0-2.1.7-2.8 1.5-.6.7-1.2 1.8-1 2.9 1 .1 2.1-.6 2.8-1.4z"/></svg>'
WINDOWS = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M3 5.1l7.4-1v7.2H3V5.1zm0 13.8l7.4 1v-7.1H3v6.1zm8.2 1.1L21 21.4v-8.6h-9.8V20zm0-15.9v7.3H21V2.6l-9.8 1.5z"/></svg>'
SHIELD = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3l8 3v6c0 4.5-3.4 8.3-8 9-4.6-.7-8-4.5-8-9V6l8-3z"/><path d="M9 12l2 2 4-4"/></svg>'
INFO = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 11v6M12 7.5v.5"/></svg>'

TEXT = {
    "it": {
        "html_lang": "it",
        "title": "CriticalPrep — L'assistente per Game Master",
        "description": "CriticalPrep è l'app per Mac e Windows che aiuta i Game Master di qualsiasi gioco di ruolo a preparare la campagna, giocare la sessione e aggiornare la Wiki con l'AI. BETA gratuita con AI inclusa.",
        "skip": "Salta al contenuto",
        "nav": [("#come-funziona", "Come funziona"), ("#funzioni", "Funzioni"), ("#ai", "Intelligenza artificiale"), ("#faq", "Domande")],
        "nav_download": "Scarica",
        "badge": "Versione di prova gratuita · AI inclusa",
        "hero_title": "Prepara meno.<br><em>Gioca di più.</em>",
        "hero_lead": "CriticalPrep è l'assistente per i Game Master di giochi di ruolo da tavolo. Tiene in ordine la tua campagna, ti aiuta durante la sessione e, quando avete finito, aggiorna la Wiki con quello che è successo. Funziona con qualsiasi sistema di gioco.",
        "dl_mac": "Scarica per Mac", "dl_win": "Scarica per Windows",
        "hero_note": "Gratis durante la BETA. Nessun account, nessuna carta di credito.",
        "mock": {
            "camp": "La Costa delle Braci", "sec_campaign": "Campagna", "details": "Dettagli", "import": "Importa risorse",
            "wb": "World Building", "sec_session": "Sessione", "plan": "Pianifica sessione", "live": "In sessione",
            "post": "Post-sessione", "wiki": "Wiki",
            "wb_title": "World Building", "wb_sub": "24 schede · 6 quest attive",
            "e1": ("PNG", "Mira Valdis", "Contrabbandiera, debitrice della Gilda"),
            "e2": ("Luogo", "Porto Cenere", "Città portuale costruita sulla lava"),
            "e3": ("Fazione", "La Gilda del Sale", "Controlla i moli e le rotte"),
            "e4": ("Quest", "La chiave della torre", "Chi l'ha rubata al faro?"),
            "post_title": "Post-sessione · Sessione 5", "post_sub": "L'AI propone 4 modifiche: scegli tu quali applicare",
            "p1": ("Mira Valdis", "Ora è alleata del party: ha restituito la chiave."),
            "p2": ("La chiave della torre", "Quest completata nella sessione 5."),
            "p3": ("Nuova scheda: Capitano Orsk", "Comandante della flotta della Gilda."),
            "live_title": "In sessione · Sessione 6", "live_sub": "Registrazione da Discord · 4 giocatori",
            "rec": "In registrazione 01:42:18",
            "q": "Chi ha la chiave della torre?",
            "a": "Mira Valdis l'ha restituita al party nella sessione 5. Prima era custodita al faro di Porto Cenere.",
            "wiki_title": "Mira Valdis", "wiki_sub": "PNG · Porto Cenere · Gilda del Sale",
            "wiki_text": "Contrabbandiera cresciuta tra i moli di [[Porto Cenere]]. Ha un debito con la [[Gilda del Sale]] e conosce le rotte nascoste verso il faro.",
            "wiki_tag": "Aggiornata dopo la sessione 5",
        },
        "what_eyebrow": "Cos'è",
        "what_title": "Il tuo secondo cervello da Game Master",
        "what_lead": "Ogni campagna accumula nomi, luoghi, segreti e promesse fatte al tavolo. CriticalPrep li raccoglie in un unico posto e ti aiuta in tre momenti.",
        "pillars": [
            ("Prepara", "Costruisci il mondo con PNG, luoghi, fazioni, quest e divinità. Importa i tuoi appunti e lascia che l'AI li trasformi in schede ordinate."),
            ("Gioca", "Al tavolo trovi qualsiasi scheda in un attimo, chiedi alla campagna chi sa cosa e registri la sessione, anche su Discord."),
            ("Aggiorna", "Dopo la sessione l'AI legge note e trascrizione e propone le modifiche alle schede. Tu scegli quali tenere, una per una."),
        ],
        "how_eyebrow": "Come funziona",
        "how_title": "Una campagna, dall'idea alla sessione dopo",
        "how_lead": "CriticalPrep segue il ritmo naturale di una campagna. Al primo avvio una breve introduzione ti mostra ogni sezione.",
        "steps": [
            ("Prima", "Crea la campagna", "Titolo, premessa, sistema di gioco, tono e membri del party. Se vuoi, una creazione guidata ti fa le domande giuste."),
            ("Prima", "Importa i tuoi materiali", "Appunti, PDF (anche scansionati), documenti Word, immagini o intere cartelle: diventano schede e domande aperte."),
            ("Prima", "Costruisci il mondo", "Crea schede a mano o con il wizard, che ti intervista e prepara la scheda. Collega tutto con i link tra le schede."),
            ("Prima della sessione", "Pianifica", "Scrivi la scaletta: l'AI controlla che non contraddica quello che è già successo nella campagna."),
            ("Al tavolo", "Gioca", "Cerca al volo, chiedi \"Chi ha la chiave della torre?\" e registra l'audio dal microfono o da Discord."),
            ("Dopo", "Aggiorna la Wiki", "Riassunto e modifiche proposte alle schede: approvi quelle giuste e puoi sempre annullarle."),
        ],
        "feat_eyebrow": "Funzioni",
        "feat_title": "Tutto quello che serve a un Game Master",
        "f1_eyebrow": "Campagna e World Building",
        "f1_title": "Un mondo ordinato, non un mucchio di appunti",
        "f1": [
            ("Schede per tutto", "PNG, luoghi, fazioni, quest, divinità e oggetti, con immagini, mappe e collegamenti tra le schede."),
            ("Importa quello che hai già", "Appunti sparsi, PDF dei manuali, documenti Word e cartelle intere: l'AI ne ricava schede e segnala cosa manca."),
            ("Wizard di World Building", "Descrivi un'idea in una riga: il wizard ti fa domande mirate e scrive la scheda completa."),
            ("Archi narrativi", "Se ti servono, segui i fili della storia con tappe e finale previsto."),
        ],
        "f2_eyebrow": "Durante la sessione",
        "f2_title": "La risposta giusta mentre i giocatori aspettano",
        "f2": [
            ("Chiedi alla campagna", "Fai una domanda in linguaggio naturale e ottieni la risposta dalle tue schede e dalle sessioni passate."),
            ("Ricerca immediata", "Ogni PNG, luogo o quest a portata di mano, senza sfogliare quaderni."),
            ("Registrazione e trascrizione", "Registra dal microfono per il gioco al tavolo, oppure da Discord con una traccia separata per ogni giocatore. La trascrizione avviene sul tuo computer."),
        ],
        "f3_eyebrow": "Dopo la sessione",
        "f3_title": "La Wiki si aggiorna. Tu decidi cosa cambia.",
        "f3": [
            ("Modifiche proposte, non imposte", "L'AI confronta la sessione con le schede e propone aggiornamenti precisi. Le approvi una per una e puoi annullarle."),
            ("Riassunti pronti da condividere", "Esporta il riassunto della sessione in PDF o Markdown per il tuo gruppo."),
            ("I tuoi file restano tuoi", "Ogni scheda è un file Markdown sul tuo computer: puoi aprirla anche con Obsidian e le modifiche tornano nell'app."),
        ],
        "ai_eyebrow": "Intelligenza artificiale",
        "ai_title": "L'AI che preferisci. O nessuna.",
        "ai_lead": "Le funzioni intelligenti usano il motore che scegli. Senza AI puoi comunque usare schede, Wiki e sessioni.",
        "ai": [
            ("Inclusa nella BETA", "Pronta all'uso", "Scegli \"Abbonamento\" nelle impostazioni: l'AI è già attiva, senza chiavi né registrazioni.", "Gratis durante la prova", True),
            ("Sul tuo computer", "Ollama o LM Studio", "Un modello che gira in locale: i testi della campagna non lasciano mai il computer.", "Gratis", False),
            ("Con un account", "OpenRouter", "Accedi con un clic, senza copiare chiavi. Ci sono anche modelli gratuiti.", "Gratis o a consumo", False),
            ("Con la tua chiave", "DeepSeek, OpenAI e altri", "Incolla la chiave del fornitore che usi già. L'app ti spiega passo per passo dove trovarla.", "A consumo, dal fornitore", False),
        ],
        "ai_note": "Con l'AI locale i testi restano sul tuo computer. Con l'AI inclusa o i fornitori cloud vengono inviati al fornitore solo per elaborare la richiesta. Le chiavi che inserisci restano nel portachiavi del sistema.",
        "dl_eyebrow": "Download",
        "dl_title": "Scarica CriticalPrep BETA " + VERSION,
        "dl_lead": "La stessa app su Mac e su Windows, con le stesse funzioni. Gratis durante la versione di prova. Disponibile in italiano, inglese, francese, spagnolo e tedesco.",
        "mac_title": "macOS", "mac_meta": "Mac con Apple silicon o Intel · macOS 14 Sonoma o successivo · DMG, 9 MB",
        "mac_btn": "Scarica per Mac",
        "mac_steps": [
            "Apri il file <strong>CriticalPrep-macOS.dmg</strong> e trascina l'app nella cartella <strong>Applicazioni</strong>.",
            "Al primo avvio macOS può dire che non è in grado di verificare lo sviluppatore: è normale per una BETA distribuita fuori dall'App Store.",
            "Apri <strong>Impostazioni di Sistema › Privacy e sicurezza</strong> e premi <strong>Apri comunque</strong> accanto all'app. Basta farlo una volta.",
        ],
        "mac_req": "Per l'AI locale servono almeno 16 GB di memoria.",
        "win_title": "Windows", "win_meta": "Windows 10 o 11 a 64 bit · installer, 83 MB",
        "win_btn": "Scarica per Windows",
        "win_steps": [
            "Apri <strong>CriticalPrep-Windows-Setup.exe</strong>: l'installazione non chiede permessi di amministratore.",
            "Se compare <strong>\"Windows ha protetto il PC\"</strong>, scegli <strong>Ulteriori informazioni</strong> e poi <strong>Esegui comunque</strong>.",
            "Trovi l'app nel menu Start. La registrazione da Discord è già inclusa nell'installer.",
        ],
        "win_req": "Per l'AI locale servono almeno 16 GB di memoria.",
        "all_versions": "Tutte le versioni e le novità",
        "faq_eyebrow": "Domande frequenti",
        "faq_title": "Domande",
        "faq": [
            ("Quanto costa?", "Durante la BETA CriticalPrep è gratuito, AI inclusa. Puoi anche usare un modello locale gratuito o il tuo account OpenRouter."),
            ("Con quali giochi di ruolo funziona?", "Con tutti: D&D, Pathfinder, Call of Cthulhu, sistemi homebrew. Indichi il sistema nei dettagli della campagna e l'AI ne tiene conto."),
            ("Mi serve una connessione a Internet?", "Solo per l'AI inclusa o per i fornitori cloud. Con un modello locale (Ollama o LM Studio) e senza registrazione da Discord funziona anche offline."),
            ("Dove vengono salvati i miei dati?", "Sul tuo computer, in una cartella che puoi scegliere. Le schede sono file Markdown leggibili con qualsiasi editor o con Obsidian. Non c'è nessun account e nessun cloud di CriticalPrep."),
            ("L'AI può cambiare le mie schede da sola?", "No. Dopo la sessione propone le modifiche e sei tu a scegliere quali applicare. Ogni modifica si può annullare."),
            ("Come funziona la registrazione da Discord?", "Crei un tuo bot Discord, l'app ti guida passo per passo. Il bot entra nel canale vocale e registra ogni giocatore su una traccia separata; la trascrizione avviene sul tuo computer."),
            ("Posso usare la stessa campagna su Mac e Windows?", "Sì: le campagne sono cartelle di file normali. Copiale o mettile in una cartella sincronizzata e le apri su entrambi i sistemi."),
            ("Perché il sistema mostra un avviso alla prima apertura?", "La BETA non è ancora firmata con un certificato a pagamento di Apple o Microsoft, quindi il sistema chiede una conferma la prima volta. Le istruzioni sono qui sopra, nella sezione Download."),
        ],
        "cta_title": "Pronto per la prossima sessione?",
        "cta_text": "Scarica CriticalPrep e prepara la tua campagna con l'AI inclusa nella BETA.",
        "footer_rights": "Fatto per i Game Master.",
        "footer_links": [("#download", "Download"), (RELEASES, "Versioni"), (REPO + "/issues", "Segnala un problema")],
        "other_lang": ("EN", "en/", "English"),
        "this_lang": "IT",
    },
    "en": {
        "html_lang": "en",
        "title": "CriticalPrep — The Game Master's Assistant",
        "description": "CriticalPrep is the Mac and Windows app that helps Game Masters of any tabletop RPG prepare the campaign, run the session and keep the Wiki up to date with AI. Free BETA with AI included.",
        "skip": "Skip to content",
        "nav": [("#how-it-works", "How it works"), ("#features", "Features"), ("#ai", "AI"), ("#faq", "FAQ")],
        "nav_download": "Download",
        "badge": "Free trial version · AI included",
        "hero_title": "Prep less.<br><em>Play more.</em>",
        "hero_lead": "CriticalPrep is the assistant for tabletop RPG Game Masters. It keeps your campaign organised, helps you during the session and, when you're done, updates the Wiki with what happened. It works with any game system.",
        "dl_mac": "Download for Mac", "dl_win": "Download for Windows",
        "hero_note": "Free during the BETA. No account, no credit card.",
        "mock": {
            "camp": "The Ember Coast", "sec_campaign": "Campaign", "details": "Details", "import": "Import Resources",
            "wb": "World Building", "sec_session": "Session", "plan": "Plan Session", "live": "In Session",
            "post": "Post-Session", "wiki": "Wiki",
            "wb_title": "World Building", "wb_sub": "24 entries · 6 active quests",
            "e1": ("NPC", "Mira Valdis", "Smuggler, in debt to the Guild"),
            "e2": ("Place", "Cinder Harbour", "A port city built on lava"),
            "e3": ("Faction", "The Salt Guild", "Controls the docks and the routes"),
            "e4": ("Quest", "The Tower Key", "Who stole it from the lighthouse?"),
            "post_title": "Post-Session · Session 5", "post_sub": "The AI proposes 4 changes: you choose which to apply",
            "p1": ("Mira Valdis", "Now an ally of the party: she returned the key."),
            "p2": ("The Tower Key", "Quest completed in session 5."),
            "p3": ("New entry: Captain Orsk", "Commander of the Guild's fleet."),
            "live_title": "In Session · Session 6", "live_sub": "Recording from Discord · 4 players",
            "rec": "Recording 01:42:18",
            "q": "Who has the tower key?",
            "a": "Mira Valdis gave it back to the party in session 5. Before that it was kept at the Cinder Harbour lighthouse.",
            "wiki_title": "Mira Valdis", "wiki_sub": "NPC · Cinder Harbour · Salt Guild",
            "wiki_text": "A smuggler raised on the docks of [[Cinder Harbour]]. She owes the [[Salt Guild]] and knows the hidden routes to the lighthouse.",
            "wiki_tag": "Updated after session 5",
        },
        "what_eyebrow": "What it is",
        "what_title": "Your Game Master second brain",
        "what_lead": "Every campaign piles up names, places, secrets and promises made at the table. CriticalPrep keeps them in one place and helps you at three moments.",
        "pillars": [
            ("Prepare", "Build the world with NPCs, places, factions, quests and deities. Import your notes and let the AI turn them into tidy entries."),
            ("Play", "At the table, find any entry in a moment, ask the campaign who knows what and record the session, Discord included."),
            ("Update", "After the session the AI reads notes and transcript and proposes changes to your entries. You choose which to keep, one by one."),
        ],
        "how_eyebrow": "How it works",
        "how_title": "A campaign, from first idea to the next session",
        "how_lead": "CriticalPrep follows the natural rhythm of a campaign. On first launch a short introduction walks you through every section.",
        "steps": [
            ("Before", "Create the campaign", "Title, premise, game system, tone and party members. If you like, guided setup asks you the right questions."),
            ("Before", "Import your material", "Notes, PDFs (scanned ones too), Word documents, images or whole folders become entries and open questions."),
            ("Before", "Build the world", "Create entries by hand or with the wizard, which interviews you and drafts the entry. Link everything together."),
            ("Before the session", "Plan", "Write your outline: the AI checks it doesn't contradict what already happened in the campaign."),
            ("At the table", "Play", "Search in a moment, ask \"Who has the tower key?\" and record audio from the microphone or Discord."),
            ("After", "Update the Wiki", "A recap and proposed changes to your entries: approve the right ones and undo any time."),
        ],
        "feat_eyebrow": "Features",
        "feat_title": "Everything a Game Master needs",
        "f1_eyebrow": "Campaign and World Building",
        "f1_title": "An organised world, not a pile of notes",
        "f1": [
            ("Entries for everything", "NPCs, places, factions, quests, deities and items, with images, maps and links between entries."),
            ("Import what you already have", "Loose notes, rulebook PDFs, Word documents and whole folders: the AI turns them into entries and flags what's missing."),
            ("World Building wizard", "Describe an idea in one line: the wizard asks targeted questions and writes the full entry."),
            ("Story arcs", "If you need them, follow the threads of your story with beats and a planned ending."),
        ],
        "f2_eyebrow": "During the session",
        "f2_title": "The right answer while the players wait",
        "f2": [
            ("Ask the campaign", "Ask a question in plain language and get the answer from your entries and past sessions."),
            ("Instant search", "Every NPC, place or quest at hand, no notebooks to flip through."),
            ("Recording and transcription", "Record from the microphone at the table, or from Discord with a separate track for each player. Transcription runs on your computer."),
        ],
        "f3_eyebrow": "After the session",
        "f3_title": "The Wiki updates itself. You decide what changes.",
        "f3": [
            ("Proposed, never imposed", "The AI compares the session with your entries and proposes precise updates. Approve them one by one and undo any time."),
            ("Recaps ready to share", "Export the session recap as PDF or Markdown for your group."),
            ("Your files stay yours", "Every entry is a Markdown file on your computer: open it in Obsidian too, and edits flow back into the app."),
        ],
        "ai_eyebrow": "Artificial intelligence",
        "ai_title": "The AI you prefer. Or none at all.",
        "ai_lead": "The smart features use the engine you choose. Without AI you can still use entries, the Wiki and sessions.",
        "ai": [
            ("Included in the BETA", "Ready to go", "Choose \"Subscription\" in the settings: the AI is already on, no keys or sign-ups.", "Free during the trial", True),
            ("On your computer", "Ollama or LM Studio", "A model running locally: your campaign text never leaves your computer.", "Free", False),
            ("With an account", "OpenRouter", "Sign in with one click, no keys to copy. Free models are available too.", "Free or pay as you go", False),
            ("With your own key", "DeepSeek, OpenAI and more", "Paste the key from the provider you already use. The app shows you step by step where to find it.", "Pay as you go, to the provider", False),
        ],
        "ai_note": "With local AI your text stays on your computer. With the included AI or cloud providers it is sent to the provider only to process the request. The keys you enter stay in your system's keychain.",
        "dl_eyebrow": "Download",
        "dl_title": "Download CriticalPrep BETA " + VERSION,
        "dl_lead": "The same app on Mac and Windows, with the same features. Free during the trial version. Available in Italian, English, French, Spanish and German.",
        "mac_title": "macOS", "mac_meta": "Mac with Apple silicon or Intel · macOS 14 Sonoma or later · DMG, 9 MB",
        "mac_btn": "Download for Mac",
        "mac_steps": [
            "Open <strong>CriticalPrep-macOS.dmg</strong> and drag the app into the <strong>Applications</strong> folder.",
            "On first launch macOS may say it cannot verify the developer: that's expected for a BETA distributed outside the App Store.",
            "Open <strong>System Settings › Privacy &amp; Security</strong> and click <strong>Open Anyway</strong> next to the app. You only need to do this once.",
        ],
        "mac_req": "Local AI needs at least 16 GB of memory.",
        "win_title": "Windows", "win_meta": "Windows 10 or 11, 64-bit · installer, 83 MB",
        "win_btn": "Download for Windows",
        "win_steps": [
            "Open <strong>CriticalPrep-Windows-Setup.exe</strong>: installing doesn't need administrator rights.",
            "If <strong>\"Windows protected your PC\"</strong> appears, choose <strong>More info</strong> and then <strong>Run anyway</strong>.",
            "You'll find the app in the Start menu. Discord recording is already included in the installer.",
        ],
        "win_req": "Local AI needs at least 16 GB of memory.",
        "all_versions": "All versions and release notes",
        "faq_eyebrow": "FAQ",
        "faq_title": "Questions",
        "faq": [
            ("How much does it cost?", "During the BETA CriticalPrep is free, AI included. You can also use a free local model or your OpenRouter account."),
            ("Which RPGs does it work with?", "All of them: D&D, Pathfinder, Call of Cthulhu, homebrew systems. You set the system in the campaign details and the AI takes it into account."),
            ("Do I need an Internet connection?", "Only for the included AI or cloud providers. With a local model (Ollama or LM Studio) and without Discord recording it also works offline."),
            ("Where is my data stored?", "On your computer, in a folder you can choose. Entries are Markdown files readable with any editor or Obsidian. There's no account and no CriticalPrep cloud."),
            ("Can the AI change my entries on its own?", "No. After the session it proposes changes and you choose which to apply. Every change can be undone."),
            ("How does Discord recording work?", "You create your own Discord bot; the app guides you step by step. The bot joins the voice channel and records each player on a separate track; transcription runs on your computer."),
            ("Can I use the same campaign on Mac and Windows?", "Yes: campaigns are folders of ordinary files. Copy them or keep them in a synced folder and open them on both systems."),
            ("Why does my system show a warning the first time?", "The BETA isn't signed with a paid Apple or Microsoft certificate yet, so the system asks for confirmation the first time. The steps are above, in the Download section."),
        ],
        "cta_title": "Ready for your next session?",
        "cta_text": "Download CriticalPrep and prepare your campaign with the AI included in the BETA.",
        "footer_rights": "Made for Game Masters.",
        "footer_links": [("#download", "Download"), (RELEASES, "Releases"), (REPO + "/issues", "Report a problem")],
        "other_lang": ("IT", "../", "Italiano"),
        "this_lang": "EN",
    },
}

IDS = {"it": ("come-funziona", "funzioni"), "en": ("how-it-works", "features")}


def wiki_links(text):
    """[[Nome]] → link evidenziato, come nell'app."""
    out, rest = "", text
    while "[[" in rest and "]]" in rest:
        before, _, tail = rest.partition("[[")
        name, _, rest = tail.partition("]]")
        out += html.escape(before) + f'<a href="#" tabindex="-1" onclick="return false">{html.escape(name)}</a>'
    return out + html.escape(rest)


def sidebar(m, active):
    rows = [("camp", m["camp"], "camp"), ("h", m["sec_campaign"], None), ("details", m["details"], None), ("import", m["import"], None),
            ("wb", m["wb"], None), ("h", m["sec_session"], None), ("plan", m["plan"], None), ("live", m["live"], None),
            ("post", m["post"], None), ("wiki", m["wiki"], None)]
    parts = []
    for key, label, cls in rows:
        if key == "h":
            parts.append(f"<p>{label}</p>")
        else:
            c = "camp" if cls else ("on" if key == active else "")
            parts.append(f'<div class="{c}">{html.escape(label)}</div>')
    return '<aside class="side" aria-hidden="true">' + "".join(parts) + "</aside>"


def window(m, active, body, label):
    return (f'<div class="window" role="img" aria-label="{html.escape(label)}">'
            '<div class="window-bar"><i></i><i></i><i></i><span>CriticalPrep</span></div>'
            f'<div class="window-body">{sidebar(m, active)}<div class="main" aria-hidden="true">{body}</div></div></div>')


def mock_world(m):
    cards = "".join(
        f'<div class="mini"><span class="tag{" gold" if t in ("Quest",) else ""}">{html.escape(t)}</span><b>{html.escape(n)}</b><small>{html.escape(d)}</small></div>'
        for t, n, d in (m["e1"], m["e2"], m["e3"], m["e4"]))
    return f'<h4>{m["wb_title"]}</h4><div class="sub">{m["wb_sub"]}</div><div class="cards">{cards}</div>'


def mock_post(m):
    items = "".join(
        f'<div class="patch"><span class="box{" on" if i < 2 else ""}"></span><div><b>{html.escape(n)}</b><small>{html.escape(d)}</small></div></div>'
        for i, (n, d) in enumerate((m["p1"], m["p2"], m["p3"])))
    return f'<h4>{m["post_title"]}</h4><div class="sub">{m["post_sub"]}</div>{items}'


def mock_live(m):
    heights = [8, 14, 22, 12, 18, 26, 10, 16, 24, 9, 20, 13, 25, 11, 17, 22, 8, 15, 21, 12, 19, 26, 10, 14]
    wave = "".join(f'<i style="height:{h}px"></i>' for h in heights)
    return (f'<h4>{m["live_title"]}</h4><div class="sub">{m["live_sub"]}</div>'
            f'<span class="rec">{m["rec"]}</span><div class="wave">{wave}</div>'
            f'<div class="chat"><div class="bubble q">{html.escape(m["q"])}</div><div class="bubble a">{html.escape(m["a"])}</div></div>')


def mock_wiki(m):
    return (f'<h4>{m["wiki_title"]}</h4><div class="sub">{m["wiki_sub"]}</div>'
            f'<span class="tag ok">{m["wiki_tag"]}</span><p style="margin:8px 0 0">{wiki_links(m["wiki_text"])}</p>')


def features(items):
    return "<ul>" + "".join(f"<li><strong>{t}</strong><span>{d}</span></li>" for t, d in items) + "</ul>"


def page(lang):
    t = TEXT[lang]
    m = t["mock"]
    how_id, feat_id = IDS[lang]
    prefix = "" if lang == "it" else "../"
    other_label, other_href, other_name = t["other_lang"]
    dl_id = "download"
    nav = "".join(f'<a href="{h}">{l}</a>' for h, l in t["nav"])
    pillars = "".join(f'<div class="pillar"><div class="num">{i + 1}</div><h3>{n}</h3><p>{d}</p></div>' for i, (n, d) in enumerate(t["pillars"]))
    steps = "".join(f'<div class="step"><span class="when">{w}</span><h3>{n}</h3><p>{html.escape(d)}</p></div>' for w, n, d in t["steps"])
    ai = "".join(
        f'<div class="ai-card{" star" if star else ""}"><div class="label">{label}</div><h3>{name}</h3><p>{d}</p><p class="price">{price}</p></div>'
        for label, name, d, price, star in t["ai"])
    faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in t["faq"])
    mac_steps = "".join(f"<li>{s}</li>" for s in t["mac_steps"])
    win_steps = "".join(f"<li>{s}</li>" for s in t["win_steps"])
    footer_links = "".join(f'<a href="{h}">{l}</a>' for h, l in t["footer_links"])
    canonical = SITE if lang == "it" else SITE + "en/"
    redirect = """<script>
try {
  var saved = localStorage.getItem("cp-lang");
  if (!saved && !/^it\\b/i.test(navigator.language || "") && location.hash === "") location.replace("en/");
} catch (e) {}
</script>""" if lang == "it" else ""

    return f"""<!doctype html>
<html lang="{t['html_lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t['title']}</title>
<meta name="description" content="{html.escape(t['description'])}">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="it" href="{SITE}">
<link rel="alternate" hreflang="en" href="{SITE}en/">
<link rel="alternate" hreflang="x-default" href="{SITE}">
<meta property="og:type" content="website">
<meta property="og:title" content="{t['title']}">
<meta property="og:description" content="{html.escape(t['description'])}">
<meta property="og:image" content="{SITE}assets/icon.png">
<meta name="theme-color" content="#7c3aed">
<link rel="icon" type="image/png" href="{prefix}assets/favicon.png">
<link rel="apple-touch-icon" href="{prefix}assets/icon.png">
<link rel="stylesheet" href="{prefix}assets/style.css">
{redirect}
</head>
<body>
<a class="skip" href="#main">{t['skip']}</a>
<header class="top">
  <div class="wrap">
    <a class="brand" href="#top"><img src="{prefix}assets/icon.png" alt="" width="30" height="30">CriticalPrep</a>
    <nav class="nav" aria-label="{t['nav_download']}">{nav}</nav>
    <div class="lang" aria-label="Lingua / Language"><span aria-current="true">{t['this_lang']}</span><a href="{other_href}" hreflang="{'en' if lang == 'it' else 'it'}" lang="{'en' if lang == 'it' else 'it'}" title="{other_name}" onclick="try{{localStorage.setItem('cp-lang','{'en' if lang == 'it' else 'it'}')}}catch(e){{}}">{other_label}</a></div>
    <a class="btn btn-primary" href="#{dl_id}">{t['nav_download']}</a>
  </div>
</header>

<main id="main">
<section class="hero" id="top">
  <div class="wrap hero-grid">
    <div>
      <span class="badge"><b>BETA {VERSION}</b>{t['badge']}</span>
      <h1>{t['hero_title']}</h1>
      <p class="lead">{t['hero_lead']}</p>
      <div class="actions">
        <a class="btn btn-primary" href="{DL_MAC}">{APPLE}{t['dl_mac']}</a>
        <a class="btn" href="{DL_WIN}">{WINDOWS}{t['dl_win']}</a>
      </div>
      <p class="small muted">{t['hero_note']}</p>
    </div>
    {window(m, "wb", mock_world(m), m["wb_title"])}
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="section-head center">
      <p class="eyebrow">{t['what_eyebrow']}</p>
      <h2>{t['what_title']}</h2>
      <p class="lead">{t['what_lead']}</p>
    </div>
    <div class="pillars">{pillars}</div>
  </div>
</section>

<section id="{how_id}">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">{t['how_eyebrow']}</p>
      <h2>{t['how_title']}</h2>
      <p class="lead">{t['how_lead']}</p>
    </div>
    <div class="steps">{steps}</div>
  </div>
</section>

<section class="alt" id="{feat_id}">
  <div class="wrap">
    <div class="section-head center">
      <p class="eyebrow">{t['feat_eyebrow']}</p>
      <h2>{t['feat_title']}</h2>
    </div>
    <div class="feature">
      <div><p class="eyebrow">{t['f1_eyebrow']}</p><h2>{t['f1_title']}</h2>{features(t['f1'])}</div>
      {window(m, "wiki", mock_wiki(m), m["wiki_title"])}
    </div>
    <div class="feature flip">
      <div><p class="eyebrow">{t['f2_eyebrow']}</p><h2>{t['f2_title']}</h2>{features(t['f2'])}</div>
      {window(m, "live", mock_live(m), m["live_title"])}
    </div>
    <div class="feature">
      <div><p class="eyebrow">{t['f3_eyebrow']}</p><h2>{t['f3_title']}</h2>{features(t['f3'])}</div>
      {window(m, "post", mock_post(m), m["post_title"])}
    </div>
  </div>
</section>

<section id="ai">
  <div class="wrap">
    <div class="section-head">
      <p class="eyebrow">{t['ai_eyebrow']}</p>
      <h2>{t['ai_title']}</h2>
      <p class="lead">{t['ai_lead']}</p>
    </div>
    <div class="ai-grid">{ai}</div>
    <p class="note">{SHIELD}<span>{t['ai_note']}</span></p>
  </div>
</section>

<section class="alt" id="{dl_id}">
  <div class="wrap">
    <div class="section-head center">
      <p class="eyebrow">{t['dl_eyebrow']}</p>
      <h2>{t['dl_title']}</h2>
      <p class="lead">{t['dl_lead']}</p>
    </div>
    <div class="dl-grid">
      <div class="dl">
        <div class="dl-head">{APPLE}<h3>{t['mac_title']}</h3></div>
        <p class="meta">{t['mac_meta']}</p>
        <a class="btn btn-primary" href="{DL_MAC}">{APPLE}{t['mac_btn']}</a>
        <ol>{mac_steps}</ol>
        <p class="req">{t['mac_req']}</p>
      </div>
      <div class="dl">
        <div class="dl-head">{WINDOWS}<h3>{t['win_title']}</h3></div>
        <p class="meta">{t['win_meta']}</p>
        <a class="btn btn-primary" href="{DL_WIN}">{WINDOWS}{t['win_btn']}</a>
        <ol>{win_steps}</ol>
        <p class="req">{t['win_req']}</p>
      </div>
    </div>
    <p class="small muted" style="text-align:center;margin-top:26px"><a href="{RELEASES}">{t['all_versions']}</a></p>
  </div>
</section>

<section id="faq">
  <div class="wrap">
    <div class="section-head center">
      <p class="eyebrow">{t['faq_eyebrow']}</p>
      <h2>{t['faq_title']}</h2>
    </div>
    <div class="faq">{faq}</div>
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap">
    <div class="cta">
      <h2>{t['cta_title']}</h2>
      <p>{t['cta_text']}</p>
      <div class="actions">
        <a class="btn" href="{DL_MAC}">{APPLE}{t['dl_mac']}</a>
        <a class="btn ghost" href="{DL_WIN}">{WINDOWS}{t['dl_win']}</a>
      </div>
    </div>
  </div>
</section>
</main>

<footer>
  <div class="wrap">
    <a class="brand" href="#top"><img src="{prefix}assets/icon.png" alt="" width="24" height="24">CriticalPrep</a>
    <span>BETA {VERSION} · {t['footer_rights']}</span>
    <nav>{footer_links}</nav>
  </div>
</footer>
</body>
</html>
"""


def main():
    (ROOT / "index.html").write_text(page("it"), encoding="utf-8")
    (ROOT / "en").mkdir(exist_ok=True)
    (ROOT / "en" / "index.html").write_text(page("en"), encoding="utf-8")
    (ROOT / ".nojekyll").write_text("", encoding="utf-8")
    print("index.html, en/index.html")


if __name__ == "__main__":
    main()

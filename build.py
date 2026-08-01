#!/usr/bin/env python3
"""ÍSDAL — static site generator.

Generates all HTML pages (shared header/footer + content) into the repo root.
Run:  python3 build.py
"""

import os

ROOT = os.path.dirname(os.path.abspath(__file__))

WEDGE = '<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><polygon points="0,9 24,0 24,24 0,24"/></svg>'

FAVICON = (
    "data:image/svg+xml,"
    "%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E"
    "%3Cpolygon points='0,9 24,0 24,24 0,24' fill='%23131311'/%3E%3C/svg%3E"
)


def head(title, desc, p):
    return f"""<!DOCTYPE html>
<html lang="is">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="{FAVICON}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}css/style.css">
</head>
<body>"""


def header(p, current):
    def cur(name):
        return ' aria-current="page"' if name == current else ""

    return f"""
<header class="site-header">
  <div class="wrap bar">
    <a class="logo" href="{p}index.html" aria-label="ÍSDAL — forsíða">
      {WEDGE.format(s=26)}
      <span class="word">ÍSDAL</span>
      <span class="tag">Arkitektur<br>&amp; Interior</span>
    </a>
    <button class="menu-btn" aria-expanded="false" aria-controls="nav">Valmynd</button>
    <nav class="site-nav" id="nav">
      <a href="{p}verkefni.html"{cur('verkefni')}>Verkefni</a>
      <a href="{p}um-okkur.html"{cur('um')}>Um okkur</a>
      <a href="{p}frettir.html"{cur('frettir')}>Fréttir</a>
      <a href="{p}hafa-samband.html"{cur('samband')}>Hafa samband</a>
    </nav>
  </div>
</header>"""


def footer(p):
    return f"""
<footer class="site-footer">
  <div class="wrap">
    <div class="cols">
      <div>
        <span class="label">Stofan</span>
        <p class="blurb">Ísdal er arkitekta- og hönnunarstofa í Reykjavík sem vinnur þvert á arkitektúr, innanhússhönnun og vinnustaði — frá fyrstu skissu að fullbúnu rými.</p>
      </div>
      <div>
        <span class="label">Vefur</span>
        <ul>
          <li><a href="{p}verkefni.html">Verkefni</a></li>
          <li><a href="{p}um-okkur.html">Um okkur</a></li>
          <li><a href="{p}frettir.html">Fréttir</a></li>
          <li><a href="{p}hafa-samband.html">Hafa samband</a></li>
        </ul>
      </div>
      <div>
        <span class="label">Samfélagsmiðlar</span>
        <ul>
          <li><a href="https://www.instagram.com/" target="_blank" rel="noopener">Instagram</a></li>
          <li><a href="https://www.linkedin.com/" target="_blank" rel="noopener">LinkedIn</a></li>
        </ul>
      </div>
      <div>
        <span class="label">Hafa samband</span>
        <ul>
          <li><a href="mailto:info@isdal.is">info@isdal.is</a></li>
          <li>Reykjavík, Ísland</li>
        </ul>
      </div>
    </div>
    <div class="footer-mark">
      <div class="word">ÍSDAL</div>
      <div class="fine">© 2026 Ísdal ehf.<br>Arkitektur &amp; Interior</div>
    </div>
  </div>
</footer>
<script src="{p}js/main.js"></script>
</body>
</html>"""


def page(filename, title, desc, current, body, p=""):
    html = head(title, desc, p) + header(p, current) + body + footer(p)
    path = os.path.join(ROOT, filename)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", filename)


# ------------------------------------------------------------------
# project data
# ------------------------------------------------------------------

PROJECTS = [
    {
        "slug": "sumarhus-vid-geysi",
        "num": "01",
        "title": "Sumarhús við Geysi",
        "cat": "arkitektur",
        "catlabel": "Arkitektúr",
        "card": "geysir-1.webp",
        "meta": [
            ("Staðsetning", "Haukadalur, Bláskógabyggð"),
            ("Tegund", "Sumarhús — nýbygging"),
            ("Hlutverk", "Arkitektúr og innanhússhönnun"),
            ("Ár", "2024–"),
            ("Staða", "Í byggingu"),
        ],
        "lede": "Sumarhús hannað utan um norðurljósin og útsýnið yfir Haukadal — svart timburhús sem hvílir lágt í mosavöxnu hrauni.",
        "paras": [
            "Húsið er hugsað sem sjónauki að himni og fjallahring. Brotið mænisform opnar stór gluggafleti til norðurs og upp í rjáfur, þannig að norðurljósin verða hluti af stofunni á veturna og miðnætursólin á sumrin. Svört standandi klæðning lætur húsið hverfa inn í dökkt hraunið á meðan hlý birta innan úr því lýsir eins og lugt í landslaginu.",
            "Innra skipulagið er einfalt og hagkvæmt: samfellt alrými fyrir eldhús, borðstofu og stofu undir fullri lofthæð, svefnrými á tveimur pöllum og baðstofa sem tengist heitum potti á sólpalli. Efnisvalið er fábrotið — furukrossviður, steinn og ull — og valið til að eldast fallega með húsinu.",
            "Verkefnið er unnið alla leið frá fyrstu skissu að byggingarleyfi og eftirliti á framkvæmdatíma.",
        ],
        "figs": [
            ("geysir-1.webp", "Húsið að vetri — norðurljós yfir Haukadal", False),
            ("geysir-2.webp", "Suðurhlið — svört klæðning í mosavöxnu hrauni", False),
        ],
    },
    {
        "slug": "rvk-studios",
        "num": "02",
        "title": "RVK Studios",
        "cat": "arkitektur vinnurymi",
        "catlabel": "Endurgerð / Vinnurými",
        "card": "rvk-studios-2.webp",
        "meta": [
            ("Staðsetning", "Gufunes, Reykjavík"),
            ("Tegund", "Endurgerð iðnaðarhúsnæðis"),
            ("Hlutverk", "Hönnun vinnurýma og sameigna"),
            ("Ár", "2023"),
            ("Staða", "Lokið"),
        ],
        "lede": "Gömul áburðarverksmiðja í Gufunesi fékk nýtt líf sem kvikmyndaver og skrifstofur RVK Studios.",
        "paras": [
            "Hráleiki verksmiðjunnar fékk að halda sér: steypt burðarvirki, sýnilegar lagnir og veðrað timbur mynda bakgrunn fyrir nýja starfsemi. Nýjum innskotum — fundarherbergjum, mötuneyti og vinnustofum — er komið fyrir sem frístandandi einingum inni í stóra rýminu svo saga hússins er alltaf sýnileg.",
            "Mötuneytið og sameiginleg rými liggja að opnu gengi umhverfis miðjukjarna, þar sem dagsbirta að ofan flæðir niður í gegnum hæðirnar. Húsgögn og lýsing voru valin til að standast harða notkun kvikmyndaframleiðslu án þess að missa hlýju.",
        ],
        "figs": [
            ("rvk-studios-2.webp", "Mötuneyti og samverurými í gömlu verksmiðjunni", False),
            ("rvk-studios-1.webp", "Yfirlitsmynd — kvikmyndaverið í Gufunesi", False),
        ],
    },
    {
        "slug": "advania",
        "num": "03",
        "title": "Advania",
        "cat": "vinnurymi innanhus",
        "catlabel": "Vinnurými",
        "card": "advania-1.webp",
        "meta": [
            ("Staðsetning", "Reykjavík"),
            ("Tegund", "Vinnustaður og matsalur"),
            ("Hlutverk", "Innanhússhönnun"),
            ("Ár", "2022"),
            ("Staða", "Lokið"),
        ],
        "lede": "Vinnurými og matsalur Advania — sterkir litir, góð hljóðvist og fjölbreytt aðstaða fyrir ólíkar vinnustundir dagsins.",
        "paras": [
            "Verkefnið snerist um að gefa starfsfólki raunverulegt val: opin vinnurými, skjólgóða bása fyrir samtöl, næðisrými og matsal sem virkar jafnt fyrir hádegismat og uppákomur. Hljóðvist var leiðarstef í efnisvali — klæddir veggfletir, teppi og hljóðdempandi loft halda ró í opnum rýmum.",
            "Litapallettan sækir í vörumerki fyrirtækisins og er notuð markvisst til að aðgreina svæði; djúpfjólubláir samtalsbásar með innfelldri lýsingu urðu eitt af einkennum vinnustaðarins.",
        ],
        "figs": [
            ("advania-1.webp", "Samtalsbás — hljóðvist og innfelld lýsing", False),
            ("advania-2.webp", "Matsalurinn — „Gjörið svo vel“", False),
        ],
    },
    {
        "slug": "eldhus-i-laugardal",
        "num": "04",
        "title": "Eldhús í Laugardal",
        "cat": "innanhus",
        "catlabel": "Innanhússhönnun",
        "card": "eldhus-laug-1.webp",
        "meta": [
            ("Staðsetning", "Laugardalur, Reykjavík"),
            ("Tegund", "Eldhús og borðstofa"),
            ("Hlutverk", "Innanhússhönnun"),
            ("Ár", "2024"),
            ("Staða", "Lokið"),
        ],
        "lede": "Dökkur reykt­ur viður, hvítur steinn og hlý innfelld lýsing — eldhús sem tengir saman eldun, borðhald og daglegt líf fjölskyldunnar.",
        "paras": [
            "Innréttingin er teiknuð frá gólfi í loft og nýtir hverja sneið rýmisins: heilklæddur tækjaveggur með innfelldum ofnum, kaffihorni og geymslu losar vinnufleti eldhússeyjunnar undan tækjum og drasli. Dökk eikin fær mótvægi í hvítum steini á borðflötum og glerskápum með speglabaki sem dýpka rýmið.",
            "Borðstofan er hugsuð sem framhald eldhússins — sérsmíðaður stofuskápur með glerhurðum og innfelldri lýsingu rammar inn borðhaldið og heldur heildarsvip í gegnum bæði rými.",
        ],
        "figs": [
            ("eldhus-laug-1.webp", "Eldhúsið — dökk eik og hvítur steinn", False),
            ("eldhus-laug-2.webp", "Eyjan við gluggann", True),
            ("eldhus-laug-3.webp", "Sérsmíðaður stofuskápur með innfelldri lýsingu", True),
        ],
    },
    {
        "slug": "eldhus-i-mosfellsbae",
        "num": "05",
        "title": "Eldhús í Mosfellsbæ",
        "cat": "innanhus",
        "catlabel": "Innanhússhönnun",
        "card": "eldhus-mos-1.webp",
        "meta": [
            ("Staðsetning", "Mosfellsbær"),
            ("Tegund", "Eldhús"),
            ("Hlutverk", "Innanhússhönnun"),
            ("Ár", "2023"),
            ("Staða", "Lokið"),
        ],
        "lede": "Ljóst og opið fjölskyldueldhús þar sem rifflaður eikarviður, grár marmari og mjúk form mætast.",
        "paras": [
            "Eyjan er hjarta rýmisins — ávalir endar og rifflaður eikarviður gera hana að húsgagni frekar en innréttingu, og barstólar við gluggann tengja eldhúsið við garðinn. Marmarinn heldur áfram upp vegginn sem heill bakveggur með innfelldri lýsingu undir efri skápum.",
            "Hvítar sléttar hurðir halda heildinni rólegri, en hlýjan kemur úr viðnum og látúnsdetaljum í blöndunartækjum og höldum.",
        ],
        "figs": [
            ("eldhus-mos-1.webp", "Eyjan — rifflaður eikarviður og grár marmari", False),
            ("eldhus-mos-2.webp", "Kaffihorn með marmarabaki", True),
        ],
    },
    {
        "slug": "fjolbyli-med-inngardi",
        "num": "06",
        "title": "Fjölbýli með inngarði",
        "cat": "arkitektur",
        "catlabel": "Arkitektúr",
        "card": "fjolbyli-1.webp",
        "meta": [
            ("Staðsetning", "Höfuðborgarsvæðið"),
            ("Tegund", "Íbúðir — hönnunartillaga"),
            ("Hlutverk", "Arkitektúr"),
            ("Ár", "2024"),
            ("Staða", "Í vinnslu"),
        ],
        "lede": "Tillaga að timburbyggðu fjölbýli þar sem íbúðirnar raðast um gróinn inngarð — sameign sem raunverulega er notuð.",
        "paras": [
            "Byggingin er brotin upp í smærri einingar með svölum og gróðurhúsum sem snúa inn í garðinn, þannig að hvert heimili á sér bæði skjólgóða einkaverönd og hlutdeild í sameiginlegu útirými. Inngarðurinn er hannaður sem dvalarsvæði með tjörn, matjurtabeðum og leiksvæði — hversdagslegur fundarstaður íbúa.",
            "Burðarvirki og klæðningar eru úr timbri til að lágmarka kolefnisspor, og virk jarðhæð með bakaríi og smáverslun tengir húsið við götuna.",
        ],
        "figs": [
            ("fjolbyli-1.webp", "Inngarðurinn — tjörn og dvalarsvæði", False),
            ("fjolbyli-2.webp", "Götuhlið með virkri jarðhæð", False),
        ],
    },
    {
        "slug": "albano",
        "num": "07",
        "title": "Albano háskólasvæðið",
        "cat": "arkitektur",
        "catlabel": "Arkitektúr",
        "card": "albano-1.webp",
        "meta": [
            ("Staðsetning", "Stokkhólmur, Svíþjóð"),
            ("Tegund", "Háskólasvæði"),
            ("Hlutverk", "Arkitekt í teymi Arkitema"),
            ("Ár", "2017–2021"),
            ("Staða", "Lokið"),
        ],
        "lede": "Nýtt háskólahverfi fyrir Stokkhólmsháskóla og KTH — kennsluhús, rannsóknarrými og stúdentaíbúðir í vistvottuðu borgarumhverfi.",
        "paras": [
            "Albano er eitt stærsta uppbyggingarverkefni háskólanna í Stokkhólmi og var skipulagt sem „vistkerfishverfi“ þar sem byggingar, almenningsrými og gróður vinna saman. Hildur starfaði að verkefninu sem arkitekt hjá Arkitema, meðal annars að hönnun kennslu- og rannsóknarbygginga.",
            "Verkefnið kenndi stofunni margt sem fylgir henni enn: samhæfingu stórra hagsmunahópa, sjálfbærnivottanir og hvernig almannarými á milli húsa ráða jafnmiklu um upplifun og húsin sjálf.",
        ],
        "figs": [
            ("albano-1.webp", "Háskólahverfið við Brunnsviken", False),
            ("albano-2.webp", "Kennslubyggingar og almenningsrými", False),
        ],
    },
    {
        "slug": "langsjoskolan",
        "num": "08",
        "title": "Långsjöskolan",
        "cat": "arkitektur",
        "catlabel": "Arkitektúr",
        "card": "langsjo-1.webp",
        "meta": [
            ("Staðsetning", "Stokkhólmur, Svíþjóð"),
            ("Tegund", "Grunnskóli — 900 nemendur"),
            ("Hlutverk", "Arkitekt í teymi Arkitema"),
            ("Ár", "2022"),
            ("Staða", "Lokið"),
        ],
        "lede": "Grunnskóli fyrir 900 nemendur þar sem timburklæðning, dagsbirta og skýr innri skipan mynda rólegan skóladag.",
        "paras": [
            "Skólinn er skipulagður um heimasvæði árganga — smærri einingar innan stórrar byggingar sem gefa nemendum öryggi og yfirsýn. Kennslurými opnast að sameiginlegum torgum þar sem hópvinna og frjáls leikur fá pláss.",
            "Timbur er ráðandi efni jafnt úti sem inni og skólalóðin var hönnuð samhliða húsinu svo útikennsla og hreyfing fléttast inn í daglegt starf. Hildur vann að verkefninu sem arkitekt hjá Arkitema.",
        ],
        "figs": [
            ("langsjo-1.webp", "Aðkoman — timburklæddar álmur", False),
            ("langsjo-2.webp", "Skólalóðin", True),
            ("langsjo-3.webp", "Heimasvæði árganga", True),
        ],
    },
    {
        "slug": "grunnskoli-i-nykoping",
        "num": "09",
        "title": "Grunnskóli í Nyköping",
        "cat": "arkitektur",
        "catlabel": "Arkitektúr",
        "card": "nykoping-1.webp",
        "meta": [
            ("Staðsetning", "Nyköping, Svíþjóð"),
            ("Tegund", "Grunnskóli — 1.100 nemendur"),
            ("Hlutverk", "Arkitekt í teymi Cedervall arkitekter"),
            ("Ár", "2017"),
            ("Staða", "Lokið"),
        ],
        "lede": "Einn stærsti grunnskóli Svíþjóðar á sínum tíma — 1.100 nemendur undir einu þaki án þess að nokkur týnist.",
        "paras": [
            "Lykillinn að svo stórum skóla er að brjóta hann niður í læsilegar einingar: aðgreindar álmur með eigin inngöngum og heimasvæðum raðast um sameiginlegan miðkjarna með sal, bókasafni og mötuneyti. Þannig fær hver nemandi „lítinn skóla“ innan þess stóra.",
            "Hildur vann að verkefninu hjá Cedervall arkitekter, frá forhönnun að útboðsgögnum.",
        ],
        "figs": [
            ("nykoping-1.webp", "Skólinn í Nyköping", False),
        ],
    },
]


def pcard(pr, p, eager=False):
    load = "" if eager else ' loading="lazy"'
    return f"""
      <a class="pcard reveal" href="{p}verkefni/{pr['slug']}.html" data-cat="{pr['cat']}">
        <div class="frame"><img src="{p}assets/img/{pr['card']}" alt="{pr['title']}"{load}></div>
        <div class="meta">
          <span class="num">{pr['num']}</span>
          <span class="title-line">{pr['title']}</span>
          <span class="cat">{pr['catlabel']}</span>
        </div>
      </a>"""


# ------------------------------------------------------------------
# index.html
# ------------------------------------------------------------------

featured = [PROJECTS[0], PROJECTS[1], PROJECTS[3], PROJECTS[2]]

index_body = f"""
<main>
  <section class="hero wrap">
    <span class="label"><b>Ísdal</b> — Arkitektastofa í Reykjavík</span>
    <h1 class="display">Rými sem eiga rætur í&nbsp;stað, birtu og&nbsp;fólki</h1>
    <div class="hero-grid">
      <div>
        <p class="lede">Ísdal er arkitekta- og hönnunarstofa sem vinnur þvert á arkitektúr, innanhússhönnun og vinnustaði. Með yfir tuttugu ára reynslu af heimilum, skrifstofum og almenningsbyggingum á Íslandi og í Svíþjóð fylgjum við verkefnum alla leið — frá fyrstu skissu að byggingarleyfi og fullbúnu rými.</p>
        <br>
        <a class="alink" href="verkefni.html">Skoða verkefnin</a>
      </div>
      <figure class="plate hero-fig reveal">
        <img src="assets/img/geysir-1.webp" alt="Sumarhús við Geysi að vetri undir norðurljósum">
        <figcaption><span>Verk 01 — <b>Sumarhús við Geysi</b></span><span>Í byggingu</span></figcaption>
      </figure>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head">
        <span class="label">01 — <b>Valin verkefni</b></span>
        <a class="alink" href="verkefni.html">Öll verkefni</a>
      </div>
      <div class="projects-grid">
        {''.join(pcard(pr, '') for pr in featured)}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head">
        <span class="label">02 — <b>Þjónusta</b></span>
      </div>
      <div class="services">
        <div class="service-row reveal">
          <span class="num">/01</span>
          <h3>Arkitektúr</h3>
          <p>Nýbyggingar, viðbyggingar og endurgerð eldri húsa — íbúðarhús, sumarhús og almenningsbyggingar, frá frumhugmynd að fullbúnu húsi.</p>
        </div>
        <div class="service-row reveal">
          <span class="num">/02</span>
          <h3>Innanhússhönnun</h3>
          <p>Innréttingar, efnisval, lýsing og húsgögn. Við teiknum sérsmíði niður í minnstu detalju og fylgjum framleiðslu og uppsetningu eftir.</p>
        </div>
        <div class="service-row reveal">
          <span class="num">/03</span>
          <h3>Vinnustaðir</h3>
          <p>Skrifstofur, mötuneyti og sérhæfð vinnurými. Greining á þörfum, rýmisskipulag og hönnun sem styður ólíkar vinnustundir dagsins.</p>
        </div>
        <div class="service-row reveal">
          <span class="num">/04</span>
          <h3>Byggingarleyfi &amp; ráðgjöf</h3>
          <p>Aðaluppdrættir, byggingarleyfisumsóknir og samskipti við byggingarfulltrúa — við þekkjum ferlið og styttum leiðina.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head">
        <span class="label">03 — <b>Stofan</b></span>
        <a class="alink" href="um-okkur.html">Um okkur</a>
      </div>
      <p class="lede" style="margin-bottom: clamp(32px, 5vw, 56px);">Ísdal var stofnuð af Hildi Ísdal arkitekt og er í dag þriggja kvenna stofa sem sameinar íslenska og skandinavíska hönnunarhefð. Við trúum á vandaða hversdagsbyggingarlist — hús og rými sem eldast vel og þjóna fólkinu sem notar þau.</p>
      <div class="studio-strip reveal">
        <div><span class="big">3</span><span class="label">Arkitektar &amp; hönnuðir</span></div>
        <div><span class="big">20+</span><span class="label">Ára reynsla</span></div>
        <div><span class="big">2</span><span class="label">Lönd — Ísland &amp; Svíþjóð</span></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head">
        <span class="label">04 — <b>Fréttir</b></span>
        <a class="alink" href="frettir.html">Allar fréttir</a>
      </div>
      <div class="news-list">
        <a class="news-item reveal" href="frettir.html">
          <time datetime="2026-08-01">01.08.2026</time>
          <h3>Ný ásýnd og nýr vefur Ísdal</h3>
          <span class="arrow">→</span>
        </a>
        <a class="news-item reveal" href="frettir.html">
          <time datetime="2026-06-15">15.06.2026</time>
          <h3>Stofan stækkar — Dagný og Sara ganga til liðs við Ísdal</h3>
          <span class="arrow">→</span>
        </a>
        <a class="news-item reveal" href="frettir.html">
          <time datetime="2026-04-03">03.04.2026</time>
          <h3>Sumarhús við Geysi rís í Haukadal</h3>
          <span class="arrow">→</span>
        </a>
      </div>
    </div>
  </section>
</main>

<section class="cta-band">
  <div class="wrap">
    <span class="label">05 — <b>Hafa samband</b></span>
    <h2>Með verkefni í&nbsp;huga? Ekki hika við að hafa samband.</h2>
    <a class="alink" href="hafa-samband.html">Hafa samband</a>
  </div>
</section>
"""

page(
    "index.html",
    "ÍSDAL — Arkitektúr & innanhússhönnun í Reykjavík",
    "Ísdal er arkitekta- og hönnunarstofa í Reykjavík. Arkitektúr, innanhússhönnun, vinnustaðir og byggingarleyfi.",
    "heim",
    index_body,
)

# ------------------------------------------------------------------
# verkefni.html
# ------------------------------------------------------------------

verkefni_body = f"""
<main>
  <section class="page-head wrap">
    <span class="label"><b>Verkefni</b> — {len(PROJECTS)} verk</span>
    <h1 class="display">Verkefni</h1>
    <p class="lede">Úrval verkefna stofunnar — frá sumarhúsum og eldhúsum til kvikmyndavera og skóla fyrir þúsund nemendur.</p>
  </section>
  <section class="section" style="padding-top: 0;">
    <div class="wrap">
      <div class="filterbar" role="group" aria-label="Sía verkefni">
        <button data-filter="allt" class="active">Allt</button>
        <button data-filter="arkitektur">Arkitektúr</button>
        <button data-filter="innanhus">Innanhússhönnun</button>
        <button data-filter="vinnurymi">Vinnustaðir</button>
      </div>
      <div class="projects-grid">
        {''.join(pcard(pr, '') for pr in PROJECTS)}
      </div>
    </div>
  </section>
</main>
"""

page(
    "verkefni.html",
    "Verkefni — ÍSDAL",
    "Verkefni Ísdal: arkitektúr, innanhússhönnun og vinnustaðir á Íslandi og í Svíþjóð.",
    "verkefni",
    verkefni_body,
)

# ------------------------------------------------------------------
# project detail pages
# ------------------------------------------------------------------

for i, pr in enumerate(PROJECTS):
    nxt = PROJECTS[(i + 1) % len(PROJECTS)]
    meta_rows = "".join(
        f'<div class="row"><span class="k">{k}</span><span class="v">{v}</span></div>'
        for k, v in pr["meta"]
    )
    paras = "".join(f"<p>{t}</p>" for t in pr["paras"])

    figs_html = []
    pending_two = []
    fig_i = 0

    def fig(src, cap, narrow=False):
        global fig_i
        fig_i += 1
        cls = ' class="narrow"' if narrow else ""
        return (
            f'<figure class="plate reveal"{cls}>'
            f'<img src="../assets/img/{src}" alt="{pr["title"]} — {cap}" loading="lazy">'
            f'<figcaption><span>Verk {pr["num"]} — Mynd {fig_i:02d}</span><span><b>{cap}</b></span></figcaption>'
            f"</figure>"
        )

    for src, cap, half in pr["figs"]:
        if half:
            pending_two.append(fig(src, cap))
            if len(pending_two) == 2:
                figs_html.append('<div class="two">' + "".join(pending_two) + "</div>")
                pending_two = []
        else:
            if pending_two:
                figs_html.append('<div class="two">' + "".join(pending_two) + "</div>")
                pending_two = []
            figs_html.append(fig(src, cap, narrow=True))
    if pending_two:
        figs_html.append('<div class="two">' + "".join(pending_two) + "</div>")

    detail_body = f"""
<main>
  <section class="detail-head wrap">
    <a class="alink crumb" href="../verkefni.html" style="transform: scaleX(-1);"></a>
    <span class="label" style="display:block; margin-bottom:18px;">Verk {pr['num']} — <b>{pr['catlabel']}</b></span>
    <h1>{pr['title']}</h1>
  </section>
  <section class="section" style="padding-top:0;">
    <div class="wrap">
      <div class="detail-grid">
        <aside>
          <div class="meta-table">{meta_rows}</div>
        </aside>
        <div class="detail-body">
          <p class="lede">{pr['lede']}</p>
          {paras}
          <div class="figs">
            {''.join(figs_html)}
          </div>
        </div>
      </div>
      <div class="next-project reveal">
        <span class="label">Næsta verk — {nxt['num']}</span>
        <a href="{nxt['slug']}.html">{nxt['title']}</a>
      </div>
    </div>
  </section>
</main>
"""
    # simpler back-link (the scaleX hack above renders poorly — use plain text link)
    detail_body = detail_body.replace(
        '<a class="alink crumb" href="../verkefni.html" style="transform: scaleX(-1);"></a>',
        '<a class="label crumb" href="../verkefni.html">← Öll verkefni</a>',
    )

    page(
        f"verkefni/{pr['slug']}.html",
        f"{pr['title']} — Verkefni — ÍSDAL",
        pr["lede"],
        "verkefni",
        detail_body,
        p="../",
    )

# ------------------------------------------------------------------
# um-okkur.html
# ------------------------------------------------------------------

um_body = """
<main>
  <section class="page-head wrap">
    <span class="label"><b>Um okkur</b> — Stofan</span>
    <h1 class="display">Lítil stofa, stór verkefni</h1>
    <p class="lede">Ísdal er arkitekta- og hönnunarstofa í Reykjavík, stofnuð af Hildi Ísdal. Í dag erum við þrjár — arkitektar og innanhússhönnuður — og vinnum verkefni af öllum stærðum, frá einu eldhúsi upp í heilar byggingar.</p>
  </section>

  <section class="section" style="padding-top:0;">
    <div class="wrap">
      <div class="section-head">
        <span class="label">01 — <b>Nálgun</b></span>
      </div>
      <div class="detail-grid">
        <div>
          <div class="studio-strip vert">
            <div><span class="big">3</span><span class="label">Arkitektar &amp; hönnuðir</span></div>
            <div><span class="big">20+</span><span class="label">Ára reynsla</span></div>
            <div><span class="big">2</span><span class="label">Lönd — Ísland &amp; Svíþjóð</span></div>
          </div>
        </div>
        <div class="detail-body">
          <p class="lede">Við trúum á vandaða hversdagsbyggingarlist — hús og rými sem eldast vel og þjóna fólkinu sem notar þau.</p>
          <p>Hvert verkefni byrjar á staðnum og fólkinu: hvernig fellur birtan, hvaðan blæs, hvernig er gengið um húsið á venjulegum þriðjudegi? Út frá því mótum við skýra hugmynd sem heldur í gegnum allt ferlið — frá skissu að byggingarleyfi, útboði og eftirliti.</p>
          <p>Reynsla okkar spannar heimili, skrifstofur, skóla og almenningsbyggingar á Íslandi og í Svíþjóð. Sú breidd nýtist í hverju verki: skólahönnun kennir manni flæði og hljóðvist, eldhúshönnun kennir manni detalju — og hvort tveggja gerir betri byggingar.</p>
          <p>Stofan tekur að sér arkitektúr, innanhússhönnun, vinnustaðaráðgjöf og gerð aðaluppdrátta til byggingarleyfis.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head">
        <span class="label">02 — <b>Teymið</b></span>
      </div>
      <div class="team-grid">
        <div class="tcard reveal">
          <div class="ph"><img src="assets/img/hildur.webp" alt="Hildur Ísdal Þorgeirsdóttir"></div>
          <div class="meta"><b>Hildur Ísdal Þorgeirsdóttir</b><span>Stofnandi — Arkitekt FAÍ &amp; innanhússhönnuður</span></div>
        </div>
        <div class="tcard reveal">
          <div class="ph">
            <span class="init">D</span>
            <svg viewBox="0 0 24 24" fill="currentColor"><polygon points="0,9 24,0 24,24 0,24"/></svg>
          </div>
          <div class="meta"><b>Dagný</b><span>Arkitekt</span></div>
        </div>
        <div class="tcard reveal">
          <div class="ph">
            <span class="init">S</span>
            <svg viewBox="0 0 24 24" fill="currentColor"><polygon points="0,9 24,0 24,24 0,24"/></svg>
          </div>
          <div class="meta"><b>Sara</b><span>Innanhússhönnuður</span></div>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head">
        <span class="label">03 — <b>Stofnandinn</b></span>
      </div>
      <div class="founder">
        <figure class="plate reveal">
          <img src="assets/img/hildur.webp" alt="Hildur Ísdal Þorgeirsdóttir, stofnandi Ísdal">
          <figcaption><span><b>Hildur Ísdal Þorgeirsdóttir</b></span><span>Reykjavík</span></figcaption>
        </figure>
        <div>
          <h3>Hildur Ísdal Þorgeirsdóttir</h3>
          <span class="label role">Stofnandi — Arkitekt FAÍ &amp; innanhússhönnuður</span>
          <p>Hildur stofnaði Ísdal árið 2023 eftir rúman áratug á stofum í Svíþjóð og á Íslandi. Hún hóf ferilinn í innanhússhönnun, lauk síðar meistaranámi í sjálfbærum arkitektúr og hefur unnið að öllu frá eldhúsum upp í háskólahverfi. Sú samsetning — detalja innanhússhönnuðarins og yfirsýn arkitektsins — mótar öll verkefni stofunnar.</p>
          <p>Hildur er löggiltur hönnuður aðaluppdrátta og hefur áritunarrétt á Íslandi.</p>
          <div class="cv">
            <div class="row"><span class="k">2023–</span><span>Ísdal — stofnandi og eigandi, Reykjavík</span></div>
            <div class="row"><span class="k">2021–23</span><span>Plús arkitektar, Reykjavík — arkitekt</span></div>
            <div class="row"><span class="k">2017–21</span><span>Arkitema, Stokkhólmi — arkitekt</span></div>
            <div class="row"><span class="k">2014–17</span><span>Cedervall arkitekter, Stokkhólmi — arkitekt</span></div>
            <div class="row"><span class="k">2012</span><span>White arkitekter, Stokkhólmi</span></div>
            <div class="row"><span class="k">2003–12</span><span>Innanhússhönnun, Reykjavík og Mílanó</span></div>
            <div class="row"><span class="k">Menntun</span><span>MS í sjálfbærum arkitektúr — KTH, Stokkhólmi · BA í arkitektúr — Listaháskóli Íslands · Innanhússhönnun — SPD Scuola Politecnica di Design, Mílanó</span></div>
          </div>
        </div>
      </div>
    </div>
  </section>
</main>

<section class="cta-band">
  <div class="wrap">
    <span class="label">04 — <b>Samstarf</b></span>
    <h2>Viltu vinna með okkur — eða hjá okkur?</h2>
    <a class="alink" href="hafa-samband.html">Hafa samband</a>
  </div>
</section>
"""

page(
    "um-okkur.html",
    "Um okkur — ÍSDAL",
    "Ísdal er þriggja kvenna arkitekta- og hönnunarstofa í Reykjavík, stofnuð af Hildi Ísdal arkitekt.",
    "um",
    um_body,
)

# ------------------------------------------------------------------
# frettir.html
# ------------------------------------------------------------------

frettir_body = """
<main>
  <section class="page-head wrap">
    <span class="label"><b>Fréttir</b> — Af stofunni</span>
    <h1 class="display">Fréttir</h1>
  </section>
  <section class="section" style="padding-top:0;">
    <div class="wrap">
      <div class="news-list">
        <div class="news-item reveal">
          <time datetime="2026-08-01">01.08.2026</time>
          <div>
            <h3>Ný ásýnd og nýr vefur Ísdal</h3>
            <p>Ísdal stígur fram sem stofa: nýtt merki, ný ásýnd og nýr vefur sem endurspeglar breiddina í verkefnum okkar — frá innréttingum til heilla bygginga. Merkið sækir form sitt í íslenska jökulinn sem stofan heitir eftir.</p>
          </div>
        </div>
        <div class="news-item reveal">
          <time datetime="2026-06-15">15.06.2026</time>
          <div>
            <h3>Stofan stækkar — Dagný og Sara ganga til liðs við Ísdal</h3>
            <p>Við bjóðum Dagnýju arkitekt og Söru innanhússhönnuð velkomnar í teymið. Með þeim verður Ísdal þriggja kvenna stofa og getur tekið að sér stærri og fjölbreyttari verkefni en áður.</p>
          </div>
        </div>
        <div class="news-item reveal">
          <time datetime="2026-04-03">03.04.2026</time>
          <div>
            <h3>Sumarhús við Geysi rís í Haukadal</h3>
            <p>Framkvæmdir við sumarhúsið í Haukadal ganga vel — húsið er fokhelt og innra frágangi miðar áfram. Stefnt er að verklokum fyrir veturinn, í tæka tíð fyrir norðurljósatímabilið.</p>
          </div>
        </div>
        <div class="news-item reveal">
          <time datetime="2026-01-20">20.01.2026</time>
          <div>
            <h3>Ísdal opnar vinnustofu í miðborg Reykjavíkur</h3>
            <p>Stofan hefur komið sér fyrir í bjartri vinnustofu í miðborginni. Kaffið er alltaf heitt — kíktu í heimsókn ef þú ert með verkefni í huga.</p>
          </div>
        </div>
      </div>
    </div>
  </section>
</main>
"""

page(
    "frettir.html",
    "Fréttir — ÍSDAL",
    "Fréttir af Ísdal — arkitekta- og hönnunarstofu í Reykjavík.",
    "frettir",
    frettir_body,
)

# ------------------------------------------------------------------
# hafa-samband.html
# ------------------------------------------------------------------

samband_body = """
<main>
  <section class="page-head wrap">
    <span class="label"><b>Hafa samband</b></span>
    <h1 class="display">Segðu okkur frá verkefninu</h1>
    <p class="lede">Stórt eða smátt — við tökum vel á móti öllum hugmyndum. Fyrsta samtal er alltaf án skuldbindinga.</p>
  </section>
  <section class="section" style="padding-top:0;">
    <div class="wrap">
      <div class="contact-grid">
        <div>
          <div class="contact-list">
            <div class="row"><span class="k">Netfang</span><span class="v"><a href="mailto:info@isdal.is">info@isdal.is</a></span></div>
            <div class="row"><span class="k">Staðsetning</span><span class="v">Reykjavík, Ísland</span></div>
            <div class="row"><span class="k">Instagram</span><span class="v"><a href="https://www.instagram.com/" target="_blank" rel="noopener">@isdal</a></span></div>
            <div class="row"><span class="k">LinkedIn</span><span class="v"><a href="https://www.linkedin.com/" target="_blank" rel="noopener">Ísdal</a></span></div>
          </div>
          <p class="muted" style="margin-top:28px; max-width:36em;">Við svörum fyrirspurnum að jafnaði innan tveggja virkra daga. Ef verkefnið þolir enga bið má líka finna okkur á vinnustofunni í miðborginni.</p>
        </div>
        <form class="contact-form" novalidate>
          <div class="field">
            <label for="nafn">Nafn</label>
            <input id="nafn" name="nafn" type="text" autocomplete="name" required>
          </div>
          <div class="field">
            <label for="netfang">Netfang</label>
            <input id="netfang" name="netfang" type="email" autocomplete="email" required>
          </div>
          <div class="field">
            <label for="skilabod">Skilaboð — segðu okkur aðeins frá verkefninu</label>
            <textarea id="skilabod" name="skilabod" rows="6" required></textarea>
          </div>
          <button type="submit">Senda fyrirspurn</button>
        </form>
      </div>
    </div>
  </section>
</main>
"""

page(
    "hafa-samband.html",
    "Hafa samband — ÍSDAL",
    "Hafðu samband við Ísdal — arkitekta- og hönnunarstofu í Reykjavík.",
    "samband",
    samband_body,
)

print("done.")

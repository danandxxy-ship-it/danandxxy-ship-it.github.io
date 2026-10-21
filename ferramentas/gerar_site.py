#!/usr/bin/env python3
"""Gera o site da 1k99 em português (raiz), inglês (/en/) e espanhol (/es/).

Para um jogo novo: acrescente um item em JOGOS (textos nos 3 idiomas + regras de privacidade)
e rode:  python3 ferramentas/gerar_site.py
"""
import html
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://danandxxy-ship-it.github.io"
EMAIL = "suporte1k99@gmail.com"
DATA = {"pt": "21 de outubro de 2026", "en": "October 21, 2026", "es": "21 de octubre de 2026"}

# caminho de cada página por idioma (relativo à raiz)
PATHS = {
    "home": {"pt": "", "en": "en/", "es": "es/"},
    "priv": {"pt": "privacidade/", "en": "en/privacy/", "es": "es/privacidad/"},
}
LANG_NAME = {"pt": "Português", "en": "English", "es": "Español"}
HTML_LANG = {"pt": "pt-BR", "en": "en", "es": "es"}

# ------------------------------------------------------------------ jogos
JOGOS = [
    {
        "id": "entrega-do-caos",
        "nome": "Entrega do Caos",
        "icone": "img/entrega-icone.png",
        "capa": "img/entrega-capa.jpg",
        "capa_alt": {"pt": "Van laranja carregada de caixas ao lado do título Entrega do Caos",
                     "en": "Orange van loaded with boxes next to the Entrega do Caos title",
                     "es": "Furgoneta naranja cargada de cajas junto al título Entrega do Caos"},
        "genero": {"pt": "Corrida infinita", "en": "Endless runner", "es": "Carrera infinita"},
        "texto": {
            "pt": "Pegue a van, encha o bagageiro de caixas e saia costurando o trânsito. Entregue na zona verde das casas, junte moedas e troque de veículo na garagem: tem bike, moto, skate, Kombi e até bitrem.",
            "en": "Grab the van, load the roof rack with boxes and weave through traffic. Deliver to the green zone by the houses, collect coins and swap vehicles in the garage: cargo bike, scooter, skateboard, retro van and even a road train.",
            "es": "Toma la furgoneta, llena la baca de cajas y esquiva el tráfico. Entrega en la zona verde de las casas, junta monedas y cambia de vehículo en el garaje: bici, moto, skate, kombi y hasta un tráiler.",
        },
        "status": {"pt": "Em teste fechado. Em breve na Google Play.", "en": "In closed testing. Coming soon to Google Play.",
                   "es": "En prueba cerrada. Muy pronto en Google Play."},
        "fotos": [("img/corrida-cidade.jpg", {"pt": "Van desviando de carros na cidade", "en": "Van dodging cars in the city", "es": "Furgoneta esquivando coches en la ciudad"}),
                  ("img/corrida-deserto.jpg", {"pt": "Corrida na estrada do deserto", "en": "Running on the desert road", "es": "Carrera en la carretera del desierto"}),
                  ("img/garagem.jpg", {"pt": "Garagem com a lista de veículos", "en": "Garage with the vehicle list", "es": "Garaje con la lista de vehículos"}),
                  ("img/corrida-noite.jpg", {"pt": "Entrega à noite na cidade", "en": "Night delivery in the city", "es": "Entrega de noche en la ciudad"})],
        "privacidade": {
            "pt": ["Classificação Livre, para todas as idades.",
                   "Anúncios: só vídeos que você escolhe assistir para ganhar algo, como continuar a corrida ou dobrar as moedas. Nenhum anúncio aparece sozinho.",
                   "Os anúncios são marcados como direcionados a crianças: não personalizados e sem ID de publicidade.",
                   "Compras: nenhuma.",
                   "Internet: só para carregar os anúncios."],
            "en": ["Rated for everyone, suitable for all ages.",
                   "Ads: only videos you choose to watch to earn something, like continuing a run or doubling your coins. No ad ever appears on its own.",
                   "Ads are marked as child-directed: non-personalized and without the advertising ID.",
                   "Purchases: none.",
                   "Internet: only to load ads."],
            "es": ["Clasificación apta para todo público.",
                   "Anuncios: solo videos que eliges ver para ganar algo, como continuar la carrera o duplicar las monedas. Ningún anuncio aparece solo.",
                   "Los anuncios se marcan como dirigidos a niños: no personalizados y sin el ID de publicidad.",
                   "Compras: ninguna.",
                   "Internet: solo para cargar los anuncios."],
        },
    },
]

# ------------------------------------------------------------------ textos da interface
UI = {
    "pt": {
        "title_home": "1k99 | Jogos para celular",
        "desc_home": "1k99 é um estúdio independente de jogos para celular.",
        "hero_h": "Jogos para celular",
        "hero_p": "A 1k99 é um estúdio independente. Fazemos jogos gratuitos, fáceis de aprender e divertidos de repetir, que funcionam no toque e no controle.",
        "jogos_h": "Nossos jogos",
        "politica": "Política de privacidade",
        "suporte": "Falar com o suporte",
        "fotos": "Imagens do jogo",
        "contato_h": "Contato",
        "contato_p": "Dúvida, bug ou sugestão sobre qualquer jogo:",
        "idiomas": "Idioma",
        "inicio": "Página inicial",
        "title_priv": "Política de privacidade | 1k99",
        "desc_priv": "Como os jogos da 1k99 tratam os seus dados.",
    },
    "en": {
        "title_home": "1k99 | Mobile games",
        "desc_home": "1k99 is an independent mobile game studio.",
        "hero_h": "Mobile games",
        "hero_p": "1k99 is an independent studio. We make free games that are easy to learn and fun to replay, playable with touch or a gamepad.",
        "jogos_h": "Our games",
        "politica": "Privacy policy",
        "suporte": "Contact support",
        "fotos": "Game screenshots",
        "contato_h": "Contact",
        "contato_p": "Questions, bugs or ideas about any of our games:",
        "idiomas": "Language",
        "inicio": "Home",
        "title_priv": "Privacy policy | 1k99",
        "desc_priv": "How 1k99 games handle your data.",
    },
    "es": {
        "title_home": "1k99 | Juegos para celular",
        "desc_home": "1k99 es un estudio independiente de juegos para celular.",
        "hero_h": "Juegos para celular",
        "hero_p": "1k99 es un estudio independiente. Hacemos juegos gratuitos, fáciles de aprender y divertidos de repetir, que se juegan con pantalla táctil o mando.",
        "jogos_h": "Nuestros juegos",
        "politica": "Política de privacidad",
        "suporte": "Contactar soporte",
        "fotos": "Imágenes del juego",
        "contato_h": "Contacto",
        "contato_p": "Dudas, errores o sugerencias sobre cualquier juego:",
        "idiomas": "Idioma",
        "inicio": "Inicio",
        "title_priv": "Política de privacidad | 1k99",
        "desc_priv": "Cómo tratan tus datos los juegos de 1k99.",
    },
}

# ------------------------------------------------------------------ política (texto completo por idioma)
G_PARTNER = {"pt": "https://policies.google.com/technologies/partner-sites?hl=pt-BR", "en": "https://policies.google.com/technologies/partner-sites?hl=en", "es": "https://policies.google.com/technologies/partner-sites?hl=es"}
G_PRIV = {"pt": "https://policies.google.com/privacy?hl=pt-BR", "en": "https://policies.google.com/privacy?hl=en", "es": "https://policies.google.com/privacy?hl=es"}


def politica(lang):
    m = f'<a href="mailto:{EMAIL}?subject=Privacidade">{EMAIL}</a>'
    if lang == "pt":
        return f"""
  <h1>Política de privacidade da 1k99</h1>
  <p class="data">Atualizada em {DATA[lang]}</p>
  <div class="resumo"><p>Esta política vale para todos os jogos publicados pela 1k99 na Google Play. Nossos jogos não têm login nem servidor próprio: o progresso fica no seu celular. Quando um jogo tem anúncios, eles vêm do Google AdMob. Quando um jogo vende alguma coisa, a compra é feita pela Google Play. O que cada jogo usa está em <a href="#jogos">Jogo por jogo</a>.</p></div>
  <h2>Quem somos</h2>
  <p>A 1k99 é um estúdio independente de jogos para Android. Quando esta página fala "nós", é a 1k99. Contato: {m}.</p>
  <h2>O que fica no seu celular</h2>
  <p>Cada jogo salva no próprio aparelho o seu progresso: moedas, itens liberados, missões, conquistas, recordes, o nome de jogador que você digitar e as configurações. A 1k99 não recebe essas informações. Se você desinstalar o jogo, o progresso é apagado junto.</p>
  <h2>Anúncios</h2>
  <p>Os anúncios dos nossos jogos são fornecidos pelo <strong>Google AdMob</strong>, a rede de anúncios do Google. Dependendo do jogo, eles podem ser vídeos que você escolhe assistir em troca de um prêmio, anúncios que aparecem entre uma partida e outra ou faixas de anúncio na tela. A seção <a href="#jogos">Jogo por jogo</a> diz quais tipos cada um usa.</p>
  <p>Para carregar e mostrar um anúncio, o kit do AdMob que vem dentro do jogo envia ao Google:</p>
  <ul>
    <li>o endereço IP da sua conexão, que dá uma ideia aproximada da região onde você está;</li>
    <li>informações técnicas do aparelho, como modelo, versão do Android e idioma;</li>
    <li>o ID de publicidade do Android, quando o jogo não é marcado como direcionado a crianças;</li>
    <li>se o anúncio foi carregado, assistido ou tocado;</li>
    <li>relatórios de erro do próprio kit de anúncios.</li>
  </ul>
  <p>O Google usa esses dados para escolher o anúncio, contar visualizações, pagar o desenvolvedor e evitar fraudes. A 1k99 só vê relatórios com totais, como quantos anúncios foram vistos no dia, e não tem acesso a dados de cada pessoa.</p>
  <p>Nos jogos livres para todas as idades, todo pedido de anúncio vai marcado como direcionado a crianças e com conteúdo para todos os públicos. Nesses jogos, o Google mostra apenas anúncios não personalizados e não usa o ID de publicidade.</p>
  <p>Nos outros jogos, onde a lei exige (como na União Europeia e no Reino Unido), o jogo pede seu consentimento antes de mostrar anúncios personalizados. Em qualquer país, você pode redefinir ou excluir o ID de publicidade nas configurações do Android, em Google e depois Anúncios.</p>
  <p>Para saber mais, veja <a href="{G_PARTNER[lang]}">como o Google usa as informações de sites ou apps que usam os serviços dele</a> e a <a href="{G_PRIV[lang]}">Política de Privacidade do Google</a>.</p>
  <h2>Compras dentro do jogo</h2>
  <p>Quando um jogo vende algum item, a compra é feita pelo sistema de pagamentos da Google Play. Os dados do seu cartão ou de outra forma de pagamento ficam com o Google e nunca chegam até nós. O jogo recebe só a confirmação de que a compra foi aprovada e qual item foi comprado, para entregar o item. Hoje nenhum jogo da 1k99 vende nada.</p>
  <h2>Com quem os dados são compartilhados</h2>
  <p>Só com o Google: pelo AdMob, para os anúncios, e pela Google Play, para as compras. Não vendemos dados e não usamos outros serviços de análise, rastreamento ou redes sociais nos nossos jogos. Tudo que é enviado vai com criptografia. Se um jogo novo passar a usar outro serviço, ele será listado nesta página antes do lançamento.</p>
  <h2>Crianças</h2>
  <p>Nossos jogos não pedem nome real, e-mail, telefone, foto nem localização exata. O nome de jogador é só um apelido que fica no celular. Mesmo assim, pais e responsáveis podem orientar a criança a não usar o nome completo. A faixa de idade de cada jogo está em <a href="#jogos">Jogo por jogo</a>.</p>
  <h2>Permissões</h2>
  <p>Nossos jogos usam acesso à internet e ao estado da conexão para carregar anúncios e, quando houver, confirmar compras. Eles não usam câmera, microfone, contatos, arquivos nem GPS. Se algum jogo precisar de outra permissão, ela será explicada em <a href="#jogos">Jogo por jogo</a>.</p>
  <h2>Como apagar seus dados</h2>
  <p>Nos jogos que têm a opção, abra Configurações e toque em Apagar progresso. Desinstalar o jogo também apaga tudo. Como não guardamos cópia do seu progresso, não há dados com a 1k99 para pedir de volta ou excluir. Para dados de anúncios, use as opções do Google indicadas acima.</p>
  <h2 id="jogos">Jogo por jogo</h2>
  {{JOGOS}}
  <h2>Mudanças nesta política</h2>
  <p>Quando lançarmos um jogo novo ou um jogo mudar o que usa, esta página será atualizada antes, com a nova data no topo.</p>
  <h2>Contato</h2>
  <p>Dúvidas sobre privacidade ou sobre qualquer jogo: {m}</p>"""
    if lang == "en":
        return f"""
  <h1>1k99 privacy policy</h1>
  <p class="data">Updated on {DATA[lang]}</p>
  <div class="resumo"><p>This policy covers every game published by 1k99 on Google Play. Our games have no login and no servers of their own: your progress stays on your phone. When a game has ads, they come from Google AdMob. When a game sells something, the purchase goes through Google Play. What each game uses is listed under <a href="#games">Game by game</a>.</p></div>
  <h2>Who we are</h2>
  <p>1k99 is an independent Android game studio. When this page says "we", it means 1k99. Contact: {m}.</p>
  <h2>What stays on your phone</h2>
  <p>Each game saves your progress on the device itself: coins, unlocked items, missions, achievements, records, the player name you type and your settings. 1k99 does not receive this information. If you uninstall the game, your progress is deleted with it.</p>
  <h2>Ads</h2>
  <p>Ads in our games are provided by <strong>Google AdMob</strong>, Google's ad network. Depending on the game, they may be videos you choose to watch for a reward, ads shown between rounds or banner ads on screen. The <a href="#games">Game by game</a> section says which kinds each game uses.</p>
  <p>To load and show an ad, the AdMob kit inside the game sends Google:</p>
  <ul>
    <li>your connection's IP address, which gives a rough idea of your region;</li>
    <li>technical device information, such as model, Android version and language;</li>
    <li>the Android advertising ID, when the game is not marked as child-directed;</li>
    <li>whether the ad was loaded, watched or tapped;</li>
    <li>error reports from the ad kit itself.</li>
  </ul>
  <p>Google uses this data to choose the ad, count views, pay the developer and prevent fraud. 1k99 only sees reports with totals, such as how many ads were watched in a day, and has no access to data about individual people.</p>
  <p>In games for all ages, every ad request is marked as child-directed and limited to content suitable for everyone. In those games Google shows only non-personalized ads and does not use the advertising ID.</p>
  <p>In other games, where the law requires it (such as in the European Union and the United Kingdom), the game asks for your consent before showing personalized ads. In any country, you can reset or delete your advertising ID in Android settings, under Google and then Ads.</p>
  <p>Learn more about <a href="{G_PARTNER[lang]}">how Google uses information from sites or apps that use its services</a> and read the <a href="{G_PRIV[lang]}">Google Privacy Policy</a>.</p>
  <h2>In-game purchases</h2>
  <p>When a game sells an item, the purchase goes through Google Play's payment system. Your card or other payment details stay with Google and never reach us. The game only receives confirmation that the purchase was approved and which item was bought, so it can deliver the item. Right now no 1k99 game sells anything.</p>
  <h2>Who the data is shared with</h2>
  <p>Only with Google: through AdMob for ads, and through Google Play for purchases. We don't sell data and we don't use any other analytics, tracking or social network services in our games. Everything sent is encrypted. If a new game uses another service, it will be listed on this page before launch.</p>
  <h2>Children</h2>
  <p>Our games don't ask for a real name, email, phone number, photo or exact location. The player name is just a nickname that stays on the phone. Even so, parents and guardians may guide children not to use their full name. Each game's age range is listed under <a href="#games">Game by game</a>.</p>
  <h2>Permissions</h2>
  <p>Our games use internet access and connection status to load ads and, when applicable, confirm purchases. They don't use the camera, microphone, contacts, files or GPS. If a game needs any other permission, it will be explained under <a href="#games">Game by game</a>.</p>
  <h2>How to delete your data</h2>
  <p>In games that offer it, open Settings and tap Delete progress. Uninstalling the game also deletes everything. Since we keep no copy of your progress, 1k99 has no data to return or delete. For ad data, use the Google options mentioned above.</p>
  <h2 id="games">Game by game</h2>
  {{JOGOS}}
  <h2>Changes to this policy</h2>
  <p>When we release a new game or a game changes what it uses, this page will be updated first, with the new date at the top.</p>
  <h2>Contact</h2>
  <p>Questions about privacy or any of our games: {m}</p>"""
    return f"""
  <h1>Política de privacidad de 1k99</h1>
  <p class="data">Actualizada el {DATA[lang]}</p>
  <div class="resumo"><p>Esta política se aplica a todos los juegos publicados por 1k99 en Google Play. Nuestros juegos no tienen inicio de sesión ni servidores propios: tu progreso queda en tu teléfono. Cuando un juego tiene anuncios, vienen de Google AdMob. Cuando un juego vende algo, la compra se hace a través de Google Play. Lo que usa cada juego está en <a href="#juegos">Juego por juego</a>.</p></div>
  <h2>Quiénes somos</h2>
  <p>1k99 es un estudio independiente de juegos para Android. Cuando esta página dice "nosotros", se refiere a 1k99. Contacto: {m}.</p>
  <h2>Lo que queda en tu teléfono</h2>
  <p>Cada juego guarda tu progreso en el propio dispositivo: monedas, objetos desbloqueados, misiones, logros, récords, el nombre de jugador que escribas y los ajustes. 1k99 no recibe esta información. Si desinstalas el juego, el progreso se borra con él.</p>
  <h2>Anuncios</h2>
  <p>Los anuncios de nuestros juegos los proporciona <strong>Google AdMob</strong>, la red de anuncios de Google. Según el juego, pueden ser videos que eliges ver a cambio de un premio, anuncios entre una partida y otra o banners en la pantalla. La sección <a href="#juegos">Juego por juego</a> indica qué tipos usa cada uno.</p>
  <p>Para cargar y mostrar un anuncio, el kit de AdMob incluido en el juego envía a Google:</p>
  <ul>
    <li>la dirección IP de tu conexión, que da una idea aproximada de tu región;</li>
    <li>información técnica del dispositivo, como modelo, versión de Android e idioma;</li>
    <li>el ID de publicidad de Android, cuando el juego no está marcado como dirigido a niños;</li>
    <li>si el anuncio se cargó, se vio o se tocó;</li>
    <li>informes de errores del propio kit de anuncios.</li>
  </ul>
  <p>Google usa estos datos para elegir el anuncio, contar las vistas, pagar al desarrollador y evitar fraudes. 1k99 solo ve informes con totales, como cuántos anuncios se vieron en el día, y no tiene acceso a datos de cada persona.</p>
  <p>En los juegos aptos para todas las edades, cada solicitud de anuncio se marca como dirigida a niños y con contenido para todo público. En esos juegos Google solo muestra anuncios no personalizados y no usa el ID de publicidad.</p>
  <p>En los demás juegos, donde la ley lo exige (como en la Unión Europea y el Reino Unido), el juego pide tu consentimiento antes de mostrar anuncios personalizados. En cualquier país puedes restablecer o eliminar el ID de publicidad en los ajustes de Android, en Google y luego Anuncios.</p>
  <p>Más información sobre <a href="{G_PARTNER[lang]}">cómo usa Google la información de sitios o apps que usan sus servicios</a> y la <a href="{G_PRIV[lang]}">Política de Privacidad de Google</a>.</p>
  <h2>Compras dentro del juego</h2>
  <p>Cuando un juego vende un objeto, la compra se hace con el sistema de pagos de Google Play. Los datos de tu tarjeta u otro medio de pago quedan con Google y nunca llegan a nosotros. El juego solo recibe la confirmación de que la compra fue aprobada y qué objeto se compró, para entregarlo. Hoy ningún juego de 1k99 vende nada.</p>
  <h2>Con quién se comparten los datos</h2>
  <p>Solo con Google: a través de AdMob para los anuncios y de Google Play para las compras. No vendemos datos ni usamos otros servicios de análisis, rastreo o redes sociales en nuestros juegos. Todo lo que se envía va cifrado. Si un juego nuevo usa otro servicio, aparecerá en esta página antes del lanzamiento.</p>
  <h2>Niños</h2>
  <p>Nuestros juegos no piden nombre real, correo, teléfono, foto ni ubicación exacta. El nombre de jugador es solo un apodo que queda en el teléfono. Aun así, padres y tutores pueden indicar a los niños que no usen su nombre completo. La edad de cada juego está en <a href="#juegos">Juego por juego</a>.</p>
  <h2>Permisos</h2>
  <p>Nuestros juegos usan el acceso a internet y el estado de la conexión para cargar anuncios y, cuando corresponda, confirmar compras. No usan cámara, micrófono, contactos, archivos ni GPS. Si algún juego necesita otro permiso, se explicará en <a href="#juegos">Juego por juego</a>.</p>
  <h2>Cómo borrar tus datos</h2>
  <p>En los juegos que tienen la opción, abre Ajustes y toca Borrar progreso. Desinstalar el juego también borra todo. Como no guardamos copia de tu progreso, 1k99 no tiene datos que devolver o eliminar. Para los datos de anuncios, usa las opciones de Google indicadas arriba.</p>
  <h2 id="juegos">Juego por juego</h2>
  {{JOGOS}}
  <h2>Cambios en esta política</h2>
  <p>Cuando lancemos un juego nuevo o un juego cambie lo que usa, esta página se actualizará antes, con la nueva fecha arriba.</p>
  <h2>Contacto</h2>
  <p>Dudas sobre privacidad o sobre cualquier juego: {m}</p>"""


# ------------------------------------------------------------------ montagem
def rel(frm, to):
    """Caminho relativo de uma página (pasta) para outra pasta ou arquivo do site."""
    depth = frm.count("/")
    return "../" * depth + to


def head(lang, page, title, desc):
    here = PATHS[page][lang]
    alts = "\n".join(f'<link rel="alternate" hreflang="{HTML_LANG[l]}" href="{SITE}/{PATHS[page][l]}">' for l in ("pt", "en", "es"))
    return f"""<!doctype html>
<html lang="{HTML_LANG[lang]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
{alts}
<link rel="alternate" hreflang="x-default" href="{SITE}/{PATHS[page]['pt']}">
<link rel="icon" href="{rel(here, 'favicon.png')}">
<link rel="apple-touch-icon" href="{rel(here, 'apple-touch-icon.png')}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{rel(here, 'style.css')}">
</head>
<body>"""


def topo(lang, page):
    here = PATHS[page][lang]
    home = rel(here, PATHS["home"][lang]) or "./"
    links = []
    for l in ("pt", "en", "es"):
        cur = ' aria-current="true"' if l == lang else ""
        links.append(f'<a href="{rel(here, PATHS[page][l]) or "./"}" lang="{HTML_LANG[l]}" data-lang="{l}"{cur}>{LANG_NAME[l]}</a>')
    return f"""<header class="topo">
  <div class="topo-dentro">
    <a class="marca" href="{home}"><img src="{rel(here, 'img/logo-1k99.png')}" width="120" height="52" alt="1k99"></a>
    <nav class="idiomas" aria-label="{UI[lang]['idiomas']}">{''.join(links)}</nav>
  </div>
</header>"""


SCRIPT = """<script>
// lembra o idioma escolhido; na primeira visita à página inicial em português,
// leva quem usa o celular em inglês ou espanhol para a versão no idioma dele
(function () {
  var links = document.querySelectorAll('.idiomas a');
  for (var i = 0; i < links.length; i++) {
    links[i].addEventListener('click', function () {
      try { localStorage.setItem('lang', this.getAttribute('data-lang')); } catch (e) {}
    });
  }
  if (!document.body.hasAttribute('data-auto')) return;
  var saved = null;
  try { saved = localStorage.getItem('lang'); } catch (e) {}
  var nav = (navigator.language || 'pt').slice(0, 2).toLowerCase();
  var want = saved || (nav === 'pt' ? 'pt' : (nav === 'es' ? 'es' : 'en'));
  if (want !== 'pt') location.replace(want + '/');
})();
</script>"""


def card(j, lang):
    here = PATHS["home"][lang]
    u = UI[lang]
    fotos = "\n".join(f'      <img src="{rel(here, f)}" width="960" height="540" loading="lazy" alt="{html.escape(a[lang])}">' for f, a in j["fotos"])
    priv = rel(here, PATHS["priv"][lang]) + "#" + j["id"]
    return f"""  <article class="card" id="{j['id']}">
    <img class="card-capa" src="{rel(here, j['capa'])}" width="1024" height="500" alt="{html.escape(j['capa_alt'][lang])}">
    <div class="card-corpo">
      <div class="card-titulo">
        <img class="icone" src="{rel(here, j['icone'])}" width="72" height="72" alt="">
        <div>
          <h3>{html.escape(j['nome'])}</h3>
          <p class="genero">{html.escape(j['genero'][lang])}</p>
        </div>
      </div>
      <p>{html.escape(j['texto'][lang])}</p>
      <span class="status">{html.escape(j['status'][lang])}</span>
      <div class="links-jogo">
        <a href="{priv}">{u['politica']}</a>
        <a href="mailto:{EMAIL}?subject={html.escape(j['nome'])}">{u['suporte']}</a>
      </div>
    </div>
    <div class="fotos" tabindex="0" aria-label="{u['fotos']}">
{fotos}
    </div>
  </article>"""


def home(lang):
    u = UI[lang]
    here = PATHS["home"][lang]
    cards = "\n".join(card(j, lang) for j in JOGOS)
    auto = ' data-auto' if lang == "pt" else ""
    page = head(lang, "home", u["title_home"], u["desc_home"]).replace("<body>", f"<body{auto}>")
    return f"""{page}
{topo(lang, 'home')}
<main>
  <section class="hero">
    <h1>{u['hero_h']}</h1>
    <p>{u['hero_p']}</p>
  </section>

  <h2 class="secao">{u['jogos_h']}</h2>
  <div class="cards">
{cards}
  </div>

  <section class="sobre">
    <h2>{u['contato_h']}</h2>
    <p>{u['contato_p']} <a href="mailto:{EMAIL}">{EMAIL}</a></p>
  </section>

  <footer>© 2026 1k99 <a href="{rel(here, PATHS['priv'][lang])}">{u['politica']}</a></footer>
</main>
{SCRIPT}
</body>
</html>
"""


def privacy(lang):
    u = UI[lang]
    jogos = "\n".join(
        f'  <h3 id="{j["id"]}">{html.escape(j["nome"])}</h3>\n  <ul>\n' + "\n".join(f"    <li>{html.escape(x)}</li>" for x in j["privacidade"][lang]) + "\n  </ul>"
        for j in JOGOS)
    body = politica(lang).replace("{JOGOS}", jogos)
    return f"""{head(lang, 'priv', u['title_priv'], u['desc_priv'])}
{topo(lang, 'priv')}
<main class="politica">{body}

  <footer>© 2026 1k99</footer>
</main>
{SCRIPT}
</body>
</html>
"""


def write(path, text):
    full = os.path.join(RAIZ, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(text)


for lang in ("pt", "en", "es"):
    write(PATHS["home"][lang] + "index.html", home(lang))
    write(PATHS["priv"][lang] + "index.html", privacy(lang))
print("site gerado")

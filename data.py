SERVICES = [
    {
        "name": "GitHub Education",
        "logo": "🐙",
        "desc": "GitHub Pro grátis, Copilot e pack com mais de 100 ferramentas para estudantes e professores.",
        "cats": ["academic", "dev"],
        "types": ["academic"],
        "link": "https://education.github.com",
    },
    {
        "name": "JetBrains (IDEs)",
        "logo": "🧠",
        "desc": "Licenças gratuitas de IntelliJ, PyCharm, WebStorm e todos os IDEs para estudantes e docentes.",
        "cats": ["academic", "dev"],
        "types": ["academic"],
        "link": "https://www.jetbrains.com/community/education/",
    },
    {
        "name": "Microsoft 365 Education",
        "logo": "🪟",
        "desc": "Word, Excel, PowerPoint, Teams e 1 TB no OneDrive gratuitamente para instituições elegíveis.",
        "cats": ["academic", "productivity"],
        "types": ["academic"],
        "link": "https://www.microsoft.com/en-us/education/products/office",
    },
    {
        "name": "Notion for Education",
        "logo": "📝",
        "desc": "Plano Plus gratuito para estudantes e docentes com email institucional verificado.",
        "cats": ["academic", "productivity"],
        "types": ["academic"],
        "link": "https://www.notion.so/product/notion-for-education",
    },
    {
        "name": "Figma for Education",
        "logo": "🎨",
        "desc": "Figma Education gratuito para estudantes e professores de instituições verificadas.",
        "cats": ["academic", "design"],
        "types": ["academic"],
        "link": "https://www.figma.com/education/",
    },
    {
        "name": "AWS Educate",
        "logo": "☁️",
        "desc": "Créditos AWS, cursos e labs de cloud computing para estudantes e educadores.",
        "cats": ["academic", "dev"],
        "types": ["academic"],
        "link": "https://aws.amazon.com/education/awseducate/",
    },
    {
        "name": "Google Workspace for Education",
        "logo": "🔵",
        "desc": "Gmail, Drive, Meet, Classroom e mais para instituições de ensino cadastradas.",
        "cats": ["academic", "productivity"],
        "types": ["academic"],
        "link": "https://edu.google.com/products/workspace-for-education/",
    },
    {
        "name": "Autodesk Education",
        "logo": "📐",
        "desc": "AutoCAD, Revit, Maya, Fusion 360 e mais de 100 softwares grátis por 1 ano.",
        "cats": ["academic", "design"],
        "types": ["academic"],
        "link": "https://www.autodesk.com/education/edu-software/overview",
    },
    {
        "name": "Adobe Creative Cloud",
        "logo": "🅰️",
        "desc": "Desconto em Creative Cloud para estudantes e docentes via instituições parceiras da Adobe.",
        "cats": ["academic", "design"],
        "types": ["academic"],
        "link": "https://www.adobe.com/creativecloud/buy/students.html",
    },
    {
        "name": "Spotify Premium Student",
        "logo": "🎵",
        "desc": "50% de desconto no Spotify Premium para estudantes universitários via SheerID.",
        "cats": ["academic"],
        "types": ["academic"],
        "link": "https://www.spotify.com/student/",
    },
    {
        "name": "Tableau for Students",
        "logo": "📊",
        "desc": "Tableau Desktop e Tableau Prep gratuitos por 1 ano para estudantes.",
        "cats": ["academic", "dev"],
        "types": ["academic"],
        "link": "https://www.tableau.com/academic/students",
    },
    {
        "name": "Vercel Education",
        "logo": "▲",
        "desc": "Plano gratuito para projetos pessoais e benefícios extras via GitHub Education.",
        "cats": ["dev"],
        "types": ["academic"],
        "link": "https://vercel.com/pricing",
    },
    {
        "name": "Namecheap Education",
        "logo": "🌐",
        "desc": "Domínio .me grátis por 1 ano e SSL grátis para estudantes via GitHub Education Pack.",
        "cats": ["academic", "dev"],
        "types": ["academic"],
        "link": "https://nc.me/",
    },
    {
        "name": "Heroku for GitHub Students",
        "logo": "💜",
        "desc": "Créditos no Heroku incluídos no GitHub Student Developer Pack.",
        "cats": ["academic", "dev"],
        "types": ["academic"],
        "link": "https://www.heroku.com/github-students",
    },
    {
        "name": "AWS Activate (Startups)",
        "logo": "🚀",
        "desc": "Até USD 100 mil em créditos AWS para startups em estágio inicial via aceleradoras parceiras.",
        "cats": ["startup", "dev"],
        "types": ["startup"],
        "link": "https://aws.amazon.com/activate/",
    },
    {
        "name": "Google for Startups",
        "logo": "🔴",
        "desc": "Até USD 200 mil em créditos Google Cloud para startups elegíveis no programa.",
        "cats": ["startup", "dev"],
        "types": ["startup"],
        "link": "https://cloud.google.com/startup",
    },
    {
        "name": "Microsoft for Startups",
        "logo": "🟦",
        "desc": "Até USD 150 mil em créditos Azure, GitHub Enterprise e suporte para startups.",
        "cats": ["startup", "dev"],
        "types": ["startup"],
        "link": "https://www.microsoft.com/en-us/startups",
    },
    {
        "name": "Stripe Atlas",
        "logo": "💳",
        "desc": "USD 20 mil em créditos AWS, Notion, Airtable e outros para empresas fundadas via Atlas.",
        "cats": ["startup"],
        "types": ["startup"],
        "link": "https://stripe.com/atlas",
    },
    {
        "name": "HubSpot for Startups",
        "logo": "🧡",
        "desc": "Até 90% de desconto no HubSpot CRM e Marketing Hub para startups elegíveis.",
        "cats": ["startup"],
        "types": ["startup"],
        "link": "https://www.hubspot.com/startups",
    },
]

# Domínios de universidades brasileiras conhecidos que não seguem padrão .edu.br
BR_UNI_DOMAINS = {
    # Federais - Sudeste
    "usp.br", "unicamp.br", "ufrj.br", "unifesp.br", "unesp.br", "ufmg.br",
    "ufjf.br", "ufv.br", "ufop.br", "ufla.br", "ufsj.br", "ufvjm.br",
    "ufrrj.br", "unirio.br", "ufabc.br", "ufes.br", "ufscar.br", "unifal.br",
    "unifei.br", "ufcat.br",
    # Estaduais - SP/RJ
    "uerj.br", "uff.br", "uenf.br", "ufsb.br",
    # Federais - Sul
    "ufrgs.br", "ufsc.br", "ufpr.br", "furg.br", "ufpel.br", "unipampa.br",
    "uffs.br", "utfpr.br",
    # Federais - Nordeste
    "ufba.br", "ufc.br", "ufpe.br", "ufrn.br", "ufpb.br", "ufpi.br",
    "ufal.br", "ufs.br", "ufma.br", "ufrb.br", "ufrpe.br", "ufcg.br",
    "ufersa.br", "univasf.br", "unilab.br", "ufca.br", "ufape.br",
    # Federais - Norte
    "ufam.br", "ufpa.br", "ufra.br", "ufopa.br", "unifap.br", "ufrr.br",
    "ufac.br", "unir.br", "ufto.br", "ufnt.br",
    # Federais - Centro-Oeste
    "unb.br", "ufmt.br", "ufms.br", "ufgd.br", "ufob.br",
    # Institutos Federais (principais)
    "ifsp.br", "ifrj.br", "ifrs.br", "ifsc.br", "ifmg.br", "ifpe.br",
    "ifce.br", "ifba.br", "ifam.br", "ifpa.br", "ifpb.br", "ifpi.br",
    "ifal.br", "ifse.br", "ifma.br", "ifmt.br", "ifms.br", "ifpr.br",
    # Privadas de destaque
    "puc-rio.br", "pucsp.br", "pucminas.br", "pucpr.br", "pucrs.br",
    "fgv.br", "insper.edu.br", "ita.br", "ime.eb.br", "mackenzie.br",
    "uftm.br", "unimontes.br", "uem.br", "uel.br", "uepg.br",
    "unioeste.br", "uenp.br", "unespar.br",
}

ACADEMIC_SUBDOMAINS = [
    "aluno.", "discente.", "estudante.", "grad.", "posgrad.", "pgrad.",
    "id.", "dac.", "sti.", "inf.", "ic.", "dcc.", "each.", "ime.",
    "academico.", "acad.",
]


def classify_domain(domain: str) -> str:
    """
    Retorna 'academic', 'startup' ou 'unknown'.
    Lógica híbrida: padrões + lista curada.
    """
    d = domain.lower()

    # Padrões globais acadêmicos
    academic_tlds = [".edu", ".edu.br", ".ac.uk", ".ac.jp", ".ac.nz",
                     ".ac.za", ".ac.in", ".ac.kr", ".edu.au"]
    if any(d.endswith(t) for t in academic_tlds):
        return "academic"

    # Subdomínios acadêmicos (ex: aluno.uerj.br)
    if any(d.startswith(s) for s in ACADEMIC_SUBDOMAINS):
        return "academic"

    # Lista curada de universidades brasileiras
    # Checa tanto o domínio exato quanto subdomínios (ex: grad.usp.br)
    for uni in BR_UNI_DOMAINS:
        if d == uni or d.endswith("." + uni):
            return "academic"

    # Padrões de startup
    startup_patterns = ["startup", "ventures", "labs", "incubadora",
                        "aceleradora", ".io", "techco", "ailab"]
    if any(p in d for p in startup_patterns):
        return "startup"

    return "unknown"


def get_matches(domain_type: str) -> list[dict]:
    return [s for s in SERVICES if domain_type in s["types"]]


CAT_LABELS = {
    "academic": "Acadêmico",
    "startup": "Startup",
    "dev": "Dev / Cloud",
    "design": "Design",
    "productivity": "Produtividade",
}

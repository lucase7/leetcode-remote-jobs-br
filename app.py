import streamlit as st
import pandas as pd
import json
import os
from datetime import datetime, date

# ---------------------------------------------------------
# 1. CONFIGURAÇÃO DA PÁGINA & ESTILO CUSTOMIZADO (CSS)
# ---------------------------------------------------------
st.set_page_config(
    page_title="LeetCode & Remote Jobs BR",
    page_icon="⚡",
    layout="wide"
)

# Estilização CSS: Sidebar Moderna + Cards Elegantes + Rodapé do Autor
st.markdown("""
    <style>
    /* Estilo da Barra Lateral */
    [data-testid="stSidebar"] {
        background-color: #0f172a;
        color: #f8fafc;
    }
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3, 
    [data-testid="stSidebar"] label, [data-testid="stSidebar"] p {
        color: #f1f5f9 !important;
    }
    
    /* Box do Autor & Contador no Rodapé da Sidebar */
    .author-box {
        background-color: #1e293b;
        border-radius: 8px;
        padding: 12px;
        margin-top: 20px;
        border: 1px solid #334155;
        text-align: center;
    }
    .author-box p {
        margin: 0;
        font-size: 0.85rem;
        color: #94a3b8 !important;
    }
    .author-box a {
        display: inline-block;
        margin-top: 8px;
        padding: 6px 12px;
        background-color: #0077b5;
        color: white !important;
        text-decoration: none;
        border-radius: 5px;
        font-weight: bold;
        font-size: 0.8rem;
    }
    .author-box a:hover {
        background-color: #005582;
    }

    /* Cards de Estatísticas e Feed */
    .metric-card {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 18px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        border-top: 4px solid #3b82f6;
    }
    .comment-card {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 16px;
        margin-bottom: 16px;
        border-left: 5px solid #10b981;
        box-shadow: 0 2px 6px rgba(0,0,0,0.04);
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. CONTADOR DE ACESSOS DA PLATAFORMA
# ---------------------------------------------------------
COUNTER_FILE = "contador_acessos.json"

def registrar_acesso():
    if "acesso_registrado" not in st.session_state:
        st.session_state["acesso_registrado"] = True
        total_acessos = 1
        if os.path.exists(COUNTER_FILE):
            try:
                with open(COUNTER_FILE, "r", encoding="utf-8") as f:
                    dados = json.load(f)
                    total_acessos = dados.get("acessos", 0) + 1
            except Exception:
                total_acessos = 1
        
        with open(COUNTER_FILE, "w", encoding="utf-8") as f:
            json.dump({"acessos": total_acessos}, f)
        return total_acessos
    else:
        if os.path.exists(COUNTER_FILE):
            try:
                with open(COUNTER_FILE, "r", encoding="utf-8") as f:
                    dados = json.load(f)
                    return dados.get("acessos", 1)
            except Exception:
                return 1
        return 1

total_visitas = registrar_acesso()

# ---------------------------------------------------------
# 3. MAPEAMENTO COMPLETO DE LOGOS & LINKS DE CAREERS
# ---------------------------------------------------------
LOGOS_EMPRESAS = {
    # Big Techs & Mapeamento Anterior
    "Accenture": "https://upload.wikimedia.org/wikipedia/commons/c/cd/Accenture.svg",
    "Adobe": "https://upload.wikimedia.org/wikipedia/commons/8/8d/Adobe_corporate_logo.svg",
    "Airbnb": "https://upload.wikimedia.org/wikipedia/commons/6/69/Airbnb_Logo_B%C3%A9lo.svg",
    "Amazon": "https://upload.wikimedia.org/wikipedia/commons/a/a9/Amazon_logo.svg",
    "Apple": "https://upload.wikimedia.org/wikipedia/commons/f/fa/Apple_logo_black.svg",
    "Bloomberg": "https://upload.wikimedia.org/wikipedia/commons/7/75/Bloomberg_logo.svg",
    "Cisco": "https://upload.wikimedia.org/wikipedia/commons/0/08/Cisco_logo_blue_2016.svg",
    "DoorDash": "https://upload.wikimedia.org/wikipedia/commons/4/4c/DoorDash_Logo.svg",
    "eBay": "https://upload.wikimedia.org/wikipedia/commons/1/1b/EBay_logo.svg",
    "Facebook": "https://upload.wikimedia.org/wikipedia/commons/7/7b/Meta_Platforms_Inc._logo.svg",
    "Goldman Sachs": "https://upload.wikimedia.org/wikipedia/commons/6/61/Goldman_Sachs.svg",
    "Google": "https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_2015_logo.svg",
    "LinkedIn": "https://upload.wikimedia.org/wikipedia/commons/0/01/LinkedIn_Logo.svg",
    "Lyft": "https://upload.wikimedia.org/wikipedia/commons/a/a4/Lyft_logo.svg",
    "Meta": "https://upload.wikimedia.org/wikipedia/commons/7/7b/Meta_Platforms_Inc._logo.svg",
    "Microsoft": "https://upload.wikimedia.org/wikipedia/commons/9/96/Microsoft_logo_%282012%29.svg",
    "Netflix": "https://upload.wikimedia.org/wikipedia/commons/0/08/Netflix_2015_logo.svg",
    "Oracle": "https://upload.wikimedia.org/wikipedia/commons/5/50/Oracle_logo.svg",
    "Palantir": "https://upload.wikimedia.org/wikipedia/commons/1/13/Palantir_Technologies_logo.svg",
    "PayPal": "https://upload.wikimedia.org/wikipedia/commons/b/b5/PayPal.svg",
    "Salesforce": "https://upload.wikimedia.org/wikipedia/commons/f/f9/Salesforce.com_logo.svg",
    "Snapchat": "https://upload.wikimedia.org/wikipedia/en/c/c4/Snapchat_logo.svg",
    "Spotify": "https://upload.wikimedia.org/wikipedia/commons/1/19/Spotify_logo_without_text.svg",
    "Twitter": "https://upload.wikimedia.org/wikipedia/commons/6/6f/Logo_of_Twitter.svg",
    "Uber": "https://upload.wikimedia.org/wikipedia/commons/c/cc/Uber_logo_2018.png",
    "Yahoo": "https://upload.wikimedia.org/wikipedia/commons/3/36/Yahoo%21_logo_2019.svg",
    
    # Novas Empresas Adicionadas
    "37Signals": "https://37signals.com/images/37signals-logo.svg",
    "Buffer": "https://upload.wikimedia.org/wikipedia/commons/3/3a/Buffer_logo.svg",
    "Datadog": "https://upload.wikimedia.org/wikipedia/commons/4/41/Datadog_logo.svg",
    "Deel": "https://upload.wikimedia.org/wikipedia/commons/e/e0/Deel_logo.svg",
    "Discourse": "https://upload.wikimedia.org/wikipedia/commons/8/80/Discourse_logo.svg",
    "DuckDuckGo": "https://upload.wikimedia.org/wikipedia/commons/d/d3/DuckDuckGo_logo.svg",
    "Elastic": "https://upload.wikimedia.org/wikipedia/commons/1/15/Elasticsearch_logo.svg",
    "Epic Games": "https://upload.wikimedia.org/wikipedia/commons/3/31/Epic_Games_logo.svg",
    "GitLab": "https://upload.wikimedia.org/wikipedia/commons/e/e1/GitLab_logo.svg",
    "MongoDB": "https://upload.wikimedia.org/wikipedia/commons/9/93/MongoDB_Logo.svg",
    "Quora": "https://upload.wikimedia.org/wikipedia/commons/9/91/Quora_logo_2015.svg",
    "Red Hat": "https://upload.wikimedia.org/wikipedia/commons/d/d8/Red_Hat_logo.svg",
    "Revolut": "https://upload.wikimedia.org/wikipedia/commons/c/ca/Revolut_logo.svg",
    "Rocket.Chat": "https://upload.wikimedia.org/wikipedia/commons/6/66/Rocket.Chat_logo.svg",
    "Stripe": "https://upload.wikimedia.org/wikipedia/commons/b/ba/Stripe_Logo%2C_revised_2016.svg",
    "Wikimedia": "https://upload.wikimedia.org/wikipedia/commons/8/81/Wikimedia-logo.svg",
    "Zapier": "https://upload.wikimedia.org/wikipedia/commons/9/90/Zapier_logo.svg"
}

CAREERS_LINKS = {
    # Lista Anterior
    "Accenture": "https://www.accenture.com/br-pt/careers",
    "Adobe": "https://www.adobe.com/careers.html",
    "Airbnb": "https://careers.airbnb.com/",
    "Amazon": "https://www.amazon.jobs/",
    "Apple": "https://www.apple.com/careers/br/",
    "Bloomberg": "https://www.bloomberg.com/company/careers/",
    "Cisco": "https://jobs.cisco.com/",
    "DoorDash": "https://careers.doordash.com/",
    "eBay": "https://careers.ebayinc.com/",
    "Facebook": "https://www.metacareers.com/",
    "Goldman Sachs": "https://www.goldmansachs.com/careers/",
    "Google": "https://www.google.com/about/careers/applications/jobs/results/",
    "LinkedIn": "https://careers.linkedin.com/",
    "Lyft": "https://www.lyft.com/careers",
    "Meta": "https://www.metacareers.com/",
    "Microsoft": "https://jobs.careers.microsoft.com/global/en/search?lc=Brazil&p=Software%20Engineering&l=en_us&pg=1&pgSz=20&o=Relevance&flt=true",
    "Netflix": "https://jobs.netflix.com/",
    "Oracle": "https://www.oracle.com/corporate/careers/",
    "Palantir": "https://www.palantir.com/careers/",
    "PayPal": "https://www.paypal.com/us/webapps/mpp/jobs",
    "Salesforce": "https://www.salesforce.com/company/careers/",
    "Snapchat": "https://careers.snap.com/",
    "Spotify": "https://lifeatspotify.com/",
    "Twitter": "https://careers.x.com/",
    "Uber": "https://www.uber.com/us/en/careers/",
    "Yahoo": "https://www.yahooinc.com/careers/",

    # Novas Empresas Adicionadas
    "37Signals": "https://37signals.com/jobs/",
    "Aha!": "https://www.aha.io/company/careers/current-openings",
    "Actabl": "https://actabl.com/",
    "Appcues": "https://www.appcues.com/company#jobs-open",
    "Appwrite": "https://www.appwrite.careers/platform-engineer/en",
    "Argyle": "https://argyle.com/careers#open-positions",
    "Bandcamp": "https://www.songtradr.com/careers",
    "Bandlab": "https://bandlabtechnologies.com/careers/",
    "Bandzoogle": "https://bandzoogle.com/jobs",
    "BeBanjo": "https://www.bebanjo.com/company/careers",
    "RequestTracker": "https://requesttracker.com/careers/",
    "Bitovi": "https://www.bitovi.com/about/jobs",
    "Bonsai": "https://apply.workable.com/hellobonsai/?lng=en",
    "Buffer": "https://buffer.com/salaries",
    "Chess.com": "https://www.chess.com/jobs",
    "CodeSandbox": "https://codesandbox.io/careers",
    "Convert": "https://convert.recruit.charliehr.com/careers",
    "Customer.io": "https://customer.io/careers#job-openings",
    "Datadog": "https://careers.datadoghq.com/remote/",
    "Deel": "https://jobs.ashbyhq.com/Deel",
    "Delighted": "https://delighted.com/jobs",
    "Discourse": "https://www.discourse.org/team",
    "Doist": "https://doist.com/careers#open-roles",
    "DuckDuckGo": "https://duckduckgo.com/hiring",
    "Elastic": "https://jobs.elastic.co/jobs/department/engineering?size=n_20_n",
    "Emsisoft": "https://wellfound.com/company/emsisoft",
    "Envato": "https://jobs.lever.co/envato-2",
    "Epic Games": "https://www.epicgames.com/site/en-US/careers/jobs?country=Brazil&department=Engineering&page=1",
    "Epsy": "https://www.epsyhealth.com/careers",
    "Ergeon": "https://www.ergeon.com/careers/",
    "Eyeo": "https://eyeo.com/careers?office=29172640",
    "Fingerprint": "https://fingerprint.com/careers/jobs/",
    "GitLab": "https://about.gitlab.com/jobs/all-jobs/",
    "Iterative": "https://jobs.lever.co/iterative?lever-origin=applied&lever-source%5B%5D=remoteintech",
    "Komoot": "https://apply.workable.com/komoot/",
    "MailerLite": "https://www.mailerlite.com/jobs",
    "Mixmax": "https://www.mixmax.com/careers?hsCtaAttrib=158184435311#open-positions",
    "Mixrank": "https://app.dover.com/jobs/mixrank",
    "MongoDB": "https://www.mongodb.com/company/careers/teams/engineering",
    "OpenCraft": "https://opencraft.com/jobs/",
    "Parabol": "https://www.parabol.co/join/",
    "Plex": "https://www.plex.tv/careers/",
    "Primer": "https://primer.io/careers",
    "Prisma": "https://www.prisma.io/careers#current",
    "QuestDB": "https://questdb.com/careers/core-database-engineer/",
    "Quora": "https://jobs.ashbyhq.com/quora",
    "Recharge": "https://job-boards.greenhouse.io/recharge",
    "Red Hat": "https://www.redhat.com/en/jobs",
    "Revolut": "https://www.revolut.com/careers/",
    "Rocket.Chat": "https://www.rocket.chat/jobs",
    "Sardine": "https://www.sardine.ai/careers#openings",
    "Semaphore": "https://semaphore.io/hiring",
    "Skillshare": "https://jobs.lever.co/skillshare",
    "StickerMule": "https://www.stickermule.com/careers",
    "Stripe": "https://stripe.com/jobs/search?remote_locations=Latin+America--Brazil+Remote",
    "SweetRush": "https://www.sweetrush.com/join-us#current-openings",
    "TestGorilla": "https://www.testgorilla.com/careers/#jobs",
    "Toggl": "https://toggl.com/jobs/#jobs",
    "Varnish": "https://varnish-software.teamtailor.com/jobs",
    "Wikimedia": "https://wikimediafoundation.org/jobs/#section-8",
    "Wildbit": "https://www.wildbit.com/jobs",
    "Zapier": "https://zapier.com/jobs#job-openings"
}
EMPRESAS_DISPONIVEIS = sorted(list(LOGOS_EMPRESAS.keys()))

# ---------------------------------------------------------
# 4. GERENCIAMENTO DE ARQUIVOS DE DADOS (JSON)
# ---------------------------------------------------------
COMMENTS_FILE = "comentarios_comunidade.json"
VAGAS_FILE = "vagas_comunidade.json"

def carregar_comentarios():
    if os.path.exists(COMMENTS_FILE):
        try:
            with open(COMMENTS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []

def salvar_comentario(nome, empresa, questoes, depoimento):
    comentarios = carregar_comentarios()
    novo = {
        "id": len(comentarios) + 1,
        "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "nome": nome if nome else "Dev Anônimo",
        "empresa": empresa,
        "questoes": questoes,
        "depoimento": depoimento,
        "respostas": []
    }
    comentarios.append(novo)
    with open(COMMENTS_FILE, "w", encoding="utf-8") as f:
        json.dump(comentarios, f, ensure_ascii=False, indent=4)

def salvar_resposta(comentario_id, nome, resposta_texto):
    comentarios = carregar_comentarios()
    for c in comentarios:
        if c["id"] == comentario_id:
            c["respostas"].append({
                "nome": nome if nome else "Dev Anônimo",
                "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
                "texto": resposta_texto
            })
            break
    with open(COMMENTS_FILE, "w", encoding="utf-8") as f:
        json.dump(comentarios, f, ensure_ascii=False, indent=4)

def carregar_vagas_ativas():
    if os.path.exists(VAGAS_FILE):
        try:
            with open(VAGAS_FILE, "r", encoding="utf-8") as f:
                vagas = json.load(f)
            
            hoje = date.today().strftime("%Y-%m-%d")
            vagas_validas = [v for v in vagas if v.get("data_fechamento", "2099-12-31") >= hoje]
            
            if len(vagas_validas) != len(vagas):
                with open(VAGAS_FILE, "w", encoding="utf-8") as f:
                    json.dump(vagas_validas, f, ensure_ascii=False, indent=4)
                    
            return vagas_validas
        except Exception:
            return []
    return []

def salvar_vaga(empresa, cargo, modelo, ingles, link, data_fechamento):
    vagas = carregar_vagas_ativas()
    nova_vaga = {
        "Empresa": empresa,
        "Cargo": cargo,
        "Modelo": modelo,
        "Nível Inglês": ingles,
        "Link": link,
        "data_fechamento": str(data_fechamento)
    }
    vagas.append(nova_vaga)
    with open(VAGAS_FILE, "w", encoding="utf-8") as f:
        json.dump(vagas, f, ensure_ascii=False, indent=4)

# Cabeçalho Principal
st.title("⚡ LeetCode Hub & Vagas Remotas BR")
st.write("Hub colaborativo com questões de Big Techs, portais de carreiras e vagas de programação.")

aba1, aba2, aba3, aba4 = st.tabs([
    "📊 LeetCode Hub", 
    "🏢 Vagas Remotas (Comunidade)", 
    "💬 Feed da Comunidade",
    "🌐 Portais Oficiais de Carreiras"
])

# =========================================================
# ABA 1: LEETCODE HUB
# =========================================================
with aba1:
    st.sidebar.header("🎯 Filtros do LeetCode")
    
    empresa_selecionada = st.sidebar.selectbox("Selecione a Empresa:", options=EMPRESAS_DISPONIVEIS)
    
    url_csv = f"https://raw.githubusercontent.com/liquidslr/leetcode-company-wise-problems/main/{empresa_selecionada}/5.%20All.csv"
    
    try:
        df = pd.read_csv(url_csv)
        
        # Filtro por Dificuldade
        col_dif = [c for c in df.columns if 'difficulty' in c.lower()]
        if col_dif:
            nome_col_dif = col_dif[0]
            dificuldades = st.sidebar.multiselect("Filtrar por Dificuldade:", options=df[nome_col_dif].unique())
            if dificuldades:
                df = df[df[nome_col_dif].isin(dificuldades)]
        
        # Filtro por Termo de Busca
        busca_termo = st.sidebar.text_input("🔍 Buscar no Título/Tópicos:")
        if busca_termo:
            col_titulo = [c for c in df.columns if 'title' in c.lower()]
            col_topicos = [c for c in df.columns if 'topic' in c.lower()]
            
            condicao_titulo = df[col_titulo[0]].str.contains(busca_termo, case=False, na=False) if col_titulo else False
            condicao_topico = df[col_topicos[0]].str.contains(busca_termo, case=False, na=False) if col_topicos else False
            
            df = df[condicao_titulo | condicao_topico]

        # Topo com Logo e Métricas
        col_logo, col_info, col_metrica = st.columns([1, 2, 2])
        
        with col_logo:
            logo_url = LOGOS_EMPRESAS.get(empresa_selecionada)
            if logo_url:
                st.image(logo_url, width=110)
            
        with col_info:
            st.subheader(f"Empresa: {empresa_selecionada}")
            st.caption("Questões filtradas diretamente do banco oficial.")
            if empresa_selecionada in CAREERS_LINKS:
                st.link_button(f"🔗 Página de Carreiras da {empresa_selecionada}", CAREERS_LINKS[empresa_selecionada])
            
        with col_metrica:
            st.metric("Total de Questões Mapeadas", len(df))

        st.divider()

        # Identificar coluna de Link dinamicamente
        col_link = [c for c in df.columns if 'url' in c.lower() or 'link' in c.lower()]
        cfg_colunas = {}
        if col_link:
            cfg_colunas[col_link[0]] = st.column_config.LinkColumn("Exercício no LeetCode")

        st.dataframe(
            df,
            column_config=cfg_colunas,
            use_container_width=True,
            height=450
        )

    except Exception as e:
        st.warning(f"Não foi possível carregar os dados de **{empresa_selecionada}**.")

# =========================================================
# ABA 2: VAGAS REMOTAS (POSTAR + AUTO-EXPIRAÇÃO)
# =========================================================
with aba2:
    st.header("🏢 Quadro de Vagas Remotas (Devs BR)")
    st.write("Vagas ativas cadastradas pela comunidade. As vagas expiradas são removidas automaticamente.")
    
    with st.expander("➕ **Publicar Nova Vaga Remota**", expanded=False):
        with st.form("form_vagas", clear_on_submit=True):
            col_v1, col_v2 = st.columns(2)
            with col_v1:
                v_empresa = st.text_input("Nome da Empresa:")
                v_cargo = st.text_input("Cargo / Título da Vaga (ex: Dev Python Jr):")
                v_link = st.text_input("Link para Candidatura:")
            with col_v2:
                v_modelo = st.selectbox("Modelo de Contratação:", ["PJ (Internacional/Gringa)", "CLT (Brasil)", "PJ (Brasil)", "Estágio Remoto"])
                v_ingles = st.selectbox("Inglês Exigido:", ["Não Exigido / Básico", "Intermediário", "Avançado / Fluente"])
                v_fechamento = st.date_input("Data de Encerramento das Inscrições:", value=date.today())
            
            sub_vaga = st.form_submit_button("📢 Publicar Vaga")
            
            if sub_vaga:
                if v_empresa and v_cargo and v_link:
                    salvar_vaga(v_empresa, v_cargo, v_modelo, v_ingles, v_link, v_fechamento)
                    st.success("Vaga publicada com sucesso!")
                    st.rerun()
                else:
                    st.error("Preencha ao menos Empresa, Cargo e Link.")

    st.divider()
    
    vagas_atuais = carregar_vagas_ativas()
    df_vagas = pd.DataFrame(vagas_atuais)
    
    if not df_vagas.empty:
        df_vagas_exibicao = df_vagas.rename(columns={"data_fechamento": "Encerramento Inscrições"})
        st.dataframe(
            df_vagas_exibicao,
            column_config={
                "Link": st.column_config.LinkColumn("Link da Vaga"),
                "Encerramento Inscrições": st.column_config.DateColumn("Prazo Limite", format="DD/MM/YYYY")
            },
            use_container_width=True
        )
    else:
        st.info("Nenhuma vaga ativa no momento. Seja o primeiro a divulgar uma!")

# =========================================================
# ABA 3: FEED DA COMUNIDADE
# =========================================================
with aba3:
    st.header("💬 Feed de Relatos & Experiências")
    st.write("Poste o que caiu na sua entrevista técnica e troque ideias com os colegas.")
    
    with st.expander("➕ **Postar Novo Relato de Entrevista**", expanded=False):
        with st.form("form_comentario", clear_on_submit=True):
            nome_user = st.text_input("Seu Nome / Nick:")
            empresa_user = st.selectbox("Empresa:", EMPRESAS_DISPONIVEIS + ["Outra"])
            questoes_user = st.text_input("Questões / Algoritmos cobrados:")
            depoimento_user = st.text_area("Seu relato ou conselho de estudo:")
            
            submeter = st.form_submit_button("🚀 Postar Relato")
            if submeter and depoimento_user.strip():
                salvar_comentario(nome_user, empresa_user, questoes_user, depoimento_user)
                st.success("Publicado!")
                st.rerun()

    st.divider()
    comentarios = carregar_comentarios()
    
    for c in reversed(comentarios):
        st.markdown(f"""
            <div class="comment-card">
                <h4>🏢 {c['empresa']} - <small style="color:gray;">{c['nome']} ({c['data']})</small></h4>
                <p><b>Questões citadas:</b> {c['questoes']}</p>
                <p>{c['depoimento']}</p>
            </div>
        """, unsafe_allow_html=True)
        
        if c["respostas"]:
            for resp in c["respostas"]:
                st.caption(f"↳ 💬 **{resp['nome']}** ({resp['data']}): {resp['texto']}")
        
        with st.expander(f"💬 Responder a {c['nome']}", expanded=False):
            with st.form(f"form_resp_{c['id']}", clear_on_submit=True):
                nome_resp = st.text_input("Seu nome:", key=f"n_{c['id']}")
                txt_resp = st.text_area("Sua resposta:", key=f"t_{c['id']}")
                if st.form_submit_button("Enviar Resposta") and txt_resp.strip():
                    salvar_resposta(c["id"], nome_resp, txt_resp)
                    st.rerun()

# =========================================================
# ABA 4: PORTAIS OFICIAIS DE CARREIRAS
# =========================================================
with aba4:
    st.header("🌐 Portais Oficiais de Carreiras - Big Techs & Multinacionais")
    st.write("Acesse diretamente a página de carreiras/vagas oficiais de cada grande empresa.")
    
    col_busca, _ = st.columns([2, 2])
    with col_busca:
        filtro_empresa = st.text_input("🔍 Buscar empresa por nome:", "")

    st.divider()

    # Filtrar empresas com base na busca
    empresas_filtradas = [emp for emp in CAREERS_LINKS.keys() if filtro_empresa.lower() in emp.lower()]

    if empresas_filtradas:
        cols = st.columns(3)
        for index, emp in enumerate(empresas_filtradas):
            col = cols[index % 3]
            url_carr = CAREERS_LINKS[emp]
            logo_url = LOGOS_EMPRESAS.get(emp, "")

            with col:
                st.markdown(f"""
                    <div style="
                        background-color: #ffffff;
                        border: 1px solid #e2e8f0;
                        border-radius: 12px;
                        padding: 16px;
                        margin-bottom: 16px;
                        text-align: center;
                        box-shadow: 0 4px 6px rgba(0,0,0,0.03);
                    ">
                        <img src="{logo_url}" style="height: 40px; max-width: 120px; object-fit: contain; margin-bottom: 12px;" />
                        <h4 style="margin: 0 0 10px 0; font-size: 1.1rem; color: #0f172a;">{emp}</h4>
                        <a href="{url_carr}" target="_blank" style="
                            display: inline-block;
                            padding: 8px 16px;
                            background-color: #2563eb;
                            color: white !important;
                            text-decoration: none;
                            border-radius: 6px;
                            font-weight: 600;
                            font-size: 0.85rem;
                        ">🚀 Ver Vagas Abertas</a>
                    </div>
                """, unsafe_allow_html=True)
    else:
        st.info("Nenhuma empresa encontrada com este nome.")

# =========================================================
# RODAPÉ DA BARRA LATERAL (CONTADOR DE ACESSOS & LINKEDIN)
# =========================================================
st.sidebar.markdown("---")
st.sidebar.markdown(f"👀 **Acessos à Plataforma:** `{total_visitas}`")

st.sidebar.markdown("""
    <div class="author-box">
        <p>Desenvolvido por</p>
        <p style="font-weight: bold; color: #f8fafc !important; font-size: 0.95rem;">Lucas Eduardo Dias</p>
        <a href="https://www.linkedin.com/in/lucaseduardodias/" target="_blank">
            🔗 Meu LinkedIn
        </a>
    </div>
""", unsafe_allow_html=True)
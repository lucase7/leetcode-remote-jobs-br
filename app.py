import streamlit as st

# =========================================================
# CONFIGURAÇÃO DA PÁGINA
# =========================================================
st.set_page_config(
    page_title="Filtros & Vagas - LeetCode e Carreiras",
    page_icon="🚀",
    layout="wide"
)

# Estilização CSS adicional para garantir um visual limpo e moderno
st.markdown("""
    <style>
        .stApp {
            background-color: #f8fafc;
        }
        /* Ajuste fino nas abas */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
        }
        .stTabs [data-baseweb="tab"] {
            padding: 8px 16px;
            border-radius: 6px;
        }
    </style>
""", unsafe_allow_html=True)


# =========================================================
# DICIONÁRIO DE EMPRESAS (ABA 4 - PORTAIS DE CARREIRAS)
# =========================================================
EMPRESAS_DATA = {
    "37Signals": {
        "link": "https://37signals.com/jobs",
        "logo": "https://img.stackshare.io/service/1063/default_5c0106404ebfa468903c5dcf742ab1aa2468f7f5.png",
        "remote_first": True
    },
    "Accenture": {
        "link": "https://www.accenture.com/careers",
        "logo": "https://logo.clearbit.com/accenture.com",
        "remote_first": False
    },
    "Actabl": {
        "link": "https://actabl.com/careers",
        "logo": "",
        "remote_first": True
    },
    "Adobe": {
        "link": "https://adobe.design/careers",
        "logo": "https://logo.clearbit.com/adobe.com",
        "remote_first": False
    },
    "Aha!": {
        "link": "https://www.aha.io/company/careers",
        "logo": "",
        "remote_first": True
    },
    "Airbnb": {
        "link": "https://careers.airbnb.com/",
        "logo": "https://logo.clearbit.com/airbnb.com",
        "remote_first": False
    },
    "Amazon": {
        "link": "https://www.amazon.jobs/",
        "logo": "https://logo.clearbit.com/amazon.com",
        "remote_first": False
    },
    "Appcues": {
        "link": "https://www.appcues.com/careers",
        "logo": "",
        "remote_first": True
    },
    "Apple": {
        "link": "https://jobs.apple.com/",
        "logo": "https://logo.clearbit.com/apple.com",
        "remote_first": False
    },
    "Appwrite": {
        "link": "https://appwrite.careers/",
        "logo": "",
        "remote_first": True
    },
    "Automattic": {
        "link": "https://automattic.com/work-with-us/",
        "logo": "https://logo.clearbit.com/automattic.com",
        "remote_first": True
    },
    "Buffer": {
        "link": "https://buffer.com/journey",
        "logo": "https://logo.clearbit.com/buffer.com",
        "remote_first": True
    },
    "Canva": {
        "link": "https://www.canva.com/careers/",
        "logo": "https://logo.clearbit.com/canva.com",
        "remote_first": True
    },
    "Doist": {
        "link": "https://doist.com/careers",
        "logo": "",
        "remote_first": True
    },
    "Elastic": {
        "link": "https://www.elastic.co/about/careers",
        "logo": "https://logo.clearbit.com/elastic.co",
        "remote_first": True
    },
    "GitLab": {
        "link": "https://about.gitlab.com/jobs/",
        "logo": "https://logo.clearbit.com/gitlab.com",
        "remote_first": True
    },
    "GitHub": {
        "link": "https://github.com/about/careers",
        "logo": "https://logo.clearbit.com/github.com",
        "remote_first": True
    },
    "Google": {
        "link": "https://www.google.com/about/careers/",
        "logo": "https://logo.clearbit.com/google.com",
        "remote_first": False
    },
    "Meta": {
        "link": "https://www.metacareers.com/",
        "logo": "https://logo.clearbit.com/meta.com",
        "remote_first": False
    },
    "Microsoft": {
        "link": "https://careers.microsoft.com/",
        "logo": "https://logo.clearbit.com/microsoft.com",
        "remote_first": False
    },
    "Mozilla": {
        "link": "https://www.mozilla.org/en-US/careers/",
        "logo": "https://logo.clearbit.com/mozilla.org",
        "remote_first": True
    },
    "Netflix": {
        "link": "https://jobs.netflix.com/",
        "logo": "https://logo.clearbit.com/netflix.com",
        "remote_first": False
    },
    "Shopify": {
        "link": "https://www.shopify.com/careers",
        "logo": "https://logo.clearbit.com/shopify.com",
        "remote_first": True
    },
    "Stripe": {
        "link": "https://stripe.com/jobs",
        "logo": "https://logo.clearbit.com/stripe.com",
        "remote_first": True
    },
    "Trello": {
        "link": "https://trello.com/about/careers",
        "logo": "https://logo.clearbit.com/trello.com",
        "remote_first": True
    },
    "Uber": {
        "link": "https://www.uber.com/us/en/careers/",
        "logo": "https://logo.clearbit.com/uber.com",
        "remote_first": False
    },
    "Zapier": {
        "link": "https://zapier.com/jobs",
        "logo": "https://logo.clearbit.com/zapier.com",
        "remote_first": True
    }
}


# =========================================================
# BARRA LATERAL (SIDEBAR)
# =========================================================
with st.sidebar:
    st.title("🎯 Filtros do LeetCode")
    
    empresa_selecionada = st.selectbox(
        "Selecione a Empresa:",
        list(EMPRESAS_DATA.keys())
    )
    
    st.divider()
    
    st.markdown("👀 **Acessos à Plataforma:** `13`")
    
    st.divider()
    
    st.markdown("""
        <div style="text-align: center; background-color: #1e293b; padding: 16px; border-radius: 8px; color: white;">
            <p style="margin-bottom: 8px; font-size: 0.85rem;">Desenvolvido por<br><strong>Lucas Eduardo Dias</strong></p>
            <a href="https://www.linkedin.com" target="_blank" style="
                display: inline-block;
                padding: 6px 12px;
                background-color: #0077b5;
                color: white !important;
                text-decoration: none;
                border-radius: 4px;
                font-size: 0.8rem;
                font-weight: bold;
            ">👔 Meu LinkedIn</a>
        </div>
    """, unsafe_allow_html=True)


# =========================================================
# CONTEÚDO PRINCIPAL (ABAS)
# =========================================================
aba1, aba2, aba3, aba4 = st.tabs([
    "💡 Voltar para LICs",
    "📅 Cronograma de Est...",
    "💻 LeetCode - The Wor...",
    "🌐 Portais Oficiais de Carreiras"
])

# ---------------------------------------------------------
# ABA 1
# ---------------------------------------------------------
with aba1:
    st.header("💡 Voltar para LICs")
    st.write("Conteúdo e instruções sobre Licenças e Certificações.")

# ---------------------------------------------------------
# ABA 2
# ---------------------------------------------------------
with aba2:
    st.header("📅 Cronograma de Estudos")
    st.write("Organização do seu plano de preparação para entrevistas técnicas.")

# ---------------------------------------------------------
# ABA 3
# ---------------------------------------------------------
with aba3:
    st.header("💻 LeetCode - The World")
    st.write(f"Questões mais frequentes da empresa selecionada: **{empresa_selecionada}**.")

# ---------------------------------------------------------
# ABA 4: PORTAIS OFICIAIS DE CARREIRAS (CORRIGIDO)
# ---------------------------------------------------------
with aba4:
    st.header("🌐 Portais Oficiais de Carreiras - Big Techs & Multinacionais")
    st.write("Acesse diretamente a página de carreiras/vagas oficiais de cada grande empresa.")
    
    col_busca, col_filtro = st.columns([2, 1])
    with col_busca:
        filtro_empresa = st.text_input("🔍 Buscar empresa por nome:", "")
    with col_filtro:
        apenas_remotas = st.checkbox("🟢 Apenas 100% Remotas (Remote-First)", value=False)

    st.divider()

    # Filtrar empresas com base na busca e modalidade
    empresas_filtradas = {}
    for nome, dados in sorted(EMPRESAS_DATA.items()):
        if filtro_empresa and filtro_empresa.lower() not in nome.lower():
            continue
        if apenas_remotas and not dados["remote_first"]:
            continue
        empresas_filtradas[nome] = dados

    if empresas_filtradas:
        cols = st.columns(3)
        for index, (emp, dados) in enumerate(empresas_filtradas.items()):
            col = cols[index % 3]
            url_carr = dados["link"]
            logo_url = dados["logo"]
            is_remote = dados["remote_first"]
            
            tag_modelo = "🟢 100% Remota" if is_remote else "🏢 Híbrida / Presencial"

            with col:
                # Renderiza o card completo com HTML seguro (unsafe_allow_html=True)
                if logo_url:
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
                            <h4 style="margin: 0 0 4px 0; font-size: 1.1rem; color: #0f172a;">{emp}</h4>
                            <p style="margin: 0 0 10px 0; font-size: 0.8rem; color: #64748b;">{tag_modelo}</p>
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
                            <div style="
                                height: 40px;
                                display: flex;
                                align-items: center;
                                justify-content: center;
                                background-color: #f1f5f9;
                                border-radius: 6px;
                                font-weight: bold;
                                color: #475569;
                                margin-bottom: 12px;
                                font-size: 0.9rem;
                            ">
                                🏢 {emp}
                            </div>
                            <h4 style="margin: 0 0 4px 0; font-size: 1.1rem; color: #0f172a;">{emp}</h4>
                            <p style="margin: 0 0 10px 0; font-size: 0.8rem; color: #64748b;">{tag_modelo}</p>
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
        st.info("Nenhuma empresa encontrada com estes critérios.")
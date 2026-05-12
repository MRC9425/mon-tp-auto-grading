"""
app_dashboard.py - Dashboard Streamlit pour l'auto-grading TP Python
Affiche progression, statistiques, comparaisons élèves
"""

import streamlit as st
import sqlite3
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import numpy as np
from pathlib import Path

# Configuration Streamlit
st.set_page_config(
    page_title="📊 Auto-Grading Dashboard",
    page_icon="📊",
    layout="wide"
)

# ==================== BASE DE DONNÉES ====================

DB_PATH = "resultats.db"

def get_eleves():
    """Récupère les élèves qui ont au moins un résultat"""
    with sqlite3.connect(DB_PATH) as conn:
        return pd.read_sql_query(
            "SELECT DISTINCT e.id, e.nom, e.email, e.date_inscription "
            "FROM eleves e JOIN resultats r ON e.id = r.eleve_id "
            "ORDER BY e.nom",
            conn
        )

def get_resultats():
    """Récupère tous les résultats"""
    with sqlite3.connect(DB_PATH) as conn:
        return pd.read_sql_query(
            "SELECT * FROM resultats ORDER BY date_test DESC",
            conn
        )

def get_tp_metadata():
    """Récupère les métadonnées des TPs"""
    with sqlite3.connect(DB_PATH) as conn:
        return pd.read_sql_query(
            "SELECT tp_name, nombre_exercices, description FROM tp_metadata ORDER BY tp_name",
            conn
        )

# ==================== CALCULS ====================

def calculate_stats():
    """Calcule les statistiques globales"""
    resultats = get_resultats()
    
    if resultats.empty:
        return {
            'total_eleves': 0,
            'taux_reussite_global': 0,
            'moyenne_exercices': 0,
            'eleves_actifs': 0
        }
    
    # Nombre d'élèves
    total_eleves = resultats['eleve_id'].nunique()
    
    # Taux de réussite global
    taux_reussite = (resultats['statut'] == 'PASSED').sum() / len(resultats) * 100
    
    # Moyenne d'exercices réussis par élève
    by_eleve = resultats.groupby('eleve_id').apply(
        lambda x: (x['statut'] == 'PASSED').sum() / len(x) * 100
    )
    moyenne_exercices = by_eleve.mean() if len(by_eleve) > 0 else 0
    
    # Élèves actifs (derniers 7 jours)
    date_limite = datetime.now() - timedelta(days=7)
    resultats['date_test'] = pd.to_datetime(resultats['date_test'], format='mixed')
    eleves_actifs = resultats[resultats['date_test'] > date_limite]['eleve_id'].nunique()
    
    return {
        'total_eleves': total_eleves,
        'taux_reussite_global': round(taux_reussite, 1),
        'moyenne_exercices': round(moyenne_exercices, 1),
        'eleves_actifs': eleves_actifs
    }

def get_scores_by_eleve():
    """Score moyen par élève"""
    resultats = get_resultats()
    eleves = get_eleves()
    
    if resultats.empty:
        return pd.DataFrame()
    
    scores = resultats.groupby('eleve_id').apply(
        lambda x: {
            'score': (x['statut'] == 'PASSED').sum() / len(x) * 100,
            'total_tests': len(x)
        }
    ).apply(pd.Series)
    
    scores = scores.reset_index()
    scores = scores.merge(eleves[['id', 'nom']], left_on='eleve_id', right_on='id')
    scores = scores.sort_values('score', ascending=False)
    
    return scores

def get_exercices_difficulty():
    """Taux de réussite par exercice"""
    resultats = get_resultats()
    
    if resultats.empty:
        return pd.DataFrame()
    
    difficulty = resultats.groupby('tp_name').apply(
        lambda x: (x['statut'] == 'PASSED').sum() / len(x) * 100
    ).reset_index()
    difficulty.columns = ['tp_name', 'taux_reussite']
    difficulty = difficulty.sort_values('taux_reussite')
    
    return difficulty

def get_progression_timeline():
    """Progression au fil du temps"""
    resultats = get_resultats()
    eleves = get_eleves()
    
    if resultats.empty:
        return pd.DataFrame()
    
    resultats['date_test'] = pd.to_datetime(resultats['date_test'], format='mixed')
    resultats['date'] = resultats['date_test'].dt.date
    
    # Score cumulatif par jour
    timeline = resultats.groupby(['date', 'eleve_id']).apply(
        lambda x: (x['statut'] == 'PASSED').sum() / len(x) * 100
    ).reset_index(name='score')
    
    timeline = timeline.merge(eleves[['id', 'nom']], left_on='eleve_id', right_on='id')
    
    return timeline

def get_activite_hebdo():
    """Activité par jour de la semaine"""
    resultats = get_resultats()
    
    if resultats.empty:
        return pd.DataFrame()
    
    resultats['date_test'] = pd.to_datetime(resultats['date_test'], format='mixed')
    resultats['jour'] = resultats['date_test'].dt.day_name()
    resultats['semaine'] = resultats['date_test'].dt.isocalendar().week
    
    activite = resultats.groupby(['jour', 'eleve_id']).size().reset_index(name='nombre')
    
    return activite

# ==================== INTERFACE ====================

st.title("📊 Dashboard Auto-Grading TP Python")

# Onglets
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["📈 Vue d'ensemble", "📊 Progression", "🏆 Comparaisons", "❌ Exercices", "👤 Détails élève"]
)

# ==================== TAB 1: VUE D'ENSEMBLE ====================

with tab1:
    st.header("📈 Vue d'ensemble de la classe")
    
    stats = calculate_stats()
    
    # KPIs
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "👥 Total élèves",
            stats['total_eleves'],
            delta=None
        )
    
    with col2:
        st.metric(
            "✅ Taux global",
            f"{stats['taux_reussite_global']}%",
            delta=None
        )
    
    with col3:
        st.metric(
            "📚 Moyenne/élève",
            f"{stats['moyenne_exercices']}%",
            delta=None
        )
    
    with col4:
        st.metric(
            "🔥 Actifs (7j)",
            stats['eleves_actifs'],
            delta=None
        )
    
    st.divider()
    
    # Scores élèves
    st.subheader("🏆 Scores par élève")
    scores = get_scores_by_eleve()
    
    if not scores.empty:
        fig = px.bar(
            scores,
            x='nom',
            y='score',
            title="Score moyen par élève (%)",
            color='score',
            color_continuous_scale='RdYlGn',
            range_color=[0, 100],
            labels={'nom': 'Élève', 'score': 'Score (%)'}
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Tableau détaillé
        st.dataframe(
            scores[['nom', 'score', 'total_tests']].rename(
                columns={'nom': 'Élève', 'score': 'Score (%)', 'total_tests': 'Tests'}
            ),
            use_container_width=True,
            hide_index=True
        )

# ==================== TAB 2: PROGRESSION ====================

with tab2:
    st.header("📈 Progression au fil du temps")
    
    timeline = get_progression_timeline()
    
    if not timeline.empty:
        fig = px.line(
            timeline,
            x='date',
            y='score',
            color='nom',
            title="Progression des élèves (derniers 10 jours)",
            labels={'date': 'Date', 'score': 'Score (%)', 'nom': 'Élève'},
            markers=True
        )
        fig.update_yaxes(range=[0, 100])
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Pas encore de données de progression")

# ==================== TAB 3: COMPARAISONS ====================

with tab3:
    st.header("🏆 Comparaisons et classements")
    
    scores = get_scores_by_eleve()
    
    if not scores.empty:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🥇 Top performeurs")
            top = scores.head(5)[['nom', 'score']].reset_index(drop=True)
            top.index = top.index + 1
            st.dataframe(top, use_container_width=True)
        
        with col2:
            st.subheader("⚠️ À suivre")
            bottom = scores.tail(5)[['nom', 'score']].reset_index(drop=True)
            bottom = bottom.sort_values('score').reset_index(drop=True)
            bottom.index = bottom.index + 1
            st.dataframe(bottom, use_container_width=True)
        
        # Distribution
        st.subheader("📊 Distribution des scores")
        fig = px.histogram(
            scores,
            x='score',
            nbins=10,
            title="Distribution des scores",
            labels={'score': 'Score (%)', 'count': 'Nombre d\'élèves'},
            color_discrete_sequence=['#3B82F6']
        )
        st.plotly_chart(fig, use_container_width=True)

# ==================== TAB 4: EXERCICES DIFFICILES ====================

with tab4:
    st.header("❌ Analyse des exercices")
    
    resultats = get_resultats()
    
    if not resultats.empty:
        # Taux de réussite par TP
        tp_stats = resultats.groupby('tp_name').apply(
            lambda x: (x['statut'] == 'PASSED').sum() / len(x) * 100
        ).sort_values().reset_index(name='taux_reussite')
        tp_stats.columns = ['TP', 'Taux de réussite (%)']
        
        fig = px.bar(
            tp_stats,
            x='Taux de réussite (%)',
            y='TP',
            orientation='h',
            title="Taux de réussite par TP (du plus difficile au plus facile)",
            color='Taux de réussite (%)',
            color_continuous_scale='RdYlGn',
            range_color=[0, 100]
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Détails par TP
        st.subheader("📋 Détails par TP")
        tp_selected = st.selectbox("Sélectionne un TP", tp_stats['TP'].unique())
        
        tp_data = resultats[resultats['tp_name'] == tp_selected]
        
        ex_stats = tp_data.groupby('exercice_num').apply(
            lambda x: {
                'réussite': (x['statut'] == 'PASSED').sum() / len(x) * 100,
                'total': len(x)
            }
        ).apply(pd.Series).reset_index()
        ex_stats.columns = ['Exercice', 'Taux de réussite (%)', 'Nombre de tests']
        
        fig = px.bar(
            ex_stats,
            x='Exercice',
            y='Taux de réussite (%)',
            title=f"Taux de réussite par exercice - {tp_selected}",
            color='Taux de réussite (%)',
            color_continuous_scale='RdYlGn',
            range_color=[0, 100]
        )
        st.plotly_chart(fig, use_container_width=True)

# ==================== TAB 5: DÉTAILS ÉLÈVE ====================

with tab5:
    st.header("👤 Détails par élève")
    
    eleves = get_eleves()
    eleve_selected = st.selectbox("Sélectionne un élève", eleves['nom'].unique())
    
    eleve_id = eleves[eleves['nom'] == eleve_selected]['id'].values[0]
    
    resultats = get_resultats()
    eleve_resultats = resultats[resultats['eleve_id'] == eleve_id]
    
    if not eleve_resultats.empty:
        # Stats globales
        col1, col2, col3 = st.columns(3)
        
        total_tests = len(eleve_resultats)
        tests_passes = (eleve_resultats['statut'] == 'PASSED').sum()
        score_global = tests_passes / total_tests * 100
        
        with col1:
            st.metric("Score global", f"{score_global:.1f}%")
        
        with col2:
            st.metric("Tests réussis", f"{tests_passes}/{total_tests}")
        
        with col3:
            last_test = eleve_resultats['date_test'].max()
            st.metric("Dernier test", last_test)
        
        st.divider()
        
        # Progression par TP
        st.subheader("📊 Progression par TP")
        
        tp_progression = eleve_resultats.groupby('tp_name').apply(
            lambda x: {
                'réussite': (x['statut'] == 'PASSED').sum() / len(x) * 100,
                'total': len(x)
            }
        ).apply(pd.Series).reset_index()
        tp_progression.columns = ['TP', 'Score (%)', 'Exercices']
        
        fig = px.bar(
            tp_progression,
            x='TP',
            y='Score (%)',
            title="Score par TP",
            color='Score (%)',
            color_continuous_scale='RdYlGn',
            range_color=[0, 100]
        )
        fig.update_yaxes(range=[0, 100])
        st.plotly_chart(fig, use_container_width=True)
        
        # Détail complet
        st.subheader("📋 Détail de tous les tests")
        
        detail = eleve_resultats[['tp_name', 'exercice_num', 'statut', 'date_test']].copy()
        detail.columns = ['TP', 'Exercice', 'Statut', 'Date']
        detail['Statut'] = detail['Statut'].apply(lambda x: '✅' if x == 'PASSED' else '❌')
        
        st.dataframe(detail, use_container_width=True, hide_index=True)
    else:
        st.warning(f"Pas encore de résultats pour {eleve_selected}")

# Footer
st.divider()
st.markdown(
    """
    <div style='text-align: center; color: gray; font-size: 12px;'>
    📊 Dashboard Auto-Grading v1.0 | Dernière mise à jour: """ + datetime.now().strftime("%d/%m/%Y %H:%M") + """
    </div>
    """,
    unsafe_allow_html=True
)
